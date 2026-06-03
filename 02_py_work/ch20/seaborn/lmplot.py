# lmplot.py
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset("iris")

# 3. 그래프 표시
sns.lmplot(data=iris,
           x= 'sepal_length',
           y= 'sepal_width',
           hue='species',
           height=6)    # 그래프 자체 높이(단위: inch)

plt.title("Linear Model Plot Example")
plt.show()

# 선 옆에 있는 반투명 음영:
# 회귀선의 신뢰구간(Confidence Interval, CI)