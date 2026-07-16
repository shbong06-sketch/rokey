import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


# 시방서
# 1. 타입 : Float32
# 2. 토픽명 : speed
# 3. 주기 : 0.5초
# 4. 값을 0.0에서 시작해서 0.1씩 증가
# 5. 최대값 10.0 도달 시 0.0으로 리셋
# =======================================

class SpeedPub(Node):
    def __init__(self):
        super().__init__('speed_pub')
        self.pub = self.create_publisher(Float32, 'speed', 10)
        self.v = 0.0
        self.max_speed = 10.0
        self.create_timer(0.5, self.tick)
    
    def tick(self):
        msg = Float32()
        msg.data = self.v
        self.pub.publish(msg)
        self.get_logger().info(f'Speed: {self.v:.1f}')
        self.v += 0.1
        if self.v > self.max_speed:
            self.v = 0.0


def main():
    rclpy.init()
    node = SpeedPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()