# file_readlines.py
# 파일객체명.readlines()

f = open(r'ch12\file1.txt', 'r')
# f = open(r'ch12\file1.txt', 'r', encoding='utf-8')

lines = f.readlines()
# print(type(lines))  # list

for line in lines:
    print(line, end='')

f.close()