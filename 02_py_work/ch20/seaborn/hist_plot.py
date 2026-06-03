# hist_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset("iris")

# 2. 기본 스타일 설정
sns.set_theme(style='darkgrid',
              palette='muted')

# 3. 그래프 표시
sns.histplot(data=iris,
           x= 'sepal_length',
        #    y= 'petal_length',   # 2차원 히스토그램으로 표시 ; 적지 않으면 count가 들어감.
           hue='species',
           kde=True)    # 분포 곡선

plt.title("Histogram Example")
plt.show()