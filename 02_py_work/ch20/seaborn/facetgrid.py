# facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
# 다양한 상황에서 식사금액과 팁의 관계
# total_bil, tip, sex, smoker, day, time, size

tips = sns.load_dataset("tips")
# print(tips)

# 2. 기본 스타일 설정
sns.set_theme(style='dark',
              palette='pastel')

# 3. 그래프 표시
g = sns.FacetGrid(tips,
                  col='sex',
                  row='time',
                  height=3.5,
                  aspect=0.95)
g.map_dataframe(sns.scatterplot,
                x = 'total_bill',
                y = 'tip')

# 기본 제목에서 값만 표시하도록 설정
# {row_name} : 행 변수값
# {col_name} : 열 변수값
g.set_titles(row_template='{row_name}',
             col_template='{col_name}')
g.fig.suptitle("Pair Plot Example", y=1.003)

plt.show()
