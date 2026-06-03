# week04_1.py

with open("data.txt", 'w', encoding='utf-8') as file:
    for i in range(1, 11):
        file.write(f"{i}번째 줄입니다.\n")

print("파일이 성공적으로 작성되었습니다.")

f = open("data.txt", 'a', encoding='utf-8')
f.write('11번째 줄입니다.\n')
f.close()
print("파일 추가가 완료 되었습니다.")

with open("data.txt", 'r', encoding='utf-8') as file:
    contents = file.read()

print("파일 내용:")
print(contents)


