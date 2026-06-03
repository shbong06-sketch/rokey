# pair_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset("iris")

# 3. 그래프 표시
g = sns.pairplot(iris,
             hue='species')
g.fig.suptitle("Pair Plot Example", y=1.001)
plt.show()