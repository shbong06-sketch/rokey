from launch import LaunchDescription
from launch_ros.actions import Node

test_concepts = ['A', 'B', 'C', 'D', 'E']
parameter_list = {concept: {'who': f'ROBOT_{concept}'} for concept in test_concepts}

def generate_launch_description():
    return LaunchDescription([
        Node(package='my_first_pkg', executable='greeter',
             name=f'greeter_{concept}', parameters=[parameter_list[concept]])
        for concept in test_concepts
    ])