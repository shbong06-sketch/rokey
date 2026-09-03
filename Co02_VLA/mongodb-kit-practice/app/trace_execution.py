import sys
from datetime import datetime, timezone

from database import (
    component_executions,
    kit_executions,
)


TERMINAL_COMPONENT_STATUSES = [
    "COMPLETED",
    "FAILED",
]


def utc_now():
    return datetime.now(timezone.utc)


def count_component_results(kit_execution_id):
    """Kit에 포함된 Component 결과를 집계한다."""
    condition = {
        "kit_execution_id": kit_execution_id,
    }

    total = component_executions.count_documents(
        condition
    )

    completed = component_executions.count_documents({
        **condition,
        "status": "COMPLETED",
    })

    failed = component_executions.count_documents({
        **condition,
        "status": "FAILED",
    })

    running = component_executions.count_documents({
        **condition,
        "status": {
            "$nin": TERMINAL_COMPONENT_STATUSES,
        },
    })

    return {
        "total": total,
        "completed": completed,
        "failed": failed,
        "running": running,
    }


def determine_kit_status(
    component_summary,
    inspection_result,
):
    """Component와 최종 검사 결과로 Kit 상태를 판정한다."""
    if component_summary["running"] > 0:
        return None

    all_components_completed = (
        component_summary["total"] > 0
        and component_summary["completed"]
        == component_summary["total"]
    )

    inspection_passed = (
        inspection_result == "PASS"
    )

    if all_components_completed and inspection_passed:
        return "SUCCESS"

    return "FAILED"


def update_kit_status(
    kit_execution_id,
    inspection_result,
):
    """Kit 상태와 최종 검사 결과를 업데이트한다."""
    kit = kit_executions.find_one({
        "kit_execution_id": kit_execution_id,
    })

    if kit is None:
        print(
            f"Kit을 찾을 수 없습니다: "
            f"{kit_execution_id}"
        )
        return

    if kit.get("status") != "RUNNING":
        print(
            f"이미 종료된 Kit입니다: "
            f"{kit.get('status')}"
        )
        return

    component_summary = count_component_results(
        kit_execution_id
    )

    if component_summary["total"] == 0:
        print("연결된 Component가 없습니다.")
        return

    kit_status = determine_kit_status(
        component_summary,
        inspection_result,
    )

    if kit_status is None:
        print("아직 실행 중인 Component가 있습니다.")
        return

    ended_at = utc_now()

    result = kit_executions.update_one(
        {
            "kit_execution_id": kit_execution_id,
            "status": "RUNNING",
        },
        {
            "$set": {
                "status": kit_status,
                "component_summary": {
                    "total": component_summary["total"],
                    "completed": (
                        component_summary["completed"]
                    ),
                    "failed": component_summary["failed"],
                },
                "final_inspection": {
                    "result": inspection_result,
                    "inspected_at": ended_at,
                },
                "ended_at": ended_at,
            },
            "$push": {
                "status_history": {
                    "status": kit_status,
                    "timestamp": ended_at,
                }
            },
        },
    )

    print("\n[Kit 상태 업데이트]")
    print(f"kit_execution_id: {kit_execution_id}")
    print(f"component_summary: {component_summary}")
    print(f"inspection_result: {inspection_result}")
    print(f"kit_status: {kit_status}")
    print(f"matched: {result.matched_count}")
    print(f"modified: {result.modified_count}")


def main():
    if len(sys.argv) != 3:
        print(
            "사용법: python3 app/update_kit_status.py "
            "<kit_execution_id> <PASS|FAIL>"
        )
        return

    kit_execution_id = sys.argv[1]
    inspection_result = sys.argv[2].upper()

    if inspection_result not in ["PASS", "FAIL"]:
        print(
            "검사 결과는 PASS 또는 FAIL이어야 합니다."
        )
        return

    update_kit_status(
        kit_execution_id,
        inspection_result,
    )


if __name__ == "__main__":
    main()