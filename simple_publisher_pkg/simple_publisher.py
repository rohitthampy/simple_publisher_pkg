import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePlublisher(Node):

    def __init__(self):

        super().__init__("simple_publisher")

        self.topic_publisher = self.create_publisher(String, 'pub_topic', 10)

        time_period = 0.5

        self.timer = self.create_timer(timer_period_sec=time_period, callback=self.timer_callback)

        self.count = 0

    def timer_callback(self):
        
        my_msg = String()

        my_msg.data = f"Hello from Docker {self.count}"

        self.topic_publisher.publish(msg=my_msg)

        self.count += 1


def main(args=None):
    
    rclpy.init(args=args)

    simple_publisher = SimplePlublisher()
    
    try:

        rclpy.spin(simple_publisher)

    except KeyboardInterrupt:
        
        simple_publisher.destroy_node()
        
    # rclpy.shutdown()


if __name__ == "__main__":
    main()
        

