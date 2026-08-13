# Rokey 부트캠프

> **"기초 이론부터 실무 프로젝트까지 기록"** > 본 저장소는 로봇 제어 및 데이터 분석 능력, AI 모델을 마스터하기 위해 공부한 파이썬, 비전 AI, ROS 등의 학습 내용과 프로젝트 소스코드를 체계적으로 정리하는 공간입니다.

---

## 📅 학습 로드맵 및 폴더 구조 (Directory Structure)

※ 교육 과정의 흐름에 따라 번호 순으로 정렬되어 있으며, 개인 프로젝트와 일일 기록(TIL)은 독립된 폴더로 관리합니다.

```text
rokey/
├── README.md                      <-- 현재 대문 문서
├── TIL/                           <-- 매일 공부한 핵심 요약 및 트러블슈팅
│   ├── Development_env/    # 개발 환경 구축 (SSH, conda, GPU 등)
│   ├── git_study/          # Git/GitHub 학습 기록
│   └── gazebo_study/       # Gazebo(ROS2) 학습 기록
│
├── Project_AI_basic/       # 개인 프로젝트: AI 기초 (Kaggle 경진대회)
│
├── 02_py_work/             # 파이썬 기본 문법, 라이브 코딩 및 과제 (ch01~ch21)
├── 03_vision_ai/           # 컴퓨터 비전 및 AI 관련 학습
│   ├── vision_ai_basic/    # AI 기초 (강의/과제/실습/보충수업)
│   └── vision_ai_applied/  # AI 응용 (강의/과제 — Transformer, ViT)
├── 04_ros/                 # ROS2 노드·통신·Gazebo 실습
│   ├── ros2_ws/            # ROS2 실습 워크스페이스 (URDF, Gazebo)
│   ├── demo_ros_prj/       # ROS2 미니 프로젝트
│   └── turtle_run1/2/      # turtle sim mcap 기록
└── 05_devops/              # 개발 협업 툴(DevOps) 환경 실습
    ├── mission_app/        # 미션 큐 기반 로봇 운행 시스템 (doosan-robot2 서브모듈)
    ├── robot_stack/        # Docker 기반 로봇 스택
    └── db_study/           # DB 학습 자료
```
