import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloPublisher(Node):
    def __init__(self):
        super().__init__('hello_publisher')  # 노드 이름 설정
        self.publisher = self.create_publisher(String, 'hello_topic', 10)  # 토픽 이름과 큐 크기 설정
        self.timer = self.create_timer(1.0, self.publish_message)  # 1초마다 메시지 발행
        self.get_logger().info('Publisher Node Started')

    def publish_message(self):
        msg = String()
        msg.data = "Hello, It's My First ROS2 Package"  # 발행할 메시지
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = HelloPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Publisher Node Stopped')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
