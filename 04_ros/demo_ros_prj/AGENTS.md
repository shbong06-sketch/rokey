# 공장 다중로봇 관제 시스템 - 프로젝트 가이드

## 개요
- ROS2 Jazzy를 사용한 공장 다중로봇 관제 시스템 데모 프로젝트
- 단순한 구조로 개발, 단계별 승인 후 진행
- 최종 목표: 10대 AMR 동시 관제 (초기 데모: 1대)

## 기술 스택
- **ROS2 버전**: Jazzy
- **프로그래밍 언어**: Python
- **DDS**: FastDDS (기본)
- **패키지 이름**: factory_robot_control

## 프로젝트 구조
```
demo_ros_prj/                         # ROS2 워크스페이스
├── src/                              # 소스 코드 디렉토리
│   └── factory_robot_control/        # ROS2 패키지
│       ├── factory_robot_control/    # Python 패키지
│       │   ├── __init__.py
│       │   ├── amr_node.py           # AMR 로봇 노드
│       │   ├── control_center_node.py # 관제 센터 노드
│       │   └── utils.py              # 유틸리티 함수
│       ├── launch/
│       │   ├── amr.launch.py         # AMR 노드 실행용
│       │   ├── control_center.launch.py # 관제 노드 실행용
│       │   └── demo.launch.py        # 데모 전체 실행용
│       ├── msg/
│       │   └── BatteryStatus.msg     # 배터리 상태 메시지
│       ├── srv/
│       │   └── ChargeCommand.srv     # 충전 명령 서비스
│       ├── CMakeLists.txt            # 빌드 설정
│       └── package.xml               # 패키지 정보
├── build/                            # 빌드 결과물
├── install/                          # 설치 결과물
└── log/                              # 빌드 로그
```

## 아키텍처

### 노드 구조
1. **AMR 노드** (amr_node.py)
   - 각 로봇별 고유 ID로 토픽 네임스페이스 구분
   - `/robot_{id}/battery` 토픽으로 배터리 상태 발행
   - 배터리 충전 서비스 서버 제공

2. **관제 센터 노드** (control_center_node.py)
   - 모든 AMR의 배터리 상태 구독
   - 배터리 잔량 15% 이하 확인 시 충전 명령 서비스 클라이언트 호출

### 통신 & 서비스 설계

#### 1. 토픽 (Topic)
- **토픽명**: `/robot_{id}/battery`
- **메시지 타입**: `factory_robot_control/msg/BatteryStatus`
- **주기**: 1초 간격 발행
- **QoS**: BEST_EFFORT, VOLATILE (최신 데이터만 유지)

#### 2. 메시지 정의 (msg/BatteryStatus.msg)
```
# 배터리 상태 메시지
float32 percentage    # 배터리 잔량 (0.0 ~ 100.0)
builtin_interfaces/Time timestamp  # 상태 보고 시간
```

#### 3. 서비스 정의 (srv/ChargeCommand.srv)
```
# 충전 명령 요청
string command        # 명령어: "START_CHARGE" 또는 "STOP_CHARGE"
---
# 충전 명령 응답
bool success          # 명령 성공 여부
string message        # 결과 메시지 (예: "충전 시작됨", "충전 중지됨")
```

#### 4. 서비스 (Service)
- **서비스명**: `/robot_{id}/charge_command`
- **서비스 타입**: `factory_robot_control/srv/ChargeCommand`
- **통신 방식**: Synchronous (동기)
- **설명**: 관제 센터에서 AMR에 충전 시작/중지 명령 전달

#### 5. 통신 흐름
```
[AMR Node]                              [관제 센터]
     |                                       |
     |--- /battery (1초 주기) ------------->|  (배터리 상태 발행)
     |                                       |
     |                                    배터리 15% 이하 확인
     |                                       |
     |<--- /charge_command (START_CHARGE) ---|  (충전 시작 명령)
     |                                       |
     |--- 응답 (success: true) ------------->|  (명령 수락)
     |                                       |
     | (배터리 100% 충전 후)                  |
     |--- /battery (100%) ----------------->|  (충전 완료 상태)
     |                                       |
     |<--- /charge_command (STOP_CHARGE) ----|  (충전 중지 명령)
     |--- 응답 (success: true) ------------->|
```

## 개발 규칙

### 코딩 컨벤션
- Python PEP 8 스타일 준수
- 변수/함수명: snake_case
- 클래스명: PascalCase
- ROS2 네이밍 컨벤션 준수

### 단계별 개발 순서
1. **1단계**: 기본 ROS2 패키지 구조 생성
2. **2단계**: 메시지/서비스 정의
3. **3단계**: 단일 AMR 노드 구현 (1대)
4. **4단계**: 관제 센터 노드 구현 (1대 관리)
5. **5단계**: 런치 파일 작성
6. **6단계**: 다중 로봇 확장 (최종 10대)

### 테스트 방법
```bash
# 패키지 빌드
colcon build --packages-select factory_robot_control

# 단일 AMR 테스트
ros2 run factory_robot_control amr_node --ros-args -p robot_id:=1

# 관제 센터 테스트
ros2 run factory_robot_control control_center_node

# 데모 실행
ros2 launch factory_robot_control demo.launch.py
```

## 주의사항
- 각 단계마다 구현 내용 확인 후 다음 단계 진행
- 복잡한 구조 피하고 단순하게 유지
- 기존 ROS2 패턴 및 라이브러리 활용
- 에러 처리 및 로깅 적절히 포함
