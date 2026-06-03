# p1.py

import re
# p42.
text = "My phone number is 123-456-7890"

numbers = re.findall("\d+", text)
print(numbers)

print("------------------------")
# p.43

text = "Contact us at support@example.com or sales@example.org."

p = re.compile("[\w.-]+@[\w.-]+\.\w+")
emails = p.finditer(text)
for m in emails:
    print(m.group(), end=', ')

print("\n----------------------")
# p.44
phone = "123-456-7890"

p = re.compile("^\d{3}-\d{3}-\d{4}$")
if p.match(phone):
    print("적절하게 사용")
else:
    print("잘못 사용")