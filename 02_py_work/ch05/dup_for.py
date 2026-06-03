# dup_for.py

# for 변수 in 리스트 :
#     코드블록
#     for 변수 in 리스트:
#         코드블록

# print("*", end = "")
# for i in range(10) :
#     print("*", end = "")
# print()

# j: 0 1 2 3 4
# i: 0 1 2 3 4 5 6 7 8 9

for i in range(5) :             # 0 ~ 4
    for j in range(10) :        # 0 ~ 9
        print("*", end = "")
    print()

print("---------------------")

# for i in range(5): 
#     for k in range(5-i):
#         print(" ", end = "")
#     for j in range(i+1) :
#         print("*", end = "")
#     print()
