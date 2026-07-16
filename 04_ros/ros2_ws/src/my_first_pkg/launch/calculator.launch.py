from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(package='my_first_pkg', executable='argument_node', name='argument_node'),
            Node(package='my_first_pkg', executable='operator_node', name='operator_node'),
        ]
    )

# argument_node, operator_node 실행