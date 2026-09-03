from pprint import pprint

from database import (
    commands,
    component_executions,
    kit_executions,
)


def find_valid_commands():
    """검증을 통과한 음성 명령을 조회한다."""
    query = {
        "validation.result": "VALID",
    }

    projection = {
        "_id": 0,
        "kit_execution_id": 1,
        "scenario_id": 1,
        "stt_text": 1,
        "validation.result": 1,
    }

    documents = commands.find(
        query,
        projection,
    ).sort("created_at", 1)

    print("\n[1. VALID 명령]")

    for document in documents:
        pprint(document)


def find_failed_grasps():
    """파지에 실패한 Component를 조회한다."""
    query = {
        "grasp.result": "FAILED",
    }

    projection = {
        "_id": 0,
        "kit_execution_id": 1,
        "component_execution_id": 1,
        "class_name": 1,
        "sequence": 1,
        "grasp.result": 1,
        "failure_code": 1,
    }

    documents = component_executions.find(
        query,
        projection,
    ).sort("sequence", 1)

    print("\n[2. 파지 실패 Component]")

    for document in documents:
        pprint(document)


def find_low_confidence_detections():
    """검출 신뢰도가 0.9 미만인 Component를 조회한다."""
    query = {
        "detection.confidence": {
            "$lt": 0.9,
        }
    }

    projection = {
        "_id": 0,
        "kit_execution_id": 1,
        "class_name": 1,
        "detection.confidence": 1,
    }

    documents = component_executions.find(
        query,
        projection,
    ).sort("detection.confidence", 1)

    print("\n[3. 신뢰도 0.9 미만 Detection]")

    for document in documents:
        pprint(document)


def find_successful_kits():
    """최종 검사에 통과한 Kit를 조회한다."""
    query = {
        "final_inspection.result": "PASS",
    }

    projection = {
        "_id": 0,
        "kit_execution_id": 1,
        "kit_type": 1,
        "status": 1,
        "component_summary": 1,
        "final_inspection": 1,
    }

    documents = kit_executions.find(
        query,
        projection,
    ).sort("started_at", 1)

    print("\n[4. 최종 검사 PASS Kit]")

    for document in documents:
        pprint(document)


def main():
    find_valid_commands()
    find_failed_grasps()
    find_low_confidence_detections()
    find_successful_kits()


if __name__ == "__main__":
    main()