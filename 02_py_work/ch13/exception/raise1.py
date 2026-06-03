# raise1.py
# raise 예외클래스명(예외 정보 데이터)
print("raise")
# 예외 발생시키기
# raise NameError('Hi there')  # 프로그램 중단

try:
    raise NameError('Hi there')  # 프로그램 중단
except NameError as e:
    print('An exception flew by!')
    print('e: ', e)

print("exit")

# 사용 이유/목적
# - 잘못된 값 들어왔을 때 방지
# - 함수에서 조건을 위반 시 실행 중단
# - 사용자 정의 에러 처리

# 사용 예 - 은행 잔고 부족 시 에러 발생
class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            try:
                raise InsufficientBalanceError('잔고가 부족합니다.')
            except InsufficientBalanceError as e:
                print("잔고를 확인하세요.")
                print(e)
        self.balance -= amount
        return self.balance

kim = Account(1000)
kim.withdraw(2000)