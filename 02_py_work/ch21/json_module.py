# json_module.py

import json
# JSON 문자열을 파이썬 객체로 변환
json_string = '{"name": "Alice", "age": 25, "city":"Seoul"}'

data = json.loads(json_string)
print(data['name'])

# 파이썬 객체를 JSON 문자열로 변환
python_dict = {"name": "Bob", "age": 30, "city":"Busan"}
json_output = json.dumps(python_dict, indent=4)
print(json_output)

# JSON 파일 저장
# with open("data.json", 'w') as file:
#     json.dump(python_dict, file, indent=4)

# JSON 파일 불러오기
with open("data.json", 'r') as file:
    loaded_data = json.load(file)
print(loaded_data)