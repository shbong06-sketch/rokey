# hw12_1.py

path = r'ch12\hw12\pizza_file1.txt'
# with open(path, "w", encoding='utf-8') as file:
#     file.write("페퍼로니피자 3000\n")
#     file.write("치즈피자 3200\n")
#     file.write("콤비네이션피자 3500\n")

# with open(path, "a", encoding='utf-8') as file:
#     file.write("불고기피자 3600\n")
#     file.write("해산물피자 3800\n")

print("----------------------")
# 답안 내용 참고 수정
pizza_menu = {
    '페퍼로니피자': 3000,
    '치즈피자': 3200,
    '콤비네이션피자': 3500
}

f = open(path, 'w', encoding='utf-8')
for key, value in pizza_menu.items():
    f.write(f"{key} {value}\n")
f.close()

pizza_menu_add = {
    '불고기피자': 3600,
    '해산물피자': 3800,
}

f = open(path, 'a', encoding='utf-8')
for key, value in pizza_menu_add.items():
    f.write(f"{key} {value}\n")
f.close()