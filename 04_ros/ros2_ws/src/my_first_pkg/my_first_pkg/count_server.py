import rclpy, time
from rclpy.node import Node
# 액션 -> 액션 서버
from rclpy.action import ActionServer
# 인터페이스
from my_interfaces.action import CountUntil

from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

class CountServer(Node):
    def __init__(self):
        super().__init__('count_server')
        self.declare_parameter('interval', 0.5) # 시간 간격
        grp = ReentrantCallbackGroup()
        self.srv = ActionServer(
            self,
            CountUntil,
            'count_until',
            execute_callback=self.execute_cb,
            callback_group=grp,
        )

    def execute_cb(self, goal_handle):
        fb = CountUntil.Feedback()  # target -> 10
        for i in range(1, goal_handle.request.target + 1):
            iv = self.get_parameter("interval").value
            fb.current = i
            goal_handle.publish_feedback(fb)
            self.get_logger().info('간격 %.1fs -> %d/%d' % (iv, i, goal_handle.request.target))
            time.sleep(iv)
            if goal_handle.is_cancel_requested:
                # 취소작업 하려면, cancel_callback() 함수 만들고, MultiThreadedExecutor에서 Return CancelResponse() 해야함.
                # 취소 요청이 오게 되면, 어떤 식으로 처리할 것인지에 대해 섬세하게 설계해야 함.
                pass
        goal_handle.succeed()
        res = CountUntil.Result()
        res.reached = True
        return res

def main():
    rclpy.init()
    node = CountServer()
    ex = MultiThreadedExecutor()    # rclpy.spin(node) 대신 executor를 만들어 spin()
    ex.add_node(node)
    ex.spin()
    rclpy.shutdown()

if __name__ == '__main__':
    main()