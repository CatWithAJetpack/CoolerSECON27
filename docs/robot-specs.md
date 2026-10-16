# Robot Specs

Source: GM1 V3.0, section 5.2, and GM2 V3.0, section 3.5.

## Size (GM1 <R01>)

- Maximum at match start: **12 in. x 12 in. x 12 in.** (304.8 mm).
- Minimum: **10 in. long x 10 in. wide**, for the first **3 in.** up from the surface.
- Game elements the robot starts with (the red tire) may extend outside the starting size.
- The robot may expand after the match starts.
- Only one robot unit is allowed.

---

## Mass (GM1 <R02>)

12 kg maximum (about 26.5 lb), in the heaviest configuration.

---

## Autonomy

Fully autonomous during the match. No external commands, signals, or remote inputs of any kind (GM2 <G07>, GM1 <R19>).

- All processing must happen on the robot (GM1 <R18>).
- Wireless communication is allowed only between parts of the robot itself (GM1 <R19>).

---

## Start Trigger

- The robot should detect the green start flag (GM2 3.4.2).
- A start button or switch is allowed as a backup (GM1 <R03>):
  - One simple electrical button or switch, clearly marked.
  - After the press, the robot must not move for at least **5 seconds**. It may run code, such as lighting an LED, during this time.

---

## Auto-Shutoff

GM2 3.4.3 highly suggests a mechanism that stops the robot automatically 3 minutes after the race starts.

---

## Emergency Stop (GM1 <R04>)

Every robot unit must have a clearly marked emergency stop. It must halt all robot actions safely and quickly.

---

## Tire Carry

The robot starts with the red tire pre-loaded and must exchange it for a blue tire during the pit stop. See pit-stop.md.

---

## Flag Mechanism

The robot must be able to raise a school flag, logo, colors, or emblem during the final lap for the 25 point bonus.

---

## Other Robot Rules

| Rule | Summary |
|---|---|
| <R05> Illegal materials | No sharp edges, explosives, flammable gases, loose materials, field grounding, abrasives, uncontained liquids, or hydraulics |
| <R07> Pneumatics | Allowed up to 100 psi |
| <R08> Aerial robots | Not allowed |
| <R09> Prompt removal | Removable by hand, no tools, no adhesives |
| <R10> Identification | Team must be identifiable from 6 ft away |
| <R12> Launching | Not allowed |
| <R16> Voltage | Power distribution 30 V or less |
| <R17> Lights | No strobes and no visible lasers |

---

## Inspection

All robots and team game elements must pass inspection before use (GM1 6.0, GM2 <TE01>). Team game elements follow the mechanical rules in GM1 section 5.2.1 (GM2 <TE02>).

---

## Field Boundary

The robot must stay on the field at all times. Reaching outside the perimeter gives a Yellow Card. Intentional and consequential violations can give a Red Card (GM2 <S01>).
