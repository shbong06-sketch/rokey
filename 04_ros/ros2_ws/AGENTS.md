# AGENTS.md

## 운영 원칙

1. **작업 전 확인**: 파일 생성, 삭제, 수정 등 주요 작업을 수행하기 전에 반드시 사용자에게 확인을 받는다.
2. **ROS 학습 가이드**: 사용자는 ROS 엔지니어가 되기 위해 학습 중이다. ROS를 쉽고 제대로 익힐 수 있도록 대화형으로 안내한다.
3. **이론 학습**: 이론 관련 내용은 문제를 하나씩 내서 대화형으로 제시한다.
4. **코드 변경 승인**: 개발 과정에서 주요 코드를 직접 적용하지 않고, 사용자의 승인을 받은 후 적용한다.

## 워크스페이스 구조

ROS 2 colcon 워크스페이스. 패키지는 `src/` 안에 위치하며, `build/`, `install/`, `log/`는 빌드 시 생성되는 출력물이다.

### 패키지

- **my_interfaces** (`src/my_interfaces/`) — `ament_cmake` 패키지. `CMakeLists.txt`에서 `rosidl_generate_interfaces`를 사용하여 커스텀 서비스 인터페이스(`AddTwoInts.srv`, `Multiply.srv`)를 정의한다. `my_first_pkg`가 이 패키지에 의존하므로 먼저 빌드해야 한다.
- **my_first_pkg** (`src/my_first_pkg/`) — `ament_python` 패키지. `std_msgs`와 `my_interfaces`를 사용하는 rclpy 노드(pub/sub, service server/client)를 포함한다.

## 빌드

워크스페이스 루트(`/home/shbong/ros2_ws`)에서:

```bash
colcon build                          # 전체 패키지 빌드
colcon build --packages-select my_interfaces   # 인터페이스 먼저 빌드
colcon build --packages-select my_first_pkg    # 그 다음 Python 패키지 빌드
```

**빌드 순서 중요**: Python 패키지가 생성된 메시지/서비스 타입을 import하므로 `my_interfaces`를 먼저 빌드해야 한다.

빌드 후 오버레이 소스:

```bash
source install/setup.bash
```

## 린트 / 테스트

```bash
colcon test
colcon test-result --verbose
```

패키지별 린트:
- `my_first_pkg`: `ament_flake8`, `ament_pep257`, `ament_copyright` 실행 (`test/` 내 pytest)
- `my_interfaces`: `ament_lint_auto` 실행 (cpplint와 copyright 검사는 현재 CMakeLists.txt에서 스킵됨)

## 노드 (console_scripts)

모든 진입점은 `src/my_first_pkg/setup.py`의 `console_scripts`에 등록되어 있다. 실행: `ros2 run my_first_pkg <이름>`

| 스크립트 | 타입 | 토픽/서비스 |
|---|---|---|
| `talker` | 퍼블리셔 | `chatter` (String) |
| `listener` | 서브스크라이버 | `chatter` (String) |
| `battery_pub` | 퍼블리셔 | `battery` (Int32, 2초 간격) |
| `battery_sub` | 서브스크라이버 | `battery` (Int32) |
| `speed_pub` | 퍼블리셔 | `speed` (Float32, 0.5초 간격) |
| `add_server` | 서비스 서버 | `add_two_ints` (AddTwoInts) |
| `add_client` | 서비스 클라이언트 | `add_two_ints` (AddTwoInts) |
| `mul_server` | 서비스 서버 | multiply (Multiply) |

## 코딩 규칙

- 노드 패턴: `rclpy.node.Node`를 서브클래싱하고, `super().__init__('node_name')`을 호출하며, `__init__`에서 퍼블리셔/서브스크라이버/서비스를 정의한다. `main()` 함수에서 `rclpy.init()` / `rclpy.spin()` / `rclpy.shutdown()`을 사용한다.
- 코드 주석은 한국어로 작성한다.
- 런치 파일은 아직 존재하지 않는다.
