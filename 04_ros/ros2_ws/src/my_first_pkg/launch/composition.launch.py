from launch import LaunchDescription
from launch_ros.actions import (ComposableNodeContainer)
from launch_ros.descriptions import (ComposableNode)

def generate_launch_description():
    return LaunchDescription([
            ComposableNodeContainer(
                name='my_container', namespace='',
                package='rclcpp_components',
                executable='component_container',
                composable_node_descriptions=[
                    ComposableNode(
                        package='composition',
                        plugin='composition::Talker',
                        name='talker',
                        extra_arguments=[{'use_intra_process_comms':True}],
                        ),
                    ComposableNode(
                        package='composition',
                        plugin='composition::Listener',
                        name='listener',
                        extra_arguments=[{'use_intra_process_comms':True}],
                        ),
            ])
        ])