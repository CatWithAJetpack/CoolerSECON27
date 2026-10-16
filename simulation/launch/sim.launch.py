"""Start Gazebo with the race track world and spawn the camera robot."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

SIM_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
URDF_PATH = os.path.join(SIM_DIR, 'models', 'robot', 'robot.urdf')
WORLD_PATH = os.path.join(SIM_DIR, 'worlds', 'track.sdf')
BRIDGE_PATH = os.path.join(SIM_DIR, 'config', 'bridge.yaml')

# Spawn pose: center of the 12 x 12 in start box (x 9..21 in,
# y -34.52..-22.52 in in the CAD frame), facing the racecourse (+y).
SPAWN_X = '0.381'
SPAWN_Y = '-0.72442'
SPAWN_Z = '0.05'
SPAWN_YAW = '1.5708'


def generate_launch_description():
    with open(URDF_PATH) as f:
        robot_description = f.read()

    # gui:=false starts only the Gazebo server (-s). A Gazebo GUI on
    # another machine can then connect to the server over gz-transport.
    gui_arg = DeclareLaunchArgument(
        'gui', default_value='true',
        description='Start the Gazebo GUI with the server')
    server_only_flag = PythonExpression([
        "'' if '", LaunchConfiguration('gui'), "' == 'true' else '-s '"])

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory('ros_gz_sim'),
            'launch', 'gz_sim.launch.py')),
        launch_arguments={
            'gz_args': ['-r ', server_only_flag, WORLD_PATH],
            'on_exit_shutdown': 'true',
        }.items(),
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True,
        }],
        output='screen',
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'race_robot',
            '-x', SPAWN_X, '-y', SPAWN_Y, '-z', SPAWN_Z, '-Y', SPAWN_YAW,
        ],
        output='screen',
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': BRIDGE_PATH,
            'use_sim_time': True,
        }],
        output='screen',
    )

    return LaunchDescription([
        gui_arg,
        gz_sim,
        robot_state_publisher,
        spawn_robot,
        bridge,
    ])
