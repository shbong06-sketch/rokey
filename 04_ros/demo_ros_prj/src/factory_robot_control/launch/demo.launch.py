"""
데모 전체 실행용 런치 파일.

지정된 수만큼의 AMR 노드와 관제 센터 노드를 동시에 실행합니다.

사용법:
    ros2 launch factory_robot_control demo.launch.py num_robots:=3
    ros2 launch factory_robot_control demo.launch.py num_robots:=10
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_nodes(context):
    """런치 컨텍스트에서 노드 목록을 동적으로 생성합니다."""
    num_robots_str = LaunchConfiguration('num_robots').perform(context)
    num_robots = int(num_robots_str)

    # 관제 센터 노드
    control_center_node = Node(
        package='factory_robot_control',
        executable='control_center_node',
        name='control_center_node',
        output='screen',
        parameters=[{'num_robots': num_robots}]
    )

    # AMR 노드 생성
    amr_nodes = []
    for i in range(1, num_robots + 1):
        amr_node = Node(
            package='factory_robot_control',
            executable='amr_node',
            name=f'amr_node_{i}',
            output='screen',
            parameters=[{'robot_id': i}]
        )
        amr_nodes.append(amr_node)

    return [control_center_node] + amr_nodes


def generate_launch_description():
    """런치 설명 생성."""
    num_robots_arg = DeclareLaunchArgument(
        'num_robots',
        default_value='3',
        description='실행할 로봇 수'
    )

    nodes = OpaqueFunction(function=generate_nodes)

    return LaunchDescription([
        num_robots_arg,
        nodes
    ])
