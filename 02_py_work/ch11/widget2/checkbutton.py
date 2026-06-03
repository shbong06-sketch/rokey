# checkbutton.py

from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar

# 1. 위젯 생성
otk = Tk()
otk.geometry('300x200')

coffee = {0: '아메리카노', 1: '라떼', 2: '카푸치노', 3: '에스프레소'}
check_value = {}

# check_value1 = BooleanVar()
# check_value2 = BooleanVar()
# check_value3 = BooleanVar()
# check_value4 = BooleanVar()
for i in range(len(coffee)):
    check_value[i] = BooleanVar()

# check_value1.set(True)
# val = check_value1.get()

# ocheckbutton1 = Checkbutton(otk, text=coffee[0], variable=check_value[0])
# ocheckbutton2 = Checkbutton(otk, text=coffee[1], variable=check_value[1])
# ocheckbutton3 = Checkbutton(otk, text=coffee[2], variable=check_value[2])
# ocheckbutton4 = Checkbutton(otk, text=coffee[3], variable=check_value[3])
for i in range(len(coffee)):
    ocheckbutton = Checkbutton(otk, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack()

# 기능: 선택된 체크버튼의 값을 변수로 가져와 출력
def buy():
    print("다음 메뉴를 주문합니다:")
    for i in range(len(coffee)):
        if check_value[i].get():
            print(coffee[i])

    # val1 = check_value1.get()     # 불리언값 접근 
    # val2 = check_value2.get()     # 불리언값 접근
    # if val1 == True:
    #     print(coffee[0])
    # if val2 == True:
    #     print(coffee[1])

obtn1 = Button(otk, text = "주문" , command = buy)


# 2. 위젯 배치
# ocheckbutton1.pack()
# ocheckbutton2.pack()
# ocheckbutton3.pack()
# ocheckbutton4.pack()
obtn1.pack()


otk.mainloop()
