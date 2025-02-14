from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='homework3_pkg',
            executable='hello_publisher',
            name='hello_publisher',
            output='screen'
        ),
        Node(
            package='homework3_pkg',
            executable='hello_subscriber',
            name='hello_subscriber',
            output='screen'
        ),
    ])
