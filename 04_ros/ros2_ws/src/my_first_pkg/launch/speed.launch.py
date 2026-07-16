from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_pkg',
            executable='speed_sub',
            name='speed_sub',
            output='screen',
        ),
        Node(
            package='my_first_pkg',
            executable='speed_pub',
            name='speed_pub',
            output='screen',
        ),
    ])