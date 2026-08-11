"""
대시보드 포함 데모 실행용 런치 파일.

AMR 노드, 관제 센터, 웹 대시보드를 동시에 실행합니다.

사용법:
    ros2 launch factory_robot_control dashboard.launch.py
    ros2 launch factory_robot_control dashboard.launch.py num_robots:=5
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, LogInfo, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_nodes(context):
    """런치 컨텍스트에서 노드 목록을 동적으로 생성합니다."""
    num_robots_str = LaunchConfiguration('num_robots').perform(context)
    port_str = LaunchConfiguration('port').perform(context)
    num_robots = int(num_robots_str)

    # 관제 센터 노드
    control_center_node = Node(
        package='factory_robot_control',
        executable='control_center_node',
        name='control_center_node',
        output='screen',
        parameters=[{'num_robots': num_robots}]
    )

    # 대시보드 서버
    dashboard_process = ExecuteProcess(
        cmd=['python3', '-m', 'factory_robot_control.dashboard_server',
             f'--robots={num_robots_str}',
             f'--port={port_str}'],
        output='screen'
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

    log_msg = LogInfo(msg=[f'대시보드 접속: http://localhost:{port_str}'])

    return [log_msg, control_center_node, dashboard_process] + amr_nodes


def generate_launch_description():
    """런치 설명 생성."""
    num_robots_arg = DeclareLaunchArgument(
        'num_robots',
        default_value='3',
        description='실행할 로봇 수'
    )

    port_arg = DeclareLaunchArgument(
        'port',
        default_value='8080',
        description='대시보드 포트'
    )

    nodes = OpaqueFunction(function=generate_nodes)

    return LaunchDescription([
        num_robots_arg,
        port_arg,
        nodes
    ])
