"""
AMR 노드 실행용 런치 파일.

사용법:
    ros2 launch factory_robot_control amr.launch.py robot_id:=1
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    """런치 설명 생성."""
    robot_id_arg = DeclareLaunchArgument(
        'robot_id',
        default_value='1',
        description='AMR 로봇 ID'
    )

    amr_node = Node(
        package='factory_robot_control',
        executable='amr_node',
        name='amr_node',
        output='screen',
        parameters=[{'robot_id': LaunchConfiguration('robot_id')}]
    )

    return LaunchDescription([robot_id_arg, amr_node])
