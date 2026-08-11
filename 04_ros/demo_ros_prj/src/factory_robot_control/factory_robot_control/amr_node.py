#!/usr/bin/env python3
"""
AMR 로봇 노드 - 배터리 상태 발행 및 충전 서비스 서버.

이 모듈은 AMR(Autonomous Mobile Robot)의 배터리 상태를 발행하고,
관제 센터로부터의 충전 명령을 처리하는 ROS2 노드를 구현합니다.

통신 구조:
    - Publisher: /robot_{id}/battery (BatteryStatus 메시지, 1초 주기)
    - Service Server: /robot_{id}/charge_command (ChargeCommand 서비스)
"""

import random

import rclpy
from rclpy.node import Node
from rclpy.timer import Timer
from factory_robot_control.msg import BatteryStatus
from factory_robot_control.srv import ChargeCommand


class AmrNode(Node):
    """
    AMR 로봇 노드 클래스.

    각 로봇은 고유한 robot_id를 가지며, 이를 통해 토픽 네임스페이스를 구분합니다.
    배터리는 초기 100%에서 시작하여 랜덤하게 소모되며,
    15% 이하로 떨어지면 관제 센터에서 충전 명령을 내립니다.

    Attributes:
        robot_id (int): 로봇 고유 식별자
        battery_percentage (float): 현재 배터리 잔량 (0.0 ~ 100.0)
        is_charging (bool): 충전 중 여부
    """

    def __init__(self, robot_id: int):
        """
        노드 초기화.

        Args:
            robot_id: 로봇 고유 ID (토픽 네임스페이스 구분용)
        """
        super().__init__(f'amr_node_{robot_id}')
        self.robot_id = robot_id
        self.battery_percentage: float = 100.0
        self.is_charging: bool = False

        # Publisher: 배터리 상태 발행 (1초 주기)
        self.battery_publisher = self.create_publisher(
            BatteryStatus,
            f'/robot_{self.robot_id}/battery',
            10
        )

        # Service Server: 충전 명령 수신
        self.charge_service = self.create_service(
            ChargeCommand,
            f'/robot_{self.robot_id}/charge_command',
            self.handle_charge_command
        )

        # Timer: 1초 간격으로 배터리 상태 발행
        self.timer: Timer = self.create_timer(1.0, self.publish_battery_status)

        self.get_logger().info(
            f'AMR 노드 시작: Robot {robot_id}\n'
            f'  - 토픽: /robot_{robot_id}/battery\n'
            f'  - 서비스: /robot_{robot_id}/charge_command'
        )

    def publish_battery_status(self) -> None:
        """
        배터리 상태를 발행하는 콜백 함수.

        1초 간격으로 호출되며, 배터리 상태를 업데이트하고 발행합니다.
        충전 중이 아닐 경우 배터리가 랜덤하게 소모됩니다.
        """
        if not self.is_charging:
            # 배터리 소모: 0.5% ~ 2.0% 랜덤
            consumption = random.uniform(0.5, 2.0)
            self.battery_percentage = max(0.0, self.battery_percentage - consumption)
        else:
            # 충전 중: 배터리 10% 증가
            self.battery_percentage = min(100.0, self.battery_percentage + 10.0)

        # BatteryStatus 메시지 생성 및 발행
        msg = BatteryStatus()
        msg.percentage = self.battery_percentage
        msg.timestamp = self.get_clock().now().to_msg()
        self.battery_publisher.publish(msg)

        # 실시간 배터리 상태 로그 출력
        status = "충전 중" if self.is_charging else "사용 중"
        self.get_logger().info(f'[Robot {self.robot_id}] 배터리: {self.battery_percentage:.1f}% ({status})')

        # 배터리 15% 이하 경고
        if self.battery_percentage <= 15.0 and not self.is_charging:
            self.get_logger().warn(
                f'[Robot {self.robot_id}] ** 배터리 부족 ** {self.battery_percentage:.1f}% - 충전 필요!'
            )

    def handle_charge_command(
        self,
        request: ChargeCommand.Request,
        response: ChargeCommand.Response
    ) -> ChargeCommand.Response:
        """
        충전 명령 요청을 처리하는 콜백 함수.

        Args:
            request: 충전 명령 요청 ("START_CHARGE" 또는 "STOP_CHARGE")
            response: 충전 명령 응답

        Returns:
            ChargeCommand.Response: 처리 결과
        """
        command = request.command
        self.get_logger().info(f'충전 명령 수신: {command}')

        if command == "START_CHARGE":
            if self.is_charging:
                response.success = False
                response.message = "이미 충전 중입니다."
            else:
                self.is_charging = True
                response.success = True
                response.message = "충전이 시작되었습니다."
                self.get_logger().info('충전 시작')

        elif command == "STOP_CHARGE":
            if not self.is_charging:
                response.success = False
                response.message = "현재 충전 중이 아닙니다."
            else:
                self.is_charging = False
                response.success = True
                response.message = "충전이 중지되었습니다."
                self.get_logger().info('충전 중지')

        else:
            response.success = False
            response.message = f"알 수 없는 명령: {command}"
            self.get_logger().error(f'알 수 없는 명령: {command}')

        return response


def main(args=None):
    """메인 함수."""
    rclpy.init(args=args)
    node = rclpy.create_node('amr_node_initial')
    robot_id = node.declare_parameter('robot_id', 1).value
    node.destroy_node()

    amr_node = AmrNode(robot_id=robot_id)
    try:
        rclpy.spin(amr_node)
    except KeyboardInterrupt:
        pass
    finally:
        amr_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
