# 중요!
# 타입 약속을 통한 서비스 요청과 구독 동작

import rclpy
from rclpy.node import Node
from my_interfaces.srv import Guess
from my_interfaces.msg import GameState

class Player(Node):
    def __init__(self):
        super().__init__('player')
        # 서비스 클라이언트
        self.cli = self.create_client(Guess, 'guess')
        # 구독
        self.create_subscription(GameState, 'game_state', self.on_state, 10)
        self.cli.wait_for_service()

        # ================================
        # **TEST 시나리오 만들기**
        # ================================
        # 테스트 전용
        # 테스트용으로 미리 요청할 문자들 세팅
        self.letters = list("xroybot")
        # 추가될 내용
        self.idx = 0
        # 요청하는 것도 자동으로 요청하도록 한다. -> 3초마다 계획된 문자들을 하나씩 던져본다.
        self.create_timer(3.0, self.guess)


    def guess(self):
        # IndexError 방지: len(self.letters) == 7 >> self.idx 는 최대 6까지
        if self.idx >= len(self.letters): return
        # self.letters에서 하나씩 문자를 뽑아서
        req = Guess.Request()
        req.letter = self.letters[self.idx]
        self.idx += 1
        # 이 문자를 서비스로 호출
        self.cli.call_async(req)
        
    def on_state(self, msg):
        # 구독한 내용 출력
        # 진행 : __b_t (남은 기회 : 3)
        self.get_logger().info(f"진행 : {msg.display} (남은 기회 : {str(msg.lives_left)})")
        if msg.finished:
            self.get_logger().warning("수고하셨습니다! 게임 끝!!")        

def main():
    rclpy.init()
    node = Player()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()