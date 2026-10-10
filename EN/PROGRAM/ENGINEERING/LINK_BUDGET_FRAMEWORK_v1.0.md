# Link Budget Framework v1.0

## Purpose
A common communications-calculation template for Cosmic Programm missions. Specific parameters are filled in after selecting the frequency band, orbit, antennas and ground segment.

## Main equation
Pr = Pt + Gt + Gr − Lspace − Latm − Lpol − Lpoint − Lother

where Pt is transmitter power; Gt/Gr are antenna gains; Lspace is free-space loss; Latm is atmospheric loss; Lpol is polarization loss; Lpoint is pointing loss; and Lother represents other losses.

## Space segment
- orbit and altitude;
- frequency band;
- transmitter power;
- antenna gain and pattern;
- pointing errors;
- coding and modulation;
- required data rate;
- duty cycle;
- power constraints.

## Ground segment
- antenna type and parameters;
- gain;
- receiver sensitivity;
- noise temperature;
- station availability;
- contact-window duration;
- geometric and weather constraints.

## Data channel
Distinguish commands, engineering telemetry, critical events, useful payload data, service data and retransmissions.

## Sensitivity
Separately analyse degraded pointing, reduced power, increased losses, shorter contact windows, prediction errors and equipment degradation.

## Calculation output
Geometry → transmitter parameters → antenna parameters → losses → Eb/N0 or SNR → data rate → BER/FER → margin → availability → constraints.

Status: FRAMEWORK / specific values require a mission-specific calculation.
