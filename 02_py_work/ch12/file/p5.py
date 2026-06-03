# p5.py

# 주문 내역 파일
path = r'.\ch12\file\order.txt'
file = open(path, 'a', encoding='utf-8')

# 터미널을 통해 주문 입력: input()
drink_order = input("주문 내역:\n")
# 다음과 같이 주문 내역 쓰기
# 주문 내역:
#  - 치즈피자 (3200원) x 3 9600원
#  - 치즈피자 (1500원) x 2 3000원

# 주문 내역은 order.txt 파일로 저장
file.write(drink_order+'\n')

file.close()

file = open(path, 'r', encoding='utf-8')
order = file.readlines()

print("주문 내역:")
for i in range(len(order)):
    for j in order[i].strip():
        print(j, end='')
    print()

# 주문 내역 읽어 화면에 출력하기