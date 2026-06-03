# generator2.py
# 리스트 컴프리헨션 사용 예제
import time

def longtime_job():
    print("job start")
    time.sleep(1)   # 1초 지연
    return "done"

list_job = [longtime_job() for i in range(5)]   # 1초 간격으로 5번 함수 호출, 리턴값으로 리스트 생성
# print(list_job)
print(list_job[0])

print("__iter__" in dir(list_job))  # True => iterable
print("__next__" in dir(list_job))  # False => not iterator