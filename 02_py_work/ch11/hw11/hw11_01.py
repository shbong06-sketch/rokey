# hw11_01.py

# 5.
# tkinter 모듈의 클래스인 Tk 클래스를 사용하여 윈도우 객체를 생성하는 코드를 작성하시오.
# 6.
# 앞서 생성한 윈도우 객체의 크기를 400x300으로 설정하고,
# 제목을 “조각 피자 주문 프로그램”으로 작성하시오.
# 7. 앞서 생성한 윈도우 객체에 “피자” 레이블을 추가하시오.
# 8. 앞서 생성한 윈도우 객체에 다음과 같이 피자 메뉴를 체크박스와 함께 추가하시오.

from tkinter import Tk
from tkinter import Label
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import Button

# 윈도우 위젯 생성
oroot = Tk(className="조각 피자 주문 프로그램")
oroot.geometry("400x300")

# 라벨 위젯 생성/배치
olabel = Label(oroot, text="피자")
olabel.pack()

# 피자 종류 및 가격 딕셔너리
pizza = {0: "치즈피자", 1: "콤비네이션피자", 2: "불고기피자"}
pizza_price = {0: 3200, 1: 3500, 2: 3600}

# 체크 버튼 클릭 동작을 위한 불리언 변수 설정
check_val = {}
for i in range(len(pizza)):
    check_val[i] = BooleanVar()

# 체크 버튼 생성/배치 반복문
for i in range(len(pizza)):
    ocheckbotton = Checkbutton(oroot, text=pizza[i]+"("+str(pizza_price[i])+"원)", variable=check_val[i])
    ocheckbotton.pack()

# 기능1: 주문 내역 가져오기
# 기능2: 총 가격 계산
def order():
    olabel1 = Label(oroot, text="주문내역:")
    olabel1.pack()
    total = 0
    for i in range(len(pizza)):
        if check_val[i]:
            order_label = Label(oroot, text=pizza[i]+"("+str(pizza_price[i])+"원)")
            order_label.pack()
            total += pizza_price[i]
    total_label = Label(oroot, text="\n총 가격: "+str(total)+"원")
    total_label.pack()

# 주문 버튼 생성/배치
obutton = Button(oroot, text="주문", command=order)
obutton.pack()

oroot.mainloop()

