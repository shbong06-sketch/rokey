from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(package='my_first_pkg', executable='game_server_improvement'),
            Node(package='my_first_pkg', executable='player_improvement'),
        ]
    )