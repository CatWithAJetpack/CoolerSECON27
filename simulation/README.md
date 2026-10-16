# Simulation

Gazebo simulation of the race field and robot. ROS 2 nodes in `ros2/src` control the robot.

## Setup

Needs Ubuntu 24.04 (native or WSL) with ROS 2 Jazzy installed. Install the Gazebo packages once:

```bash
sudo apt install ros-jazzy-ros-gz ros-jazzy-robot-state-publisher
```

`run_sim.sh` checks for these packages and prints this command if any are missing.

## Run

```bash
./simulation/run_sim.sh
```

Gazebo opens with the field. The robot spawns in the center of the start box, facing the racecourse.

To start only the Gazebo server, with no GUI, run:

```bash
./simulation/run_sim.sh gui:=false
```

## Topics

| Topic | Use |
|---|---|
| `/cmd_vel` | Drive the robot |
| `/camera/image_raw` | Camera image |
| `/camera/camera_info` | Camera calibration |
| `/odom` | Robot position estimate |

Set `use_sim_time:=true` on every ROS 2 node that talks to the simulation.

## Files

| File | Contents |
|---|---|
| `run_sim.sh` | Starts everything |
| `launch/sim.launch.py` | Starts Gazebo, spawns the robot, connects topics to ROS 2 |
| `worlds/track.sdf` | The field |
| `models/robot/robot.urdf` | The robot and its camera |
| `config/bridge.yaml` | List of topics shared with ROS 2 |

## Field accuracy

`worlds/track.sdf` is built from the official 2027 sources:

1. The arena CAD, `2027 IEEE SoutheastCon Arena_Fusion360.f3d` (June 2026). Every field coordinate comes from this model's vertices.
2. Game Manual 2 V3.0 (9/18/2026, revised 10/4/2026), Figure 3.2.1 and Appendices B and E. A copy is in `docs/Game-Manual-2027-2-V3-1.docx`. The drawing confirms the CAD values.
3. The Arena Build Guide (Valencia College), for paint use and photos.

Get these files from the hardware competition page: <https://ieeesoutheastcon.org/student-competitions/>.

### Modeled from the CAD

| Element | Size (in) | Color |
|---|---|---|
| Board | 48 x 96, 23/32 thick | Onyx PPG1011-7 |
| Racecourse walls | 1 thick, 4 tall | Winter Chill PPG1036-2 |
| Pit area walls | 1 thick, 4 tall | Onyx PPG1011-7 |
| Pit divider | 15.95 x 1.52 x 1 | Winter Chill PPG1036-2 |
| Center divider | 1 x 1 x 36 (see open questions) | Winter Chill PPG1036-2 |
| Octagon line | 0.90 wide on the straight sides | Delicate White PPG1001-1 |
| Pit boxes 1 to 3 | 12 x 12 | Delicate White PPG1001-1 |
| Start box | 12 x 12 | Delicate White PPG1001-1 |

The CAD draws the octagon diagonals at 52.5 degrees, and the diagonal line is 0.71 in wide at one end and 0.85 in at the other. The world copies these values exactly.

Paint colors are the published sRGB values for each PPG code.

### Open questions for the GDC Q&A

Ask these on the official SoutheastCon Discord. Q&A answers override the game manual.

1. Center divider. GM2 V3.0 changed the label from 1x1 to "1"x2"x36"". What is the finished size, and does the board lie flat or on edge?
2. Obstacle zones (Appendix E). Each zone is 16 in wide, and starts 2 in from the side rail and stops 2 in from the center rail. The CAD leaves 22.5 in between the wall and the divider, so the margins give 18.5 in, not 16 in. Which value is correct?
3. Center divider position. The CAD puts it 16 in from the pit divider and 15 in from the far wall. The Arena Build Guide drawing shows 15 in and 16 in. GM2 V3.0 Figure 3.2.1 shows 15 in at both ends, which leaves 1 in unaccounted. The world follows the CAD.
4. Pit divider size. Figure 3.2.1 labels it "1"x1"x16"". The CAD makes it 15.95 x 1.52 x 1 in. The world follows the CAD.

### Not modeled yet

The official sources do not define these elements exactly. They stay out of the world until they do.

| Element | What the sources say |
|---|---|
| Start flag tower | GM2 Appendix F: "Details will be provided in Version 3.1." |
| AprilTag | Build guide: "approximately 4 x 4 in". GM2 V3.0 gives no family or size, and the text names two different walls. See `docs/apriltags.md`. |
| Obstacle cars (3) | Build guide: "approximately 8.55 x 8.2 x 4.5 in". Judges place them in the Appendix E zones before each race. |
| Spare tires | GM2 Appendix D gives an STL. No position inside the pit boxes. |
| Checkered lines | The CAD gives the area: two 15 x 4 in bands at y = -23 to -19 in, 1.5 x 1.333 in squares. Which squares are black is not defined. |
