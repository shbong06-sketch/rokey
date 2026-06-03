# option.py
from tkinter import Tk
from tkinter import StringVar
from tkinter import OptionMenu

# 1. 위젯 생성
otk = Tk()
otk.geometry('400x300')

options_list = ['Option1', 'Option2', 'Option3']

selected_option = StringVar()
selected_option.set(options_list[0])
# sel_option = selected_option.get()
# print(sel_option)

def get_menu(value):
    sel_option = selected_option.get()
    print(sel_option)

# * 역할 : 컨테이너 자료 => 개별 인자로 분배(언패킹)
# - 컨테이너 자료: list, tuple, dict, set

# 매개변수 => 부모 인스턴스, 선택 시 저장할 옵션, 선택할 메뉴
option_menu = OptionMenu(otk, 
                         selected_option, *options_list, command=get_menu)
# option_menu = OptionMenu(otk, selected_option, options_list[0], options_list[1], options_list[2])

option_menu.pack()

otk.mainloop()