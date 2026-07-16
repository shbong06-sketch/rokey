from launch import LaunchDescription
from launch_ros.actions import Node

test_concepts = ['A', 'B']

def generate_launch_description():
    return LaunchDescription(
        # [
        #     Node(
        #         package='my_first_pkg',
        #         executable='talker',
        #         name='talker_a',
        #     ),
        #     Node(
        #         package='my_first_pkg',
        #         executable='talker',
        #         name='talker_b',
        #         remappings=[('chatter', 'chatter_b')],
        #     ),
        #     Node(
        #         package='my_first_pkg',
        #         executable='listener',
        #     ),
        #     Node(
        #         package='my_first_pkg',
        #         executable='greeter',
        #         parameters=[{'who': 'ROBOT'}],
        #     ),
        # ]
        # [ Node(package='my_first_pkg', executable='talker', name=f'talker_{i}', remappings=[('chatter', f'chatter_{i}')]) for i in test_concepts ]
        # 리스트 컴프리헨션 장점 - 속도가 빠르다.

        # 블로킹 포함
        [
            Node(package='my_first_pkg', executable='talker', name='talker_main'),
            Node(package='my_first_pkg', executable='blocking_fixed'),
            Node(package='my_first_pkg', executable='add_client'),
            Node(package='my_first_pkg', executable='add_server'),
            Node(package='my_first_pkg', executable='battery_pub'),
            Node(package='my_first_pkg', executable='battery_sub'),
            Node(package='my_first_pkg', executable='speed_pub'),
            Node(package='my_first_pkg', executable='speed_sub'),
        ]
        
    )

# remmapings= [('원래 이름', '바꿀 이름')]