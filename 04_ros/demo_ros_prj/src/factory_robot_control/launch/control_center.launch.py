"""
관제 센터 노드 실행용 런치 파일.

사용법:
    ros2 launch factory_robot_control control_center.launch.py
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """런치 설명 생성."""
    control_center_node = Node(
        package='factory_robot_control',
        executable='control_center_node',
        name='control_center_node',
        output='screen'
    )

    return LaunchDescription([control_center_node])
