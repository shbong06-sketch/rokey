from pprint import pprint

from database import (
    component_executions,
    kit_executions,
)


def calculate_kit_success_rate():
    """종료된 Kit의 전체 성공률을 계산한다."""
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

    result = list(
        kit_executions.aggregate(pipeline)
    )

    return result[0] if result else None


def calculate_grasp_success_rate():
    """파지 결과가 기록된 Component의 성공률을 계산한다."""
    pipeline = [
        {
            "$match": {
                "grasp.result": {
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
                                    "$grasp.result",
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
                                    "$grasp.result",
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

    result = list(
        component_executions.aggregate(pipeline)
    )

    return result[0] if result else None


def calculate_kit_type_metrics():
    """Kit 종류별 성공률을 계산한다."""
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
                "_id": "$kit_type",
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
                "kit_type": "$_id",
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
        {
            "$sort": {
                "kit_type": 1,
            }
        },
    ]

    return list(
        kit_executions.aggregate(pipeline)
    )


def main():
    print("\n[전체 Kit 성공률]")

    kit_metric = calculate_kit_success_rate()

    if kit_metric is None:
        print("집계할 종료 Kit가 없습니다.")
    else:
        pprint(kit_metric)

    print("\n[Component 파지 성공률]")

    grasp_metric = calculate_grasp_success_rate()

    if grasp_metric is None:
        print("집계할 파지 결과가 없습니다.")
    else:
        pprint(grasp_metric)

    print("\n[Kit 종류별 성공률]")

    kit_type_metrics = calculate_kit_type_metrics()

    if not kit_type_metrics:
        print("집계할 종료 Kit가 없습니다.")
    else:
        for metric in kit_type_metrics:
            pprint(metric)


if __name__ == "__main__":
    main()