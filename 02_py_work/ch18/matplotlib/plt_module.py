# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
# plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["font.family"] = "NanumGothic"

# 선 그래프
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x, y)
# # plt.title("Line Plot")
# plt.title("선 그래프")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

print("------------------------")
# 막대 그래프
# categories = ["A", "B", "C", "D"]
# values = [3, 7, 8, 5]
# plt.bar(categories, values)
# plt.title("막대 그래프")
# plt.show()

print("------------------------")
# Histogram => 연속 데이터
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# # plt.hist(data)    # bins 디폴트값 = 10
# plt.hist(data, bins=4, color='skyblue', edgecolor='black')
# plt.title("히스토그램")
# plt.show()

print("------------------------")
# 산점도(Scatter Plot)
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
# plt.scatter(x,y, color='green')
# plt.title("Scatter Plot")
# plt.show()

print("------------------------")
# Pie Chart
# sizes = [15, 30, 45, 10]
# labels = ['Group A', 'Group B', 'Group C', 'Group D']
# # plt.pie(sizes, labels=labels)
# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, counterclock=False)
# plt.title("Pie Chart")
# plt.show()

# % 포멧 시작
# 1 전체 최소 자릿수
# .1 소수점 자릿수
# f 실수(float) 형식
# %% 실제% 문자 출력

print("------------------------")
# Box Plot
# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8, 50]   # 50: 이상치 -> 한번 더 체크하는 용도로 활용 가능
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# 이상치(outlier): 대부분의 데이터 패턴에서 크게 벗어난 값
# 이상치 생성 이유: 측정 오류, 데이터 처리 오류, 실제 특이한 사건
# 이상치 발생시 처리 방법
# 1. 제거(삭제)
# 입력/측정/데이터 수집 오류
# 2. 값 수정(대체)
# 평균값, 중앙값, 치환값 등으로 바꾸는 방법
# 3. 윈저라이징
# 극단값을 최대/최소 범위 값으로 바꾸는 방법
# 4. 로그 변환(데이터 변환)
# 데이터 분포를 줄이는 방법
# 5. 그대로 사용
# 이상치가 실제 의미 있는 데이터라면 그대로 사용

# print("------------------------")
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# # plt.plot(x, y, color='red', linestyle='--', marker='o')
# # plt.plot(x, y, color='blue', linestyle='-', marker='^') # ^ : 삼각형
# plt.plot(x,y,'k^:')     # 축약형(색상, 마커, 라인스타일)
# plt.show()

# color
# 'r' : red
# 'g' : green
# 'b' : blue
# 'k' : black
# 'y' : yellow
# 'm' : magenta
# 'c' : cyan
# linestyle: '-' '--' ':' '-.' ...
# marker: '.' ',' 'o' '^' 'v' ...

print("------------------------")
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x,y,'k^:')
# plt.xlim(0,5)
# plt.ylim(0,40)
# plt.xticks(range(1, 5))
# plt.yticks(range(0, 41, 10))
# plt.show()

print("------------------------")
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# x1 = [1, 2, 3, 4]
# y1 = [2, 5, 9, 7]
# plt.plot(x, y, "k^-.", label="Data 1")
# plt.plot(x1, y1, color="m", label="Data 2")
# plt.legend(loc='upper left')
# plt.savefig(r"ch18\matplotlib\my_plot.png")
# plt.show()

print("------------------------")
# Subplot 응용
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 8, 5]
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# fig : 전체 그래프창
# axs : 각 subplot(그래프 영역)
fig, axs = plt.subplots(2,2)
axs[0,0].plot(x, y)
axs[0,1].bar(categories, values)
axs[1,0].scatter(x, y)
axs[1,1].hist(data)
fig.suptitle("전체 그래프 제목")
plt.tight_layout()
plt.show()