import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Int32, Bool
from my_robot_interfaces.msg import BesturingsData
import can
import struct
from geometry_msgs.msg import Twist

class CmdVelReader(Node):
    def __init__(self):
        super().__init__('cmd_vel_reader')
        self.cmd_vel_subscription = self.create_subscription(Twist, '/cmd_vel',  self.cmd_vel_callback, 10)


    def cmd_vel_callback(self, msg: Twist):
        #inverted zodat het overeenkomt met het aansturen van de motor (sturen)
        inverted_angular_z = -msg.angular.z
        print(f"linear x: {msg.linear.x}, Angular z: {inverted_angular_z}")



def main(args=None):
    rclpy.init(args=args)
    node = CmdVelReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()