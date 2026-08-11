# Mission Stack — 미션 큐 기반 로봇 운행 시스템

> "어디로 갈지는 DB가 정하고, 어떻게 가는지는 로봇이 안다."

하이브리드 방식의 로봇 미션 시스템입니다.
DB에 **"어디로"(미션)** 만 쌓으면, 워커 노드가 이를 꺼내
ROS2 서비스를 호출해 실제 로봇을 움직입니다.

```
┌──────────┐      ┌────────────────────┐      ┌───────────────────────────┐
│  누군가   │      │   PostgreSQL 16    │      │   ros_worker (컨테이너)    │
│ 미션 입력 │─────▶│ missions 테이블(큐) │─────▶│  mission_worker_pkg        │
└──────────┘      └────────────────────┘      │  (ROS2 Jazzy)              │
                                              └─────────────┬─────────────┘
                                                            │
                                              ┌─────────────▼─────────────┐
                                              │  dsr_msgs2 서비스           │
                                              │  /dsr01/dsr_controller2     │
                                              │  set_robot_mode, move_joint │
                                              └─────────────┬─────────────┘
                                                            │
                                                        실제 로봇
```

## 구성 요소

| 경로 | 역할 |
|---|---|
| `compose.yaml` | `db`(PostgreSQL 16) + `ros_worker`(ROS2 워커) 두 서비스 정의 |
| `Dockerfile` | ROS Jazzy 이미지에 `dsr_msgs2`를 colcon 빌드하고 워커 실행 |
| `.env` / `.env.example` | DB 접속 정보 (시크릿은 코드가 아닌 환경변수에서) |
| `db/init.sql` | `missions` 테이블 스키마와 샘플 데이터 |
| `src/mission_worker_pkg/` | ROS2 패키지 버전 워커 — `.env` 기반, 컨테이너에서 실행 |
| `worker/mission_worker.py` | 스탠드얼론 실행용 단순 워커 — DB 접속 정보가 하드코딩 |
| `src/doosan-robot2/` | 두산 로봇 인터페이스 패키지 — git **서브모듈** (`dsr_msgs2` 포함, `jazzy` 고정) |

## 실행 방식 두 가지

- **Docker (권장)**: `docker compose up` — DB가 healthy 해진 뒤
  `ros_worker`가 `dsr_msgs2`를 빌드하고 미션 큐를 감시합니다.
- **호스트**: `python3 worker/mission_worker.py` — 로봇 소프트웨어가
  이미 떠 있는 호스트에서 빠르게 확인할 때 사용합니다.

## 미션 라이프사이클

```
대기 ──▶ 진행 ──▶ 완료
  │              실패(목적지 불명 / 모션 오류)
```

- **우선순위**: `priority`(1~9) 숫자가 작을수록 먼저 처리
- **이중 처리 방지**: `UPDATE ... WHERE status='대기'` + `rowcount` 체크로
  여러 워커가 돌아도 같은 미션은 한 번만 집힘
- **실패 처리**: 모르는 목적지면 움직이지 않고 즉시 `실패` 처리

## 목적지 ↔ 관절 자세

DB는 "목적지 이름"만 알고, 실제 관절 자세는 워커가 압니다.

| 목적지 | 관절 자세(도) |
|---|---|
| 대기장소 | `[0, 0, 0, 0, 0, 0]` |
| 선반A | `[0, 0, 90, 0, 90, 0]` |
| 선반B | `[30, 0, 90, 0, 90, 0]` |
| 충전독 | `[-30, 30, 60, 0, 90, 0]` |

## 실행 방법

### 1. 환경 변수 준비

```bash
cp .env.example .env   # DB_NAME, DB_USER, DB_PASSWORD 등을 채운다
```

| 변수 | 설명 |
|---|---|
| `DB_HOST` | compose 안에서는 `db`(서비스명)로 자동 주입 |
| `DB_PORT` | 기본 `5432` |
| `DB_NAME` / `DB_USER` / `DB_PASSWORD` | PostgreSQL 접속 정보 |

### 0. 서브모듈 포함 클론 (처음 한 번)

```bash
git clone --recurse-submodules <저장소>   # src/doosan-robot2 서브모듈 포함
```

이미 클론했을 때는:

```bash
git submodule update --init
# 최신으로 올리려면: git submodule update --remote
```

### 2. Docker로 전체 스택 실행

```bash
docker compose up --build
```

`ros_worker`가 실제 로봇과 통신하려면 두산 로봇 컨트롤러 노드가
서비스 경로 `/dsr01/dsr_controller2`에 떠 있어야 합니다.

### 3. 미션 넣기

```bash
psql -h localhost -U postgres -d robotdb
#   INSERT INTO missions (kind, target, priority) VALUES ('이동', '선반A', 1);
```

### 호스트에서 워커만 돌리기 (확인용)

```bash
python3 worker/mission_worker.py
```

## 요구 사항

- Docker / Docker Compose (컨테이너 실행 시)
- 두산 로봇 컨트롤러 + ROS2 (`dsr_controller2` 노드)
- 호스트 실행 시: ROS2 Jazzy, `dsr_msgs2`, `psycopg2`, `rclpy`, `python-dotenv`

---