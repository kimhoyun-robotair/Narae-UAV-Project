import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class HelloPublisher(Node):

    def __init__(self):
        super().__init__('hello_publisher')
        qos_profile = QoSProfile(depth=10)
        self.hello_publisher = self.create_publisher(String, 'hello', qos_profile)
        self.timer = self.create_timer(1, self.publish_hello_msg)

    def publish_hello_msg(self):
        msg = String()
        msg.data = 'Hello, It’s My First ROS2 Package'
        self.hello_publisher.publish(msg)
        self.get_logger().info('Published message: {0}'.format(msg.data))
        


def main(args=None):
    rclpy.init(args=args)
    node = HelloPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        if rclpy.ok():  # ✅ shutdown이 호출되지 않은 경우에만 실행  
            rclpy.shutdown()
    #GPT의 깨끗한 shutdown finally코드 적용버전


if __name__ == '__main__':
    main()