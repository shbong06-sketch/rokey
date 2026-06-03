# file_read.py
# 파일객체명.read()

f = open(r'ch12\file1.txt', 'r')
# f = open(r'ch12\file1.txt', 'r', encoding='utf-8')

data = f.read()
# print(type(data))  # str
print(data)

f.close()