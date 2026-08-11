"""
유틸리티 함수 모음.

이 모듈은 공장 다중로봇 관제 시스템에서 사용되는 유틸리티 함수들을 포함합니다.
"""


def get_battery_status_message(percentage: float, timestamp):
    """
    배터리 상태 메시지 생성.

    Args:
        percentage: 배터리 잔량 (0.0 ~ 100.0)
        timestamp: 타임스탬프

    Returns:
        BatteryStatus 메시지
    """
    from factory_robot_control.msg import BatteryStatus

    msg = BatteryStatus()
    msg.percentage = percentage
    msg.timestamp = timestamp
    return msg


def create_charge_command(command: str):
    """
    충전 명령 서비스 요청 생성.

    Args:
        command: 명령어 ("START_CHARGE" 또는 "STOP_CHARGE")

    Returns:
        ChargeCommand 요청
    """
    from factory_robot_control.srv import ChargeCommand

    request = ChargeCommand.Request()
    request.command = command
    return request
