from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_asgmt_2',
            executable='hello_publisher',
            name='hello_publisher',
        ),
        Node(
            package='my_asgmt_2',
            executable='hello_subscriber',
            name='hello_subscriber',
        )
    ])