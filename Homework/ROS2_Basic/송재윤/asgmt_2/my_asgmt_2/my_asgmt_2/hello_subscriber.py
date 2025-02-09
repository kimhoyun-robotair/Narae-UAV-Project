import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class HellowSubscriber(Node):

    def __init__(self):
        super().__init__('hello_subscriber')
        qos_profile = QoSProfile(depth=10)
        self.hello_subscriber = self.create_subscription(
            String,
            'hello',
            self.subscribe_topic_message,
            qos_profile)
        
    def subscribe_topic_message(self, msg):
        self.get_logger().info('Recevied message: {0}'.format(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = HellowSubscriber()
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