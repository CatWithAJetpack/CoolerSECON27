import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class LaserSubscriber(Node):

    def __init__(self):
        super().__init__("laser_subscriber")
        self.subscription = self.create_subscription(
            float, "laser", self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning


def main(args=None):
    rclpy.init(args=args)

    laser_subscriber = LaserSubscriber()

    rclpy.spin(laser_subscriber)

    laser_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

