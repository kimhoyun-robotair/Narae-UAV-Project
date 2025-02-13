
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloSubscriber(Node):
    def __init__(self):
        super().__init__('hello_subscriber')  # 노드 이름 설정
        self.subscription = self.create_subscription(
            String,
            'hello_topic',  # 구독할 토픽 이름
            self.listener_callback,
            10)  # 큐 크기 설정
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Subscriber Node Started')

    def listener_callback(self, msg):
         self.get_logger().info('Received: "%s"' % msg.data)  # 수정된 로그 메시지 형식


def main(args=None):
    rclpy.init(args=args)
    node = HelloSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Subscriber Node Stopped')
    finally:
        node.destroy_node()
        rclpy.shutdown()

