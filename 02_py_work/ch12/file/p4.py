# p4.py

# 피자 메뉴와 가격
pizza_menu = {"페퍼로니 피자":3000, "치즈 피자":3200, "콤비네이션 피자": 3500, "불고기 피자": 3600, "해산물 피자": 3800}
drink_menu = {"콜라": 1500, "사이다": 1500, "생수":1000}
# 메뉴 통합
menu = {}
menu.update(pizza_menu)
menu.update(drink_menu)

# 주문 내역 파일
path = r'.\ch12\file\order.txt'
file = open(path, 'w+', encoding='utf-8')

# 터미널을 통해 주문 입력: input()
pizza_order = input("주문 내역:\n")
# 다음과 같이 주문 내역 쓰기
# 주문 내역:
#  - 치즈피자 (3200원) x 3 9600원

# 주문 내역은 order.txt 파일로 저장
file.write(pizza_order+'\n')

file.seek(0)
pizza = file.readline().split()
print("주문 내역:")
for i in pizza:
    print(i, end=' ')

file.close()
# 주문 내역 읽어 화면에 출력하기