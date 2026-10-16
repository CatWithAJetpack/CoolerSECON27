# Field

Source: Game Manual 2 (GM2) V3.0, section 3.2 and Figure 3.2.1, and the official arena CAD (`2027 IEEE SoutheastCon Arena_Fusion360.f3d`). Measured values below come from the CAD.

## Overview

The field is one 4 ft x 8 ft board: 23/32 in. x 4 ft. x 8 ft. RTD Sheathing Syp. It has two areas: the racecourse and the pit area.

| Area | Length along the board |
|---|---|
| Racecourse | 68 in |
| Pit area | 28 in |

---

## Racecourse

- Octagon-shaped white line on a black board. The line is 0.90 in wide on the straight sides.
- Octagon sides (CAD): long sides 36.65 in, end sides 13.03 in (outer edge), diagonals 9.78 in at 52.5 degrees.
- Center divider wall, 36 in long, inside the octagon. See the open question below.
- Two lanes on each long straightaway: the inner lane (between the divider and the line) and the outer lane (between the line and the wall).

---

## Pit Area

- Three pit boxes, numbered 1 to 3. Each box is 12 x 12 in, painted white.
- The boxes sit against the pit end wall, 2 in from each side wall, 3 in apart.
- Start box: 12 x 12 in, painted white, between pit box 3 and the racecourse.
- Pit divider wall between the pit area and the racecourse: 15.95 x 1.52 x 1 in (CAD).
- Checkered lines: two strips, 15 in long and 4 in deep, one on each side of the pit divider.

---

## Walls

| Element | Size | Color |
|---|---|---|
| Perimeter walls | 1 in thick, 4 in tall | Gray on the racecourse, black on the pit area |
| Pit divider | 15.95 x 1.52 x 1 in | Gray |
| Center divider | 36 in long (see open question) | Gray |

Gray walls count for the clean lap bonus. See scoring.md.

---

## Colors

| Area | Color | Paint Code |
|---|---|---|
| Board and pit area walls | Black (Onyx) | PPG1011-7 |
| Racecourse walls and dividers | Gray (Winter Chill) | PPG1036-2 |
| Racecourse line, pit boxes, start box | White (Delicate White) | PPG1001-1 |

---

## Tolerances

Field and game elements may vary by **± 1 inch (25.4 mm)** per match (GM2 <G02>). Design your robot to handle this.

---

## Obstacles

- **Three** obstacle cars, placed randomly on the racecourse (GM2 3.1).
- The obstacles go in different lanes, on the straightaways, in the inner lane and the outer lane (GM2 3.4.1).
- Placement zones are in GM2 Appendix E. See below.
- The build guide uses Melissa & Doug pull-back plush vehicles, approximately 8.55 in long, 8.2 in wide, and 4.5 in tall.
- Do not interact with them after placement (GM2 <GS01>).

### Placement zones (GM2 Appendix E)

- Four zones, all the same size. Two on each side of the center divider.
- Along the straightaway: each zone runs 16 in from one end of the center divider. The two zones on a side have 4 in between them.
- Across the straightaway: each zone starts 2 in from the side wall and stops 2 in from the center divider, for a total width of 16 in.

---

## Open Questions

Ask these on the official SoutheastCon Discord Q&A. Q&A answers override the game manuals (GM1 <C00>).

1. **Center divider size.** GM2 V3.0 changed the drawing label from 1x1 to "1"x2"x36"". The finished size and orientation are not stated. The CAD shows 1 x 1 x 36 in.
2. **Obstacle zone width.** The CAD leaves 22.5 in between the side wall and the center divider. With 2 in margins on each side, a zone is 18.5 in wide, not 16 in.
3. **Center divider position.** The CAD puts it 16 in from the pit divider and 15 in from the far wall. The Arena Build Guide drawing shows 15 in and 16 in. GM2 V3.0 Figure 3.2.1 shows 15 in at both ends, which leaves 1 in unaccounted.
4. **Pit divider size.** Figure 3.2.1 labels it "1"x1"x16"". The CAD makes it 15.95 x 1.52 x 1 in.
