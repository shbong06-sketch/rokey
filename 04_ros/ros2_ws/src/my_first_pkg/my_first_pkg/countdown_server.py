import rclpy, time
from rclpy.node import Node
from rclpy.action import ActionServer
from my_interfaces.action import CountDown

class CountDownServer(Node):
    def __init__(self):
        super().__init__('count_down_server')
        self.srv = ActionServer(
            self, CountDown, 'count_down', self.execute_cb
        )
        self.get_logger().info('Waiting for goal request...')

    def execute_cb(self, gh):
        fb = CountDown.Feedback()
        for i in range(gh.request.start, 0, -1):
            self.get_logger().info(f'Countdown: {i}')
            fb.remain = i
            gh.publish_feedback(fb)
            time.sleep(1.0)
        gh.succeed()
        self.get_logger().info('Goal Request Completed. Waiting for another goal request...')
        res = CountDown.Result()
        res.done = True
        return res

def main():
    rclpy.init()
    node = CountDownServer()
    rclpy.spin(node)
    rclpy.shutdown()