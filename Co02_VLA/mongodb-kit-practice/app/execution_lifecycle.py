from datetime import datetime, timezone
from pprint import pprint
from time import sleep
from uuid import uuid4

from database import (
    commands,
    component_executions,
    kit_executions,
)

# 실행 식별자 선언
KIT_EXECUTION_ID = "KIT-LIFECYCLE-001"
COMPONENT_EXECUTION_ID = str(uuid4())

# 시간 생성
def utc_now():
    return datetime.now(timezone.utc)


def reset_demo():
    """동일한 데모 실행 데이터만 제거한다."""
    condition = {
        "kit_execution_id": KIT_EXECUTION_ID,
    }

    commands.delete_many(condition)
    component_executions.delete_many(condition)
    kit_executions.delete_many(condition)

# 새 문서로 저장 -- 음성, 명령 검증 완료 대상 저장
def save_command():
    """음성 인식과 명령 검증 결과를 저장한다."""
    document = {
        "command_execution_id": str(uuid4()),
        "kit_execution_id": KIT_EXECUTION_ID,
        "scenario_id": "SCENARIO_01",
        "scenario_version": "v1",
        "stt_text": "정전 키트에 생수 한 개를 넣어줘",
        "extracted_command": {
            "kit_type": "BLACKOUT",
            "items": [
                {
                    "class_name": "water",
                    "qty": 1,
                }
            ],
        },
        "validation": {
            "result": "VALID",
            "reason": None,
        },
        "created_at": utc_now(),
    }

    result = commands.insert_one(document)

    print(f"[1] Command 저장: {result.inserted_id}")

# 전체 키트 작업을 나타내는 문서 생성
# None 값을 입력해 문서 구조와 예상 필드를 처음부터 확인 가능
# -> 관리 대상을 확정시켜 추후 값이 들어올 때 update 하도록
def start_kit_execution():
    """Kit 작업 시작 문서를 생성한다."""
    started_at = utc_now()

    document = {
        "kit_execution_id": KIT_EXECUTION_ID,
        "kit_type": "BLACKOUT",
        "status": "RUNNING",
        "requested_items": [
            {
                "class_name": "water",
                "qty": 1,
            }
        ],
        "component_summary": {
            "total": 1,
            "completed": 0,
            "failed": 0,
        },
        "status_history": [
            {
                "status": "RUNNING",
                "timestamp": started_at,
            }
        ],
        "final_inspection": None,
        "started_at": started_at,
        "ended_at": None,
    }

    result = kit_executions.insert_one(document)

    print(f"[2] Kit 시작: {result.inserted_id}")


def start_component_execution():
    """Component 작업 시작 문서를 생성한다."""
    document = {
        "component_execution_id": COMPONENT_EXECUTION_ID,
        "kit_execution_id": KIT_EXECUTION_ID,
        "class_name": "water",
        "sequence": 1,
        "attempt": 1,
        "status": "RUNNING",
        "started_at": utc_now(),
        "ended_at": None,
    }

    result = component_executions.insert_one(document)

    print(f"[3] Component 시작: {result.inserted_id}")


def save_detection_result():
    """객체 검출 및 위치 추정 결과를 추가한다."""
    result = component_executions.update_one(
        {
            "component_execution_id": COMPONENT_EXECUTION_ID,
            "status": "RUNNING",
        },
        {
            "$set": {
                "detection": {
                    "confidence": 0.94,
                    "target_position": {
                        "frame_id": "camera_link",
                        "x": 0.31,
                        "y": -0.12,
                        "z": 0.08,
                        "unit": "m",
                    },
                    "detected_at": utc_now(),
                }
            }
        },
    )

    print(
        "[4] Detection 저장: "
        f"modified={result.modified_count}"
    )


def save_grasp_result():
    """로봇 파지 결과를 추가한다."""
    result = component_executions.update_one(
        {
            "component_execution_id": COMPONENT_EXECUTION_ID,
            "status": "RUNNING",
        },
        {
            "$set": {
                "grasp": {
                    "result": "SUCCESS",
                    "position": {
                        "frame_id": "base",
                        "x": 0.45,
                        "y": 0.10,
                        "z": 0.12,
                        "unit": "m",
                    },
                    "completed_at": utc_now(),
                }
            }
        },
    )

    print(
        "[5] Grasp 저장: "
        f"modified={result.modified_count}"
    )


def complete_component_execution():
    """배치 결과를 추가하고 Component를 완료한다."""
    ended_at = utc_now()

    result = component_executions.update_one(
        {
            "component_execution_id": COMPONENT_EXECUTION_ID,
            "status": "RUNNING",
        },
        {
            "$set": {
                "release": {
                    "result": "SUCCESS",
                    "position": {
                        "frame_id": "base",
                        "x": 0.60,
                        "y": 0.20,
                        "z": 0.10,
                        "unit": "m",
                    },
                    "completed_at": ended_at,
                },
                "status": "COMPLETED",
                "ended_at": ended_at,
            }
        },
    )

    print(
        "[6] Component 완료: "
        f"modified={result.modified_count}"
    )


def complete_kit_execution():
    """최종 검사 결과를 추가하고 Kit를 완료한다."""
    ended_at = utc_now()

    result = kit_executions.update_one(
        {
            "kit_execution_id": KIT_EXECUTION_ID,
            "status": "RUNNING",
        },
        {
            "$set": {
                "status": "SUCCESS",
                "component_summary.completed": 1,
                "final_inspection": {
                    "result": "PASS",
                    "expected_count": 1,
                    "detected_count": 1,
                    "inspected_at": ended_at,
                },
                "ended_at": ended_at,
            },
            "$push": {
                "status_history": {
                    "status": "SUCCESS",
                    "timestamp": ended_at,
                }
            },
        },
    )

    print(
        "[7] Kit 완료: "
        f"modified={result.modified_count}"
    )


def print_result():
    """최종 저장 결과를 조회한다."""
    kit = kit_executions.find_one(
        {"kit_execution_id": KIT_EXECUTION_ID},
        {"_id": 0},
    )

    component = component_executions.find_one(
        {
            "component_execution_id":
                COMPONENT_EXECUTION_ID,
        },
        {"_id": 0},
    )

    print("\n[최종 Kit 문서]")
    pprint(kit)

    print("\n[최종 Component 문서]")
    pprint(component)


def main():
    reset_demo()

    save_command()
    sleep(1)

    start_kit_execution()
    sleep(1)

    start_component_execution()
    sleep(1)

    save_detection_result()
    sleep(1)

    save_grasp_result()
    sleep(1)

    complete_component_execution()
    sleep(1)

    complete_kit_execution()

    print_result()


if __name__ == "__main__":
    main()