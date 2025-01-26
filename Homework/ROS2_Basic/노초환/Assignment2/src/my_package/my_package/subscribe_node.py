import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SubscribeNode(Node):
    def __init__(self):
        super().__init__('subscribe_node')
        self.subscription = self.create_subscription(String,"NET1",self.callback,10)
        self.subscription  
        self.get_logger().info("Subscribe Node has been started.")

    def callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    subscribe_node = SubscribeNode()
    rclpy.spin(subscribe_node)
    subscribe_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
