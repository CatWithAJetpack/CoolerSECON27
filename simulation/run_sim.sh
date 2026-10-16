#!/usr/bin/env bash
# Start Gazebo with the race field and robot, and bridge the topics to ROS 2 Jazzy.
#
# Needs Ubuntu 24.04 (native or WSL) with ROS 2 Jazzy installed.
# Usage:
#   ./simulation/run_sim.sh             Gazebo with GUI
#   ./simulation/run_sim.sh gui:=false  Gazebo server only, no window
set -euo pipefail

SIM_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load ROS 2 Jazzy if this shell has not loaded it yet.
if [ -z "${ROS_DISTRO:-}" ]; then
    if [ ! -f /opt/ros/jazzy/setup.bash ]; then
        echo "error: ROS 2 Jazzy not found at /opt/ros/jazzy." >&2
        exit 1
    fi
    set +u
    source /opt/ros/jazzy/setup.bash
    set -u
elif [ "${ROS_DISTRO}" != "jazzy" ]; then
    echo "error: this shell has ROS 2 ${ROS_DISTRO} loaded. Open a new shell with ROS 2 Jazzy." >&2
    exit 1
fi

# Packages the launch file uses.
missing=()
for pkg in ros_gz_sim ros_gz_bridge robot_state_publisher; do
    ros2 pkg prefix "${pkg}" >/dev/null 2>&1 || missing+=("${pkg}")
done
if [ "${#missing[@]}" -gt 0 ]; then
    echo "error: missing ROS 2 packages: ${missing[*]}" >&2
    echo "Install them with:" >&2
    echo "  sudo apt install ros-jazzy-ros-gz ros-jazzy-robot-state-publisher" >&2
    exit 1
fi

exec ros2 launch "${SIM_DIR}/launch/sim.launch.py" "$@"
