import pytest
from my_first_pkg.game_server_improvement import GameServer


@pytest.fixture
def server():
    # rclpy 초기화 없이 __init__을 우회하여 로직만 테스트
    s = GameServer.__new__(GameServer)
    s.words = ["robot", "apple"]
    s.word_index = 0
    s.word = s.words[0]
    s.shown = ["_"] * len(s.word)
    s.lives = 6
    return s


def test_lives_never_negative(server):
    # 단어에 없는 문자를 lives(6)보다 많이 틀려도 음수가 되면 안 된다
    for letter in "xyzwqvkfjm":  # 10번 틀림
        server.apply_guess(letter)
    assert server.lives >= 0


def test_wrong_guess_decreases_lives(server):
    server.apply_guess("x")
    assert server.lives == 5


def test_correct_guess_keeps_lives(server):
    server.apply_guess("r")
    assert server.lives == 6
    assert server.shown[0] == "r"


def test_non_alpha_ignored(server):
    # 숫자, 기호는 무시되고 lives가 깎이지 않는다
    for ch in ["1", "@", "!", " ", "3"]:
        assert server.apply_guess(ch) is False
    assert server.lives == 6
    assert server.shown == ["_"] * len("robot")


def test_start_game_sets_word(server):
    ok = server.start_game("Hello")
    assert ok is True
    assert server.word == "hello"                    # 소문자 정규화
    assert server.shown == ["_"] * len("hello")      # shown 초기화
    assert server.lives == 6                          # lives 초기화


def test_start_game_rejects_non_alpha(server):
    ok = server.start_game("ab1c")
    assert ok is False
    # 상태는 그대로 (fixture 초기값 유지)
    assert server.word == "robot"
    assert server.lives == 6


def test_reset_after_lose(server):
    # lives를 모두 소진시킨다 (6번 틀림 -> lives 0)
    for letter in "xyzwqv":
        server.apply_guess(letter)
    assert server.lives == 0
    # 게임 종료 후 다시 추측하면 새 게임이 시작된다 (옵션 A: 추측은 버림)
    server.apply_guess("a")
    assert server.lives == 6                       # 초기화됨
    assert server.word == "apple"                  # 다음 단어
    assert server.shown == ["_"] * len("apple")    # 추측은 버려짐
