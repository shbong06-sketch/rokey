from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_pkg',
            executable='battery_sub',
            name='battery_sub',
            output='screen',
        ),
        Node(
            package='my_first_pkg',
            executable='battery_pub',
            name='battery_pub',
            output='screen',
        ),
    ])