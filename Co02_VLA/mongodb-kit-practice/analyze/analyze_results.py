import sys
from pathlib import Path
from pprint import pprint

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = PROJECT_ROOT / "app"

sys.path.append(str(APP_PATH))

from database import (  # noqa: E402
    component_executions,
    kit_executions,
)


def calculate_kit_success_rate():
    """종료된 Kit를 기준으로 전체 성공률을 계산한다."""
    pipeline = [
        {
            "$match": {
                "status": {
                    "$in": [
                        "SUCCESS",
                        "FAILED",
                    ]
                }
            }
        },
        {
            "$group": {
                "_id": None,
                "total": {
                    "$sum": 1,
                },
                "success": {
                    "$sum": {
                        "$cond": [
                            {
                                "$eq": [
                                    "$status",
                                    "SUCCESS",
                                ]
                            },
                            1,
                            0,
                        ]
                    }
                },
                "failed": {
                    "$sum": {
                        "$cond": [
                            {
                                "$eq": [
                                    "$status",
                                    "FAILED",
                                ]
                            },
                            1,
                            0,
                        ]
                    }
                },
            }
        },
        {
            "$project": {
                "_id": 0,
                "total": 1,
                "success": 1,
                "failed": 1,
                "success_rate": {
                    "$round": [
                        {
                            "$multiply": [
                                {
                                    "$divide": [
                                        "$success",
                                        "$total",
                                    ]
                                },
                                100,
                            ]
                        },
                        2,
                    ]
                },
            }
        },
    ]

    results = list(
        kit_executions.aggregate(pipeline)
    )

    if not results:
        return {
            "total": 0,
            "success": 0,
            "failed": 0,
            "success_rate": 0.0,
        }

    return results[0]


def calculate_grasp_rate_by_item():
    """품목별 파지 성공률을 계산한다."""
    pipeline = [
        {
            "$match": {
                "gr": {
                    "$exists": False,
                }
            }
        }
    ]