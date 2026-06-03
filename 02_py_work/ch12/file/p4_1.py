# p4_1.py

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
order_list = []
while True:
    pizza_order = input("주문하실 메뉴를 입력하세요.(주문을 마치려면 enter를 누르세요.)\n:")
    if pizza_order == '':
        break
    order_list.append(pizza_order)


# 주문 내역은 order.txt 파일로 저장
for i in order_list:
    file.write(i+'\n')

file.seek(0)
order_menu = file.readlines()
# 주문 항목의 딕셔너리 만들기
order_dict = {}
# 주문 내역의 메뉴 리스트에서 딕셔너리에 있는 메뉴 찾기+숫자 세기
for name in order_menu:
    name = name.strip()
    if name in order_dict:
        order_dict[name] += 1
    else :
        order_dict[name] = 1

print("주문 내역:")
for order in order_dict:
    price = menu[name]
    count = order_dict[name]
    total = price*count

    print(f"- {order} ({price}원) x {count} {total}원")
# # 다음과 같이 주문 내역 쓰기
# # 주문 내역:
# #  - 치즈피자 (3200원) x 3 9600원

file.close()
# 주문 내역 읽어 화면에 출력하기