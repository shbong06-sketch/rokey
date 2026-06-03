# week03.py

# 8-1.
def list_max(num_list):
	max = num_list[0]
	for num in num_list:
		if num > max:
			max = num
	print(max)
		
list_max([1, 12, 5, 6, 3])

print("----------------------")
# 8-2 리스트 최솟값
numbers = [42, 17, 23, 56, 9, 34]

def list_min(numbers):
	min = numbers[0]
	for num in numbers:
		if num < min:
			min = num
	return min

print(list_min(numbers))

print("----------------------")
# 10-1. math 모듈에서 factorial 함수를 가져와 숫자 5의 팩토리얼을 구하는 프로그램을 작성하시오.

from math import factorial

num = factorial(5)
print(num)

print("----------------------")
# 10-2. 아래의 클래스를 상속받는 Dog 클래스를 생성하고
# speak 메서드를 오버라이딩하여
# Dog 클래스의 인스턴스가 “Woof!” 를 반환하도록 프로그램을 작성하시오.

class Animal:
	def speak(self):
		return 'Animal speaks'

class Dog(Animal):
	def speak(self):
		return "Woof!"
	
dog = Dog()
print(dog.speak())

print("----------------------")
import tkinter as tk
from tkinter import messagebox

def on_buton_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")
	

root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text="클릭하세요", command=on_buton_click)
btn.pack(pady=20)

root.mainloop()