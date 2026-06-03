# toeic.py
# 토익 점수를 3분류 하는 프로그램
tscore = 700
# tscore = 400
# tscore = 990

print("당신의 토익 점수는", end=" ")
if tscore >= 900 :
    print("%d점으로 상위권입니다." %tscore)
elif tscore >= 700 :
    print("%d점으로 중위권입니다." %tscore)
else :
    print("%d점으로 하위권입니다." %tscore)
print("if 문 종료됨.")

print("-----------------")
# 토익점수를 4분류 하는 프로그램
# 900점 이상: 상위권
# 900미만~600이상 : 중상위권
# 600미만~300이상 : 중위권
# 300미만 : 하위권
# ts_score = 700
# ts_score = 400
# ts_score = 200
tscore = 990
grade = ["상위권", "중상위권", "중위권", "하위권"]

print("당신의 토익 점수는", end=" ")
if tscore >= 900 :
    print("%d점으로 %s입니다." %(tscore, grade[0]))
elif tscore >= 600 :
    print("%d점으로 %s입니다." %(tscore, grade[1]))
elif tscore >= 300 :
    print("%d점으로 %s입니다." %(tscore, grade[2]))
else :
    print("%d점으로 %s입니다." %(tscore, grade[3]))
print("if 문 종료됨.")

print("----------------")
# 990점 이하~900이상: 상위권

tscore = 990
grade = ["상위권", "중상위권", "중위권", "하위권"]

print("당신의 토익 점수는", end=" ")
# if tscore >= 900 and tscore <= 990 :
if 990 >= tscore >= 900 :
    print("%d점으로 %s입니다." %(tscore, grade[0]))
elif tscore >= 600 :
    print("%d점으로 %s입니다." %(tscore, grade[1]))
elif tscore >= 300 :
    print("%d점으로 %s입니다." %(tscore, grade[2]))
else :
    print("%d점으로 %s입니다." %(tscore, grade[3]))
print("if 문 종료됨.")