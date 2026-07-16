# semiconductor_pub 만들기
# 1. 상속 - Node
# 2. pub 생성 - create_publisher(메시지타입, '토픽명', 버퍼)
# 3. timer 구성 - 몇 초, 콜백
# 4. 콜백함수 - temp, vibration 값 랜덤 생성 -> 송출 -> 로그로 출력
# 5. main 돌리기 - 병렬 필요? no

import rclpy
from rclpy.node import Node
from my_interfaces.msg import SemiConductorSensor
import random

class SemiCondutorPub(Node):
    def __init__(self):
        super().__init__('semi_conductor_sensor')
        self.pub = self.create_publisher(SemiConductorSensor, 'semi_conductor/sensor', 10)
        self.create_timer(0.5, self.tick)

    def tick(self):
        msg = SemiConductorSensor()
        msg.temp = random.uniform(40.0, 70.0)
        msg.vibration = random.uniform(0.0, 1.0)
        self.pub.publish(msg)
        self.get_logger().info(f"temp : {msg.temp:.2f}  vibration : {msg.vibration:.4f}")

def main():
    rclpy.init()
    try:
        node = SemiCondutorPub()
        rclpy.spin(node)
    except KeyboardInterrupt:   # ctrl + C로 종료 시 나오는 예외
        # 예외 내용 -> 상황을 정리하는 내용
        # ex) 주행 노드 -> 안전하게 마무리(긴급 정지, ...)
        print("상황 정리하는 내용...")
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
