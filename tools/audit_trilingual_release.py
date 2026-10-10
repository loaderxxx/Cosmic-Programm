#!/usr/bin/env python3
"""Offline, read-only audit; structural checks are not independent source/language review."""
from __future__ import annotations
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
SHA = re.compile(r'^[0-9a-f]{40}$')
LINK = re.compile(r'\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)')
REQ = re.compile(r'\b(?:SYS|REQ)-\d+(?:[-.]\d+)*\b')
FORMULA = 'Pr = Pt + Gt + Gr − Lspace − Latm − Lpol − Lpoint − Lother'
def git(root, *args):
    p = subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,encoding='utf-8',check=False)
    if p.returncode:
        raise RuntimeError('Git read failed: '+' '.join(args)+': '+p.stderr.strip())
    return p.stdout
def source(root, ref, path):
    if not SHA.fullmatch(ref) or path.startswith('/') or '..' in Path(path).parts:
        raise ValueError('Invalid pinned source')
    return git(root,'show',f'{ref}:{path}')
def table_shape(text):
    blocks, current = [], []
    for line in text.splitlines()+['']:
        s=line.strip()
        if s.startswith('|') and s.endswith('|'):
            if re.fullmatch(r'[|\s:\-]+',s):
                continue
            current.append(len(re.split(r'(?<!\\)\|',s))-2)
        elif current:
            blocks.append(current)
            current=[]
    return blocks
def numbers(text):
    text=re.sub(r'.*?','',text)
    text=re.sub(r'https?://[^\s<>]+','',text)
    text=re.sub(r'^#{1,6}\s.*$','',text,flags=re.M)
    text=re.sub(r'^\s*\d+[.)]\s+','',text,flags=re.M)
    text=re.sub(r'(?<=\d),(?=\d{1,2}(?:\D|$))','.',text)
    text=re.sub(r'(?<=\d)[,\u00a0\u202f](?=\d{3}(?:\D|$))','',text)
    return Counter(re.findall(r'(?<![\w-])\d+(?:\.\d+)?(?:\+)?',text))
def audit(root,m):
    if m['locale'] not in ('EN','RU','AR') or not SHA.fullmatch(m['recovered_commit']):
        raise ValueError('Invalid locale or source SHA')
    ref=m['recovered_commit']; errors=[]; warnings=[]; rows=[]
    for pack in m['packs']:
        names=git(root,'ls-tree','-r','--name-only',ref,pack['source_root']).splitlines()
        names=[n for n in names if n.endswith('.md')]
        if pack.get('filename_pattern'):
            names=[n for n in names if re.fullmatch(pack['filename_pattern'],Path(n).name)]
        if len(names)!=pack['expected_count']:
            errors.append({'pack':pack['id'],'type':'source_count','actual':len(names),'expected':pack['expected_count']})
        for src in names:
            rel=src[len(pack['source_root'].rstrip('/'))+1:]
            dest=pack['target_root'].rstrip('/')+'/'+rel; f=root/dest
            if not f.is_file():
                errors.append({'path':dest,'type':'missing_file'}); continue
            text=f.read_text(encoding='utf-8'); original=source(root,ref,src)
            if len(text.strip())<80:
                errors.append({'path':dest,'type':'empty_or_stub'})
            a,b=table_shape(original),table_shape(text)
            if a!=b:
                errors.append({'path':dest,'type':'table_shape','source':a,'edition':b})
            ids=sorted(set(REQ.findall(original))-set(REQ.findall(text)))
            if ids:
                errors.append({'path':dest,'type':'missing_requirement_ids','ids':ids})
            if FORMULA in original and FORMULA not in text:
                errors.append({'path':dest,'type':'formula_changed'})
            missing=numbers(original)-numbers(text)
            if missing:
                warnings.append({'path':dest,'type':'numeric_review','missing':dict(missing)})
            if 'cite' in text:
                warnings.append({'path':dest,'type':'unresolved_legacy_citation'})
            for target in LINK.findall(text):
                u=urlsplit(target.strip('<>'))
                if u.scheme or u.netloc or not u.path: continue
                resolved=(f.parent/unquote(u.path)).resolve()
                if not resolved.is_relative_to(root) or not resolved.exists():
                    errors.append({'path':dest,'type':'broken_local_link','target':target})
            rows.append({'source':src,'path':dest,'bytes':len(text.encode('utf-8')),'tables':len(b)})
    gd=root/m['graph_directory']; g=json.loads((gd/'GRAPH.json').read_text(encoding='utf-8'))
    s=json.loads((gd/'SOURCES.json').read_text(encoding='utf-8'))
    sr=s if isinstance(s,list) else s['sources']; si={x['id'] for x in sr}
    ni=[x['id'] for x in g['nodes']]; ns=set(ni); ei=[]; counts={}
    if len(ni)!=len(ns): errors.append({'type':'duplicate_graph_nodes'})
    for key,status,field in [('evidence_edges','SOURCE_CLAIM','sources'),('hypothesis_edges','HYPOTHESIS','basis')]:
        counts[key]=len(g[key])
        for e in g[key]:
            ei.append(e['id'])
            if e['from'] not in ns or e['to'] not in ns: errors.append({'edge':e['id'],'type':'unknown_endpoint'})
            refs=e.get(field,[])
            if not refs or not set(refs).issubset(si): errors.append({'edge':e['id'],'type':'unresolved_evidence'})
            if e['status']!=status: errors.append({'edge':e['id'],'type':'claim_classification'})
    if len(ei)!=len(set(ei)): errors.append({'type':'duplicate_edges'})
    for c in g.get('constraints',[]):
        if not set(c.get('scope',[])).issubset(set(ei)): errors.append({'constraint':c['id'],'type':'unknown_scope'})
    return {'research_id':m['research_id'],'locale':m['locale'],'head':git(root,'rev-parse','HEAD').strip(),
            'recovered_commit':ref,'structural_result':'PASS' if not errors else 'FAIL',
            'independent_language_review':'NOT_PERFORMED','scientific_source_revalidation':'NOT_PERFORMED_BY_THIS_SCRIPT',
            'documents_checked':len(rows),'graph_nodes':len(ni),'graph_sources':len(si),'edge_counts':counts,
            'errors':errors,'warnings':warnings,'documents':rows}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path('.'))
    p.add_argument('--manifest',type=Path,default=Path('QUALITY/CS-TRI-20261010/manifest.json'))
    p.add_argument('--output',type=Path,default=Path('release-audit.json'))
    a=p.parse_args(); root=a.root.resolve()
    result=audit(root,json.loads((root/a.manifest).read_text(encoding='utf-8')))
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary={k:v for k,v in result.items() if k!='documents'}
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a',encoding='utf-8') as f:
            f.write('## COSMOSYNTH documentation audit\n\n```json\n'+json.dumps(summary,ensure_ascii=False,indent=2)+'\n```\n')
    return 0 if not result['errors'] else 1
if __name__=='__main__':
    try: sys.exit(main())
    except (OSError,ValueError,KeyError,RuntimeError) as e:
        print('AUDIT_ERROR: '+str(e),file=sys.stderr); sys.exit(2)
