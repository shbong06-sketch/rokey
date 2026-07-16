import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_interfaces.action import CountUntil

class CountClient(Node):
    # CountClient 만들기
    # 액션 서버 상태 확인
    # Goal을 정해서
    # 액션 서버에게 전달
    # 잘 전달되었는지, 피드백 확인, 결과 확인 -> 비동기
    def __init__(self):
        super().__init__('count_client')
        self._cli = ActionClient(self, CountUntil, 'count_until')
        self._cli.wait_for_server()
        goal = CountUntil.Goal()
        goal.target = 15
        fut = self._cli.send_goal_async(goal=goal, feedback_callback=self.on_fb)
        fut.add_done_callback(self.on_goal)
    
    def on_fb(self, msg):
        # 피드백 어떻게 처리하나 -> 그냥 출력하자
        # log는 문자열로 처리. 문자열 이외의 형태는 에러 발생
        self.get_logger().info(f"현재 진행중 {str(msg.feedback.current)}")

    def on_goal(self, fut):
        # 목표달성하면 어떻게 처리하나
        gh = fut.result()
        if not gh.accepted:
            self.get_logger().warning("목표 거절됨")
        gh.get_result_async().add_done_callback(self.on_result)

    def on_result(self, fut):
        ret = fut.result().result
        self.get_logger().info(f"최종 결과 : {str(ret.reached)}")


def main():
    rclpy.init()
    node = CountClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()