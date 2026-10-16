# AprilTags

Source: GM2 V3.0, sections 3.3, 3.4.1, Appendix C, and Appendix G, and the Arena Build Guide.

## What They Are

AprilTags are visual fiducial markers for robotics. The robot's camera reads the tag ID to find its assigned pit box.

Reference: https://april.eecs.umich.edu/software/apriltag

---

## Tag Specs

| Property | Value | Source |
|---|---|---|
| IDs used | 1, 2, 3 | GM2 3.3 |
| Tags on the field per match | 1 | GM2 3.3 |
| Size | Approximately 4 x 4 in | Arena Build Guide |
| Family | Not stated in GM2 V3.0 | See open question |

NOTE: An earlier version of this file listed family 41h12 and a size of 68 mm. Neither value appears in GM2 V2.0 or V3.0. Confirm both on the Q&A before relying on them.

---

## ID to Pit Box

| Tag ID | Assigned Pit Box |
|---|---|
| 1 | Pit box 1 |
| 2 | Pit box 2 |
| 3 | Pit box 3 |

---

## Placement

- One tag is selected by the die roll and mounted before each match.
- GM2 3.4.1: "fastened to the wall by the starting area".
- GM2 3.3: "mounted to the Field on the wall separating the pit area from the racecourse".
- GM2 Figure 3.2.1 marks one tag on the side wall next to the start box. It also marks three tag positions on the pit end wall, one behind each pit box.
- The Arena Build Guide says the tags attach to the board magnetically.
- Do not interact with the tag after placement. Doing so voids AprilTag-related scoring (GM2 <GS01>).

---

## Physical Handling

Cut the tags out and laminate them (GM2 Appendix C).

---

## Detection Tips

- Read the tag early. The robot starts in the start box next to the tag.
- Test detection under varying light. The competition venue may differ from your lab.

---

## Open Question

Which tag family and exact size does the GDC use? Ask on the official SoutheastCon Discord Q&A.
