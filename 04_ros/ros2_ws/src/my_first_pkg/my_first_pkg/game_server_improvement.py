import rclpy
from rclpy.node import Node
from my_interfaces.srv import Guess
from my_interfaces.msg import GameState

class GameServer(Node):
    def __init__(self):
        super().__init__("game_server")
        # 진행할 단어 목록과 현재 인덱스
        self.words = ["robot", "apple", "python", "sensor"]
        self.word_index = 0
        self.word = self.words[self.word_index]
        # 맞춘 단어, 남은 기회
        self.shown = ["_"] * len(self.word)
        self.lives = 6
        # 방송 기능
        self.pub = self.create_publisher(GameState, "game_state", 10)
        # 추론에 대한 응답 기능
        self.create_service(Guess, 'guess', self.on_guess)

    def is_finished(self):
        # 다 맞췄거나 기회를 모두 소진하면 게임 종료
        return ("_" not in self.shown) or (self.lives <= 0)

    def reset_game(self):
        # 다음 단어로 교체하고 상태 초기화 (목록 끝이면 처음으로 순환)
        self.word_index = (self.word_index + 1) % len(self.words)
        self.word = self.words[self.word_index]
        self.shown = ["_"] * len(self.word)
        self.lives = 6

    def start_game(self, word):
        # 주어진 단어로 새 게임을 시작. 알파벳으로만 이뤄진 단어만 허용
        w = word.strip().lower()
        if len(w) == 0 or not (w.isascii() and w.isalpha()):
            return False
        self.word = w
        self.shown = ["_"] * len(self.word)
        self.lives = 6
        return True

    def apply_guess(self, letter):
        # 게임이 끝난 상태면 새 게임 시작 후 이번 추측은 버림 (옵션 A)
        if self.is_finished():
            self.reset_game()
            return False
        # 순수 로직: 추측 문자를 처리하고 정답 여부(correct)를 반환
        g = letter.strip().lower()
        # 한 글자가 아니면 무시
        if len(g) != 1:
            return False
        # 알파벳(a-z)이 아니면 무시
        if not (g.isascii() and g.isalpha()):
            return False
        # 이미 맞춘 문자 (중복 방지)
        if g in self.shown:
            return False
        # 정답: 해당 위치의 shown 값을 업데이트
        if g in self.word:
            for idx, c in enumerate(self.word):
                if g == c:
                    self.shown[idx] = c
            return True
        # 오답: lives 감소, 단 0 미만으로 내려가지 않게 가드
        if self.lives > 0:
            self.lives -= 1
        return False

    def on_guess(self, request, response):
        # 순수 로직 위임 후 응답 구성
        response.correct = self.apply_guess(request.letter)
        response.display = " ".join(self.shown)
        response.lives_left = self.lives
        self.publish_state(response.display)
        return response

    def publish_state(self, display):
        m = GameState()
        m.display = display
        m.lives_left = self.lives
        # 게임이 완료되었는가?
        m.finished = self.is_finished()
        self.pub.publish(m)

def main():
    rclpy.init()
    node = GameServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
