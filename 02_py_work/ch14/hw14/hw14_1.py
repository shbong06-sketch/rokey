# hw14_1.py

# 6.
text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"

import re
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern, text)
print(emails)

print("----------------------")
# 7.
text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"

import re
p = r"\d{2,3}-\d{3,4}-\d{4}"
numbers = re.findall(p, text)
print(numbers)

print("-------------------------")
# 8.
text = "I love Python. Java is also popular. Python is great for AI."

import re
# p = "[\w\s]*Python[\w\s]*\."
p = "[^.]*Python[^.]*\."
py_texts = re.findall(p, text)
print(py_texts)

print("-------------------------")
# 9.
text = "상품 코드: A123, B456, C789, 가격: 12000원"

import re
p = "\d+"
nums = re.findall(p, text)
print(nums)

print("-------------------------")
# 10.
text = "NASA is working on AI projects with IBM and Google."

import re
p = "[A-Z]{2,}"
caps = re.findall(p, text)
print(caps)