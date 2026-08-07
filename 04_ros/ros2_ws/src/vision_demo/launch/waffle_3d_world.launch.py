#!/usr/bin/env python3
#
# Turtlebot3-waffle의 2D 라이다를 3D 라이다로 교체한 모델을 띄우는 launch 파일
# turtlebot3_gazebo/launch/turtlebot3_world.launch.py 를 기반으로 작성

import os

os.environ['TURTLEBOT3_MODEL'] = 'waffle'

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_vision_demo = get_package_share_directory('vision_demo')
    pkg_tb3_gazebo = get_package_share_directory('turtlebot3_gazebo')
    ros_gz_sim = get_package_share_directory('ros_gz_sim')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='-2.0')
    y_pose = LaunchConfiguration('y_pose', default='-0.5')

    world = os.path.join(
        pkg_tb3_gazebo,
        'worlds',
        'turtlebot3_world.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': ['-r -s -v2 ', world], 'on_exit_shutdown': 'true'}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-g -v2 ', 'on_exit_shutdown': 'true'}.items()
    )

    # TF 링크(base_scan 등)가 원본과 동일하므로 원본 robot_state_publisher를 재사용
    robot_state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_tb3_gazebo, 'launch', 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    # 2D 라이다를 3D 라이다(수평 360 x 수직 16)로 교체한 waffle 모델
    model_sdf = os.path.join(pkg_vision_demo, 'worlds', 'turtlebot3_waffle_3d.sdf')

    spawn_turtlebot_cmd = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'waffle_3d',
            '-file', model_sdf,
            '-x', x_pose,
            '-y', y_pose,
            '-z', '0.01'
        ],
        output='screen',
    )

    # 2D 라이다(scan)에 더해 3D 라이다 포인트클라우드(scan/points -> PointCloud2)를 브릿지
    bridge_params = os.path.join(
        pkg_vision_demo,
        'config',
        'waffle_3d_bridge.yaml'
    )

    start_gazebo_ros_bridge_cmd = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ],
        output='screen',
    )

    start_gazebo_ros_image_bridge_cmd = Node(
        package='ros_gz_image',
        executable='image_bridge',
        arguments=['/camera/image_raw'],
        output='screen',
    )

    # 모델의 mesh(model://turtlebot3_common)와 월드 리소스를 해석하기 위한 경로 설정
    set_env_vars_resources = AppendEnvironmentVariable(
        'GZ_SIM_RESOURCE_PATH',
        os.path.join(pkg_tb3_gazebo, 'models'))

    ld = LaunchDescription()

    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(spawn_turtlebot_cmd)
    ld.add_action(robot_state_publisher_cmd)
    ld.add_action(start_gazebo_ros_bridge_cmd)
    ld.add_action(start_gazebo_ros_image_bridge_cmd)
    ld.add_action(set_env_vars_resources)

    return ld
