import rclpy
from rclpy.node import Node
from my_interfaces.action import RecordTrajectory
from rclpy.action import ActionServer
# bag record를 실행하는 커멘드를 파이썬 안에서 수행
import os
import signal
import subprocess
import time

class ServerBag(Node):
    def __init__(self):
        super().__init__('record_server')
        ActionServer(self, RecordTrajectory, 'record_action', self.execute_callback, cancel_callback=self.cancel_callback)

    def execute_callback(self, goal_handle):
        duration = goal_handle.request.duration
        self.get_logger().info(f"Action 요청 받은 값 : {str(duration)}")

        # 폴더 경로 생성 - ros2 bag record -o 폴더경로 /토픽명
        # - 현위치/turtle_trajectory_20260722
        bag_path = os.path.join(os.getcwd(), 'turtle_trajectory_'+time.strftime('%Y%m%d_%H%M%S'))
        # 실행 - subprocess 사용
        proc = subprocess.Popen(['ros2', 'bag', 'record', '-o', bag_path, '/turtle1/cmd_vel', '/turtle1/pose'])
        time.sleep(duration)
        # duration 만큼 진행하고 멈추기(signal) : ctrl+C 전달
        proc.send_signal(signal.SIGINT)
        proc.wait()

        goal_handle.succeed()   # 완료되면 이 메서드 호출
        result = RecordTrajectory.Result()
        result.bag_path = bag_path
        result.message_count = 100
        self.get_logger().info(f"녹화 완료 -> {bag_path}")
        return result

    def cancel_callback(self):
        pass

def main():
    rclpy.init()
    rclpy.spin(ServerBag())
    rclpy.shutdown()

# 액션을 가동 -> 하나의 콜백
# "x초 저장해줘" 요청 -> 액션이 가동 -> x초 동안 저장하면서,
# 피드백으로 "n초 진행 중" 내용 전달
# 최종적으로 x개의 메시지, bag 경로 최종 전달

# 추가로 '취소' 요청을 한다면,
# MultiThread executor와 callback group 부분 변경 필요

if __name__ == '__main__':
    main()