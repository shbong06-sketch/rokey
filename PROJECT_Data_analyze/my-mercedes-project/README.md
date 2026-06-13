# 🚗 Mercedes-Benz Greener Manufacturing (Kaggle)

메르세데스-벤츠 제조 공정 데이터(차량의 옵션 조합)를 활용하여 테스트 베치(Test Bench)에서의 소요 시간을 예측하는 머신러닝 프로젝트입니다. 효율적인 공정 스케줄링을 통해 탄소 배출을 줄이는 친환경 제조(Greener Manufacturing) 가치를 목표로 합니다.

## 📅 프로젝트 기간
- 2026.06 ~ 진행 중 (약 2주 소요 예상)

## 📂 폴더 및 파일 구조
이 프로젝트는 유지보수와 가독성을 위해 데이터 탐색(EDA), 전처리, 모델링 파이프라인을 독립된 주피터 노트북으로 분리하여 관리합니다.

```text
mercedes-benz-kaggle/
├── data/
│   ├── raw/                  # 캐글 원본 데이터 (train.csv, test.csv)
│   └── processed/            # 전처리 및 차원축소가 완료된 데이터
├── notebooks/
│   ├── 01_eda.ipynb          # 데이터 분포 확인 및 이상치 탐색
│   ├── 02_preprocessing.ipynb # 범주형 변수 인코딩 및 PCA/ICA 차원 축소
│   └── 03_modeling.ipynb     # LightGBM/XGBoost 모델 학습 및 교차 검증
├── models/                   # 학습이 완료된 가중치 파일 (.pkl 등)
├── submission/               # 캐글 최종 제출용 .csv 파일
└── README.md                 # 프로젝트 가이드라인
```

## 배운 점 및 회고
