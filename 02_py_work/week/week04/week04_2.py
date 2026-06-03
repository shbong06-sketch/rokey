# week04_2.py

while True:
    try: 
        num = float(input("숫자를 입력하세요 :"))
        print(f"입력한 숫자의 제곱: {num**2}")
        break
    except ValueError:
        print("올바른 숫자를 입력하세요!")

print("-------------------")
numbers = [10, 20, 30, 40, 50]
f = map(lambda x: x**2, numbers)

for i in numbers:
    print(next(f), end=' ')

print("2번 답안 내용 정리------")
numbers = [10, 20, 30, 40, 50]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"제곱된 리스트: {squared_numbers}")