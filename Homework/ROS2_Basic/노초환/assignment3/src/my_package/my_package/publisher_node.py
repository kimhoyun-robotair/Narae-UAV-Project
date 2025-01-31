import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publish_node')
        self.publisher = self.create_publisher(String, "NET1", 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.get_logger().info("Publish Node has been started.")
        
    def publish_message(self):
        msg = String()
        msg.data = "Hello, It’s My First ROS2 Package"
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        
def main(args=None):
    rclpy.init(args=args)
    publish_node = PublisherNode()
    rclpy.spin(publish_node)
    publish_node.destroy_node()
    rclpy.shutdown()
        
if __name__ == '__main__':
    main()
        
        