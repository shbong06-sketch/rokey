# 데이터 저장 시각 기록용
from datetime import datetime, timezone
# 프로젝트 실행 식별자 생성
from uuid import uuid4

# 선택한 컬렉션 객체 가져오기
from database import (
    commands,
    component_executions,
    kit_executions,
)

# 공통 Kit 실행 ID - Kit 단위로 하나의 작업으로 묶는다.
KIT_EXECUTION_ID = "KIT-DEMO-001"
# 실제 프로젝트 적용 방안 - controller가 키트 작업 시작할 때 UUID 생성
# kit_execution_id = str(uuid4())

def remove_existing_demo_data():
    """스크립트 재실행 시 기존 데모 데이터만 제거한다."""
    # 조건 지정 : WHERE kit_execution_id = 'KIT_DEMO_001'
    condition = {
        "kit_execution_id": KIT_EXECUTION_ID,
    }

    # 중복 데이터 전부 제거 -> delete_many() 사용
    commands.delete_many(condition)
    component_executions.delete_many(condition)
    kit_executions.delete_many(condition)


def insert_command(now):
    # Command 문서 저장
    command_document = {
        "command_execution_id": str(uuid4()),
        "kit_execution_id": KIT_EXECUTION_ID,
        "scenario_id": "SCENARIO_01",
        "scenario_version": "v1",
        "stt_text": "정전 키트에 생수와 붕대를 넣어줘",
        "extracted_command": {
            "kit_type": "BLACKOUT",
            "items": [
                {
                    "class_name": "water",
                    "qty": 1,
                },
                {
                    "class_name": "bandage",
                    "qty": 1,
                },
            ],
        },
        "validation": {
            "result": "VALID",
            "reason": None,
        },
        "created_at": now,
    }
    # 문서 하나를 컬렉션에 저장 -> insert_one()
    result = commands.insert_one(command_document)

    print(f"Command inserted: {result.inserted_id}")

# 키트 전체 작업의 상태 저장 함수
def insert_kit_execution(now):
    kit_document = {
        "kit_execution_id": KIT_EXECUTION_ID,
        "kit_type": "BLACKOUT",
        "status": "RUNNING",
        "requested_items": [
            {
                "class_name": "water",
                "qty": 1,
            },
            {
                "class_name": "bandage",
                "qty": 1,
            },
        ],
        "component_summary": {
            "total": 2,
            "completed": 0,
            "failed": 0,
        },
        "final_inspection": None,
        "started_at": now,
        "ended_at": None,
    }

    result = kit_executions.insert_one(kit_document)

    print(f"Kit execution inserted: {result.inserted_id}")

# component 단위 작업의 상태 저장 함수
def insert_component_executions(now):
    component_documents = [
        {
            "component_execution_id": str(uuid4()),
            "kit_execution_id": KIT_EXECUTION_ID,
            "class_name": "water",
            "sequence": 1,
            "attempt": 1,
            "detection": {
                "confidence": 0.94,
                "target_position": {
                    "frame_id": "camera_link",
                    "x": 0.31,
                    "y": -0.12,
                    "z": 0.08,
                    "unit": "m",
                },
            },
            "grasp": {
                "result": "SUCCESS",
                "position": {
                    "frame_id": "base",
                    "x": 0.45,
                    "y": 0.10,
                    "z": 0.12,
                    "unit": "m",
                },
            },
            "release": {
                "result": "SUCCESS",
            },
            "status": "COMPLETED",
            "created_at": now,
        },
        {
            "component_execution_id": str(uuid4()),
            "kit_execution_id": KIT_EXECUTION_ID,
            "class_name": "bandage",
            "sequence": 2,
            "attempt": 1,
            "detection": {
                "confidence": 0.87,
                "target_position": {
                    "frame_id": "camera_link",
                    "x": 0.28,
                    "y": -0.08,
                    "z": 0.07,
                    "unit": "m",
                },
            },
            "grasp": {
                "result": "FAILED",
                "position": {
                    "frame_id": "base",
                    "x": 0.42,
                    "y": 0.14,
                    "z": 0.11,
                    "unit": "m",
                },
            },
            "release": {
                "result": "NOT_EXECUTED",
            },
            "status": "FAILED",
            "failure_code": "GRASP_FAILED",
            "created_at": now,
        },
    ]

    result = component_executions.insert_many(
        component_documents
    )

    print(
        "Component executions inserted: "
        f"{len(result.inserted_ids)}"
    )


def main():
    # 현재 시간 생성
    now = datetime.now(timezone.utc)
    # 기존 데모 데이터 제거
    remove_existing_demo_data()
    # command 1건 저장
    insert_command(now)
    # kit_execution 1건 저장
    insert_kit_execution(now)
    # component_execution 2건 저장
    insert_component_executions(now)

    print("\nDemo data creation completed")


if __name__ == "__main__":
    main()