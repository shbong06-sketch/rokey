# facetgrid2.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset("iris")
# 2. 기본 스타일 설정
sns.set_theme(style='darkgrid', palette='colorblind')
# 3. 그래프 표시
g = sns.FacetGrid(iris,
                  col= 'species',
                  height=3,
                  aspect=1.2)
g.map_dataframe(sns.histplot, x='sepal_length', kde=True)
g.set_titles(row_template='{row_name}',
             col_template='{col_name}')
plt.show()