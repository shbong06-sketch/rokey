import rclpy
from rclpy.node import Node
from my_interfaces.srv import Guess
from my_interfaces.msg import GameState

class GameServer(Node):
    def __init__(self):
        super().__init__("game_server")
        self.word = "robot"
        # 맞춘 단어, 남은 기회
        self.shown = ["_"] * len(self.word)
        self.lives = 6
        # 방송 기능
        self.pub = self.create_publisher(GameState, "game_state", 10)
        # 추론에 대한 응답 기능
        self.create_service(Guess, 'guess', self.on_guess)

    def on_guess(self, request, response):
        # 요청 알파벳 받기
        g = request.letter.strip().lower()
        # 판단
        if len(g) != 1:
            response.correct = False
            response.display = " ".join(self.shown)
            response.lives_left = self.lives
            return response
        # 들어온 문자가 문제 단어에 들어있는지?
        if g in self.shown:    # 중복 처리 방지
            response.correct = False
        
        elif g in self.word:    # 들어 있다면
            # word에 단어를 하나씩 확인해서, 주어진 letter와 같은 위치의 shown 값을 업데이트
            for idx, c in enumerate(self.word):
                if g == c:
                    self.shown[idx] = c
            response.correct = True

        else :      # 없으면
            self.lives -= 1
            response.correct = False
            
        response.display = " ".join(self.shown)
        response.lives_left = self.lives
        self.publish_state(response.display)

        # 응답
        return response

    def publish_state(self, display):
        m = GameState()
        m.display = display
        m.lives_left = self.lives
        # 게임이 완료되었는가?
        # "_"가 없을 때(display에서)
        # self.lives가 0이 되었을 때
        m.finished = ("_" not in display) or (self.lives <= 0)
        self.pub.publish(m)

def main():
    rclpy.init()
    node = GameServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()