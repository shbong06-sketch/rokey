# box_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset("iris")

# 3. 그래프 표시
sns.boxplot(data=iris,
             x= 'species',
             y= 'sepal_length')

plt.title("Box Plot Example")
plt.show()