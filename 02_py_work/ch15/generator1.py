# generator1.py
# 제너레이터 생성방법 1. yield 사용
def mygen():
    for i in range(1,100):
        result = i * i
        yield result

gen = mygen()
print(next(gen))    # yield는 next당 한번씩 실행
print(next(gen))
print("줄번호: ", gen.gi_frame.f_lineno)    # 현재 멈춘 줄번호(코드 내에서 어느 위치의 yield에서 멈추었는지 확인 가능)
print(next(gen))

# for item in gen:x``
#     print(item)

# print(next(gen))    # StopIteration

