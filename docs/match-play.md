# Match Play

Source: GM2 V3.0, sections 3.1, 3.2.2, 3.4.2, and 3.5.2.

## Start

The match starts when the referee raises the green start flag and declares the match started (GM2 3.4.2):

```
FLAG DOWN → REFEREE RAISES FLAG → MATCH/TIMER START → FLAG REMAINS UP AND OUT OF ROBOT'S PATH
```

- The robot should detect the flag autonomously.
- If the robot does not start with the flag, the technician can press the start button or switch.
- A robot that uses a start switch must stay still for 5 seconds after the press (GM1 <R03>).
- Starting before the flag removes the 10 point flag start bonus. It also gives a Yellow Card and a 2 point penalty (GM2 <G05>).

NOTE: GM2 section 3.1 says the robot begins "when the green flag is lowered". Sections 3.4.1 and 3.4.2 say the flag starts down and the referee raises it. The procedure in 3.4.2 is the detailed one. Confirm on the Q&A.

NOTE: The start flag tower design is not final. GM2 Appendix F says "Details will be provided in Version 3.1."

---

## Race Flow

```
Start Box
   |
Enter course (+25 pts)
   |
Lap 1
   |
[Pit stop here, or after lap 2]
   |
Lap 2
   |
[Pit stop here, if not done after lap 1]
   |
Lap 3, the final lap: raise the school flag for +25 pts
   |
Cross finish line
   |
End in the assigned pit box (+15 pts)
```

---

## Lap Rules

- 3 laps total.
- Finish all 3 laps within **3 minutes** for the 100 point completion bonus.
- Finish in less than **2 minutes 45 seconds** for 30 more points.
- Each lap earns clean lap bonuses independently:
  - No gray wall contact: +15 pts
  - No obstacle contact: +25 pts

---

## Flag Raising

- Raise a school flag, logo, colors, or emblem during the final (victory) lap.
- Worth 25 points.

---

## Timer

- 3 minutes from match start.
- No extension for a late start, and no penalty (GM2 <G05>).
- Actions after time expires do not score (GM2 <G06>).
- Field damage after time expires still gives a Yellow Card.

---

## Autonomous Operation

The robot must operate fully on its own once the match starts. No external commands or signals of any kind (GM2 <G07>, GM1 <R19>).
