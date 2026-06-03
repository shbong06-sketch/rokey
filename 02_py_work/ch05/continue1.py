# continue1.py

count = 0
while count < 3 :
    count += 1
    if count == 2 :
        continue
    print(count)
print("반복문이 종료되었습니다.")

print("-----------------------------")
# 필터링 예제
users = ['admin', 'guest', '', None, 'user1']

for user in users :
    if not user:
        continue
    print(user)

# ""(빈 값) / None => 건너뜀
# 유효한 데이터만 처리

