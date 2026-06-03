# generator2_1.py
# 제너레이터 컴프리헨션 사용 예제

# 차이점
# 1. 실행 "타이밍"이 다름
# 2. 중간에 정지 가능

import time

def longtime_job():
    print("job start")
    time.sleep(1)   # 1초 지연
    return "done"

gen_job = (longtime_job() for i in range(5))
print(next(gen_job))    # next로 호출할 때마다 한번씩 작업 실행
# do_something_else()   # 추가적인 조건이나 함수를 넣어서 작업 중단시킬 수 있다.
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))    # StopIteration
# print(gen_job)            # generator object

print("__iter__" in dir(gen_job))  # True => iterable
print("__next__" in dir(gen_job))  # True => iterator