import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    world = LaunchConfiguration('world')

    declare_world = DeclareLaunchArgument(
        'world',
        default_value='/usr/share/gazebo-11/worlds/empty.world',
        description='Gazebo world file'
    )

    # Lancer Gazebo avec le monde choisi
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={'world': world}.items()
    )

    # Lancer le robot Go2
    go2_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('go2_config'),
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    return LaunchDescription([
        declare_world,
        gazebo,
        go2_sim
    ])
