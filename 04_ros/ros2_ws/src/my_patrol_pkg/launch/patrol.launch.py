from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(package='my_patrol_pkg', executable='patrol_robot')
        ]
    )