# hw12_2.py

path = r'ch12\hw12\pizza_file1.txt'
with open(path, "r", encoding='utf-8') as file:
    pizza_lines = file.readlines()
    list = []
    for pizza_line in pizza_lines:
        list = pizza_line.split()
        print(list[0], list[1])

print("-----------------------")
with open(path, "r", encoding='utf-8') as file:
    pizza_lines = file.readlines()
    pizza_list = []
    for pizza_line in pizza_lines:
        linelist = pizza_line.split()
        pizza_list.append(linelist[0].strip())
print(pizza_list)