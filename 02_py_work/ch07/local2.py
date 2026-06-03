# local2.py

b = 0   # 전역변수 선언(초기화)
print("b의 값은", b)
b = 1   # 전역변수 재할당
print("b의 값은", b)

def scope_test() :
    global a    # 지역 => 전역 사용하겠다는 선언
                # 변수 생성 선언은 아님
    a = 1       # 전역변수(재할당)
    # c = 0     # 지역 변수 선언
    print("scope_test() 함수 안의 a 값은", a)

a = 0   # 전역변수 선언(초기화)
print("scope_test() 함수 밖의 a 값은", a)
scope_test()

print("scope_test() 함수 호출 후 a 값은", a)

# 실무 관점
# global 가능하면 안 쓰는 게 좋음
# 이유
# 디버깅 어려움
# 사이드 이펙트 : 함수의 결과 외에 '외부의 상태'를 변경하는 것.
# 함수의 재사용성이 떨어짐.
def increment() :
    global count
    count += 1

# def increment(count) :
#     return count + 1

increment()
increment()
print(count)    # 2

print("-------------------------")
count = 100
increment()
print(count)
# 의도치 않게 기존 값이 바뀜.

print("-------------------------")
def process():
    increment()     # 내부에서 count 값을 변경.
process()           # process() 함수만 봐서는 count가 바뀌는 것을 알 수 없다.

