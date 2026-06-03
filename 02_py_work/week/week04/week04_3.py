# week04_3.py

data = """python one
life is too short
python two
you need python
python three"""

import re
p = re.compile("^python\s\w+", re.M)
matches = p.findall(data)
print("Python으로 시작하는 문장들: ")
for match in matches:
    print(match)

print("--------------------")
email_pattern = "^[\w.+\-]+\@[\w.\-]+\.\w{2,}$"
email_add = input("이메일 주소를 입력하세요 :")
email_form = re.compile(email_pattern)
email_veri = email_form.match(email_add)
try :
    print("올바른 이메일 형식입니다.\n", email_veri.group())
except AttributeError:
    print("잘못된 이메일 형식입니다.")

if re.match(email_pattern, email_add):
    print(f"올바른 이메일 형식입니다.: {email_add}")
else:
    print("올바른 이메일 형식이 아닙니다.")