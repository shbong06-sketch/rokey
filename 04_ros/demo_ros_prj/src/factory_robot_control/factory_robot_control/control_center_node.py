#!/usr/bin/env python3
"""
관제 센터 노드 - AMR 배터리 상태 모니터링 및 충전 명령.

이 모듈은 여러 AMR의 배터리 상태를 모니터링하고,
배터리 잔량이 15% 이하로 떨어지면 충전 명령을 내리는 ROS2 노드를 구현합니다.

통신 구조:
    - Subscriber: /robot_{id}/battery (BatteryStatus 메시지)
    - Service Client: /robot_{id}/charge_command (ChargeCommand 서비스)
"""

from typing import Dict, Optional

import rclpy
from rclpy.node import Node
from rclpy.timer import Timer
from rclpy.task import Future
from factory_robot_control.msg import BatteryStatus
from factory_robot_control.srv import ChargeCommand


class ControlCenterNode(Node):
    """
    관제 센터 노드 클래스.

    여러 AMR의 배터리 상태를 구독하고, 필요시 충전 명령을 내립니다.

    Attributes:
        managed_robots (Dict[int, float]): 관리 중인 로봇들의 배터리 상태
        CHARGE_THRESHOLD (float): 충전 시작 기준 배터리 잔량 (%)
    """

    CHARGE_THRESHOLD: float = 15.0

    def __init__(self, robot_ids: list = None):
        """
        노드 초기화.

        Args:
            robot_ids: 관리할 로봇 ID 목록 (기본값: [1])
        """
        super().__init__('control_center_node')

        if robot_ids is None:
            robot_ids = [1]
        self.robot_ids: list = robot_ids
        self.managed_robots: Dict[int, float] = {}
        self.subscribers: Dict[int, object] = {}
        self.charge_clients: Dict[int, object] = {}
        self.charge_futures: Dict[int, Optional[Future]] = {}

        # 각 로봇에 대한 Subscriber 및 Service Client 설정
        for robot_id in self.robot_ids:
            self.setup_robot_interface(robot_id)

        # 주기적 모니터링 타이머 (2초 간격)
        self.monitoring_timer: Timer = self.create_timer(2.0, self.monitor_battery_levels)

        self.get_logger().info(
            f'관제 센터 노드 시작\n'
            f'  - 관리 로봇 수: {len(self.robot_ids)}대\n'
            f'  - 로봇 ID: {self.robot_ids}\n'
            f'  - 충전 기준: {self.CHARGE_THRESHOLD}% 이하'
        )

    def setup_robot_interface(self, robot_id: int) -> None:
        """
        로봇과의 통신 인터페이스를 설정합니다.

        Args:
            robot_id: 로봇 고유 ID
        """
        subscriber = self.create_subscription(
            BatteryStatus,
            f'/robot_{robot_id}/battery',
            lambda msg, rid=robot_id: self.battery_callback(rid, msg),
            10
        )
        self.subscribers[robot_id] = subscriber

        charge_client = self.create_client(
            ChargeCommand,
            f'/robot_{robot_id}/charge_command'
        )
        self.charge_clients[robot_id] = charge_client

        self.managed_robots[robot_id] = 100.0

        self.get_logger().info(
            f'Robot {robot_id} 인터페이스 설정 완료\n'
            f'  - 구독: /robot_{robot_id}/battery\n'
            f'  - 서비스: /robot_{robot_id}/charge_command'
        )

    def battery_callback(self, robot_id: int, msg: BatteryStatus) -> None:
        """
        배터리 상태 수신 콜백 함수.

        Args:
            robot_id: 로봇 고유 ID
            msg: BatteryStatus 메시지
        """
        self.managed_robots[robot_id] = msg.percentage
        self.get_logger().debug(f'Robot {robot_id} 배터리: {msg.percentage:.1f}%')

    def monitor_battery_levels(self) -> None:
        """
        주기적으로 모든 로봇의 배터리 상태를 모니터링합니다.

        배터리 잔량이 15% 이하인 로봇에게 충전 명령을 보냅니다.
        """
        for robot_id, battery_level in self.managed_robots.items():
            if robot_id in self.charge_futures and self.charge_futures[robot_id] is not None:
                continue

            if battery_level <= self.CHARGE_THRESHOLD:
                self.get_logger().warn(
                    f'Robot {robot_id} 배터리 부족: {battery_level:.1f}% -> 충전 명령 전송'
                )
                self.send_charge_command(robot_id, "START_CHARGE")

    def send_charge_command(self, robot_id: int, command: str) -> None:
        """
        로봇에게 충전 명령을 보냅니다.

        Args:
            robot_id: 로봇 고유 ID
            command: 명령어 ("START_CHARGE" 또는 "STOP_CHARGE")
        """
        charge_client = self.charge_clients[robot_id]

        if not charge_client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error(f'Robot {robot_id} 서비스 서버 연결 실패')
            return

        request = ChargeCommand.Request()
        request.command = command
        future = charge_client.call_async(request)
        future.add_done_callback(
            lambda future, rid=robot_id: self.charge_response_callback(rid, future)
        )
        self.charge_futures[robot_id] = future

        self.get_logger().info(f'Robot {robot_id} 충전 명령 전송: {command}')

    def charge_response_callback(self, robot_id: int, future: Future) -> None:
        """
        충전 명령 응답을 처리하는 콜백 함수.

        Args:
            robot_id: 로봇 고유 ID
            future: 서비스 호출 결과
        """
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(f'Robot {robot_id} 충전 성공: {response.message}')
            else:
                self.get_logger().warn(f'Robot {robot_id} 충전 실패: {response.message}')
        except Exception as e:
            self.get_logger().error(f'Robot {robot_id} 오류: {str(e)}')
        finally:
            self.charge_futures[robot_id] = None


def main(args=None):
    """메인 함수."""
    rclpy.init(args=args)
    node = rclpy.create_node('control_center_init')
    num_robots = node.declare_parameter('num_robots', 3).value
    node.destroy_node()

    robot_ids = list(range(1, num_robots + 1))
    control_center = ControlCenterNode(robot_ids=robot_ids)
    try:
        rclpy.spin(control_center)
    except KeyboardInterrupt:
        pass
    finally:
        control_center.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
