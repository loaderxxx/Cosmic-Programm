# BRANCH PROTECTION — DESIRED STATE

Canonical branch: `main`.

Desired GitHub enforcement:
- require pull request before merge;
- require relevant status checks when CI exists;
- require review where appropriate;
- block force-push;
- block deletion;
- keep `agent/cursor` and `agent/chatgpt` available.

Bootstrap verification has not enabled GitHub enforcement yet. This file records the intended state; repository settings must be enabled/verified separately.

Until enforcement is enabled, agents must follow the policy procedurally and must not push directly to main except explicit owner-authorized bootstrap/admin actions.
