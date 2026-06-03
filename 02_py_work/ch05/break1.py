# break1.py

count = 0
while count < 3 :
    # count = count + 1
    count += 1
    if count == 2 :
        break
    print(count)
print("반복문이 종료되었습니다.")

for i in range(1, 4) :
    if i == 2 :
        break
    print(i)
print("반복문이 종료되었습니다.")

print("--------------------------")
# 원하는 값을 찾으면 종료하는 예제
users = ['kim', 'lee', 'park']

for user in users :
    if user == 'lee' :
        print('발견!')
        break

# 찾으면 탐색 중지 => 성능 절약

while True :
    cmd = input("프롬프트> ")
    if cmd == 'python3' :
        print("파이썬 프로그램 실행")
    elif cmd == 'exit' :
        print("터미널 종료")
        break