# semiconductor temp, vibe 구독
# 요청을 받으면 요청 항목에 대한 값을 리턴

import rclpy
from rclpy.node import Node
from my_interfaces.msg import SemiConductorSensor
from my_interfaces.srv import SemiConductorData

class SemiConductorSub(Node):
    def __init__(self):
        super().__init__('semi_conductor_sub')
        self.temp = 0.0
        self.vibe = 0.0
        # sensor 데이터 구독
        self.create_subscription(SemiConductorSensor, 'semi_conductor/sensor', self.on_sensor, 10)
        # 서비스 구현
        self.create_service(SemiConductorData, 'semi_conductor/data', self.on_info)

    def on_sensor(self, msg):
        self.temp = msg.temp
        self.vibe = msg.vibration
        self.get_logger().info(f"센서 데이터 수신 중. TEMP : {self.temp:.2f}℃    VIBE : {self.vibe:.4f}Hz")
        # 일반적으로 센서 데이터는 누락이 될 수도 있지만, 중요하지 않은 경우도 있고, 실시간성이 중요한 경우가 더 많아 별도의 예외처리는 하지 않는다.
        # 중요한 데이터(누락되면 안되는 액션 목표나 서비스 요청 등)는 ROS에서 별도로 예외처리를 통해 누락을 방지해준다.

    def on_info(self, req, res):
        # TEMP = 1, VIBE = 2
        # 요청받은 데이터를 응답한다.
        data = {req.TEMP : ['온도', self.temp, '도'], req.VIBE : ['진동', self.vibe, 'Hz']}
        data_type = req.semiconductor_data_type
        if data_type in data.keys():
            res.semiconductor_data_result = data[data_type][1]
            self.get_logger().info(f"{data[data_type][0]} 요청 응답 - {data[data_type][0]} : {data[data_type][1]:.4f}{data[data_type][2]}")
        else :
            self.get_logger().warning(f"요청할 데이터의 종류를 다시 확인하세요. 현재 요청 : {data_type}")
        return res

def main():
    rclpy.init()
    try :
        node = SemiConductorSub()
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("상황 정리 중...")
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()