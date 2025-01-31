import launch
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='publisher',
            name='publisher_node'
        ),
        Node(
            package='my_package',
            executable='subscriber',
            name='subscriber_node'
        ),
    ])
