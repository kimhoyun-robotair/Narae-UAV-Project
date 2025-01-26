import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class PublishNode(Node):
    def __init__(self):
        super().__init__('publish_node')
        self.publisher = self.create_publisher(String, "NET1", 10)
        self.timer = self.create_timer(1.0, self.callback)
        self.get_logger().info("Publish Node has been started.")
        
    def callback(self):
        msg = String()
        msg.data = "Hello, It’s My First ROS2 Package"
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        
def main(args=None):
    rclpy.init(args=args)
    publish_node = PublishNode()
    rclpy.spin(publish_node)
    publish_node.destroy_node()
    rclpy.shutdown()
        
if __name__ == '__main__':
    main()
        
        