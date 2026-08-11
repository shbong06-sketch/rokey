#!/usr/bin/env python3
"""
공장 다중로봇 관제 대시보드.

ROS2 토픽을 구독하여 실시간으로 로봇 배터리 상태를 모니터링하고,
웹 브라우저에서 대시보드를 통해 상태를 확인할 수 있습니다.

실행 방법:
    python3 dashboard_server.py
    브라우저에서 http://localhost:8080 접속
"""

import json
import threading
import time
from collections import deque
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from factory_robot_control.msg import BatteryStatus
from factory_robot_control.srv import ChargeCommand


# ============================================================
# 전역 변수
# ============================================================
robot_data = {}  # {robot_id: {percentage, is_charging, timestamp}}
robot_history = {}  # {robot_id: deque([(time, percentage)])}
alerts = []  # 경고 메시지 목록
alerts_lock = threading.Lock()
data_lock = threading.Lock()
sse_clients = []  # SSE 클라이언트 목록


class DashboardRosNode(Node):
    """대시보드용 ROS2 노드."""

    def __init__(self, num_robots: int = 3):
        super().__init__('dashboard_node')
        self.num_robots = num_robots
        self.subscribers = {}
        self.charge_clients = {}

        for robot_id in range(1, num_robots + 1):
            self.setup_robot(robot_id)

        self.get_logger().info(f'대시보드 노드 시작: {num_robots}대 로봇 관리')

    def setup_robot(self, robot_id: int):
        """로봇 구독자 및 서비스 클라이언트 설정."""
        self.subscribers[robot_id] = self.create_subscription(
            BatteryStatus,
            f'/robot_{robot_id}/battery',
            lambda msg, rid=robot_id: self.battery_callback(rid, msg),
            10
        )

        self.charge_clients[robot_id] = self.create_client(
            ChargeCommand,
            f'/robot_{robot_id}/charge_command'
        )

        with data_lock:
            robot_data[robot_id] = {
                'percentage': 100.0,
                'is_charging': False,
                'timestamp': time.time()
            }
            robot_history[robot_id] = deque(maxlen=60)  # 60초 히스토리

    def battery_callback(self, robot_id: int, msg: BatteryStatus):
        """배터리 상태 수신 콜백."""
        with data_lock:
            old_data = robot_data.get(robot_id, {})
            old_charging = old_data.get('is_charging', False)

            robot_data[robot_id] = {
                'percentage': msg.percentage,
                'is_charging': old_charging,
                'timestamp': time.time()
            }
            robot_history[robot_id].append((time.time(), msg.percentage))

        # 배터리 15% 이하 경고
        if msg.percentage <= 15.0 and not old_charging:
            alert_msg = f'[Robot {robot_id}] 배터리 부족: {msg.percentage:.1f}%'
            with alerts_lock:
                alerts.append({'message': alert_msg, 'time': time.time(), 'robot_id': robot_id})

        # SSE 알림 전송
        self.notify_sse_clients()

    def send_charge_command(self, robot_id: int, command: str):
        """충전 명령 전송."""
        client = self.charge_clients.get(robot_id)
        if not client:
            return False

        if not client.wait_for_service(timeout_sec=2.0):
            return False

        request = ChargeCommand.Request()
        request.command = command
        future = client.call_async(request)

        try:
            result = future.result(timeout=5.0)
            with data_lock:
                if robot_id in robot_data:
                    robot_data[robot_id]['is_charging'] = (command == "START_CHARGE")
            return result.success
        except Exception:
            return False

    def notify_sse_clients(self):
        """SSE 클라이언트에게 상태 변경 알림."""
        data = get_all_data()
        for client in sse_clients[:]:
            try:
                client.put_data(f"data: {json.dumps(data)}\n\n")
            except Exception:
                sse_clients.remove(client)


def get_all_data():
    """전체 로봇 데이터 반환."""
    with data_lock:
        robots = {}
        for robot_id, data in robot_data.items():
            history = list(robot_history.get(robot_id, []))
            robots[robot_id] = {
                'percentage': data['percentage'],
                'is_charging': data['is_charging'],
                'timestamp': data['timestamp'],
                'history': history[-30:]  # 최근 30개
            }

    with alerts_lock:
        recent_alerts = [a for a in alerts if time.time() - a['time'] < 60]

    return {'robots': robots, 'alerts': recent_alerts}


# ============================================================
# 웹 서버 핸들러
# ============================================================
class DashboardHandler(SimpleHTTPRequestHandler):
    """대시보드 HTTP 핸들러."""

    ros_node = None

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == '/' or parsed.path == '/index.html':
            self.send_html(DASHBOARD_HTML)
        elif parsed.path == '/api/data':
            data = get_all_data()
            self.send_json(data)
        elif parsed.path == '/api/events':
            self.send_sse()
        elif parsed.path.startswith('/api/charge'):
            params = parse_qs(parsed.query)
            robot_id = int(params.get('robot_id', [1])[0])
            command = params.get('command', ['START_CHARGE'])[0]
            if self.ros_node:
                success = self.ros_node.send_charge_command(robot_id, command)
                self.send_json({'success': success})
            else:
                self.send_json({'success': False, 'error': 'ROS node not ready'})
        else:
            self.send_error(404)

    def send_html(self, html):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, default=str).encode('utf-8'))

    def send_sse(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Connection', 'keep-alive')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        queue = deque(maxlen=10)
        client_obj = type('Client', (), {'put_data': lambda self, d: queue.append(d)})()
        sse_clients.append(client_obj)

        try:
            while True:
                if queue:
                    data = queue.popleft()
                    self.wfile.write(data.encode('utf-8'))
                    self.wfile.flush()
                else:
                    # heartbeat
                    self.wfile.write(b": heartbeat\n\n")
                    self.wfile.flush()
                    time.sleep(1)
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            if client_obj in sse_clients:
                sse_clients.remove(client_obj)

    def log_message(self, format, *args):
        pass  # 로그 억제


# ============================================================
# 대시보드 HTML
# ============================================================
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>공장 다중로봇 관제 대시보드</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #1a1a2e;
            color: #eee;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #16213e, #0f3460);
            padding: 20px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e94560;
        }
        .header h1 { font-size: 24px; color: #e94560; }
        .header .status { font-size: 14px; color: #aaa; }
        .container { padding: 20px 30px; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }
        .stat-card {
            background: #16213e;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            border: 1px solid #0f3460;
        }
        .stat-card .value { font-size: 32px; font-weight: bold; color: #e94560; }
        .stat-card .label { font-size: 13px; color: #aaa; margin-top: 5px; }
        .robots-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }
        .robot-card {
            background: #16213e;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #0f3460;
            transition: transform 0.2s;
        }
        .robot-card:hover { transform: translateY(-2px); }
        .robot-card.warning { border-color: #ff6b35; animation: pulse 2s infinite; }
        .robot-card.charging { border-color: #00d4aa; }
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 5px rgba(255, 107, 53, 0.5); }
            50% { box-shadow: 0 0 20px rgba(255, 107, 53, 0.8); }
        }
        .robot-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .robot-id { font-size: 18px; font-weight: bold; }
        .robot-status {
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
        }
        .status-using { background: #333; color: #aaa; }
        .status-charging { background: #00d4aa22; color: #00d4aa; }
        .status-warning { background: #ff6b3522; color: #ff6b35; }
        .battery-container { margin: 15px 0; }
        .battery-bar-bg {
            width: 100%;
            height: 24px;
            background: #0f3460;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
        }
        .battery-bar {
            height: 100%;
            border-radius: 12px;
            transition: width 0.5s ease, background 0.5s ease;
        }
        .battery-bar.high { background: linear-gradient(90deg, #00d4aa, #00b894); }
        .battery-bar.medium { background: linear-gradient(90deg, #fdcb6e, #f39c12); }
        .battery-bar.low { background: linear-gradient(90deg, #e94560, #ff6b35); }
        .battery-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 12px;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }
        .battery-info { font-size: 12px; color: #aaa; margin-top: 8px; }
        .robot-actions { margin-top: 15px; }
        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
            font-weight: bold;
            transition: opacity 0.2s;
        }
        .btn:hover { opacity: 0.8; }
        .btn-charge { background: #00d4aa; color: #1a1a2e; }
        .btn-stop { background: #e94560; color: white; }
        .btn:disabled { opacity: 0.4; cursor: not-allowed; }
        .alerts-section {
            background: #16213e;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #0f3460;
        }
        .alerts-title { font-size: 16px; font-weight: bold; margin-bottom: 15px; color: #ff6b35; }
        .alert-item {
            padding: 10px 15px;
            background: #ff6b3511;
            border-left: 3px solid #ff6b35;
            border-radius: 4px;
            margin-bottom: 8px;
            font-size: 13px;
        }
        .no-alerts { color: #666; font-size: 13px; }
        .chart-container {
            background: #16213e;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #0f3460;
            margin-top: 20px;
        }
        canvas { width: 100% !important; height: 200px !important; }
    </style>
</head>
<body>
    <div class="header">
        <h1>공장 다중로봇 관제 대시보드</h1>
        <div class="status" id="connection-status">연결 중...</div>
    </div>
    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="value" id="total-robots">0</div>
                <div class="label">전체 로봇</div>
            </div>
            <div class="stat-card">
                <div class="value" id="charging-count" style="color: #00d4aa;">0</div>
                <div class="label">충전 중</div>
            </div>
            <div class="stat-card">
                <div class="value" id="warning-count" style="color: #ff6b35;">0</div>
                <div class="label">배터리 부족</div>
            </div>
            <div class="stat-card">
                <div class="value" id="avg-battery">0%</div>
                <div class="label">평균 배터리</div>
            </div>
        </div>

        <div class="robots-grid" id="robots-grid"></div>

        <div class="alerts-section">
            <div class="alerts-title">경고 알림</div>
            <div id="alerts-list">
                <div class="no-alerts">경고 없음</div>
            </div>
        </div>

        <div class="chart-container">
            <div class="alerts-title">배터리 히스토리</div>
            <canvas id="history-chart"></canvas>
        </div>
    </div>

    <script>
        let robotData = {};
        let chartData = {};

        function getBatteryClass(pct) {
            if (pct <= 15) return 'low';
            if (pct <= 50) return 'medium';
            return 'high';
        }

        function getStatusClass(robot) {
            if (robot.percentage <= 15 && !robot.is_charging) return 'warning';
            if (robot.is_charging) return 'charging';
            return 'using';
        }

        function getStatusText(robot) {
            if (robot.percentage <= 15 && !robot.is_charging) return '부족';
            if (robot.is_charging) return '충전 중';
            return '사용 중';
        }

        function updateDashboard(data) {
            robotData = data.robots;

            const robots = Object.entries(data.robots);
            const total = robots.length;
            const charging = robots.filter(([,r]) => r.is_charging).length;
            const warning = robots.filter(([,r]) => r.percentage <= 15 && !r.is_charging).length;
            const avg = total > 0 ? (robots.reduce((sum, [,r]) => sum + r.percentage, 0) / total).toFixed(1) : 0;

            document.getElementById('total-robots').textContent = total;
            document.getElementById('charging-count').textContent = charging;
            document.getElementById('warning-count').textContent = warning;
            document.getElementById('avg-battery').textContent = avg + '%';

            const grid = document.getElementById('robots-grid');
            grid.innerHTML = robots.map(([id, robot]) => `
                <div class="robot-card ${getStatusClass(robot)}">
                    <div class="robot-header">
                        <span class="robot-id">Robot ${id}</span>
                        <span class="robot-status status-${getStatusClass(robot)}">${getStatusText(robot)}</span>
                    </div>
                    <div class="battery-container">
                        <div class="battery-bar-bg">
                            <div class="battery-bar ${getBatteryClass(robot.percentage)}"
                                 style="width: ${robot.percentage}%"></div>
                            <span class="battery-text">${robot.percentage.toFixed(1)}%</span>
                        </div>
                    </div>
                    <div class="robot-info">
                        <div class="battery-info">최근 업데이트: ${new Date(robot.timestamp * 1000).toLocaleTimeString()}</div>
                    </div>
                    <div class="robot-actions">
                        ${robot.is_charging
                            ? `<button class="btn btn-stop" onclick="sendCommand(${id}, 'STOP_CHARGE')">충전 중지</button>`
                            : `<button class="btn btn-charge" onclick="sendCommand(${id}, 'START_CHARGE')" ${robot.percentage > 15 ? 'disabled' : ''}>충전 시작</button>`
                        }
                    </div>
                </div>
            `).join('');

            // 알림 업데이트
            const alertsList = document.getElementById('alerts-list');
            if (data.alerts && data.alerts.length > 0) {
                alertsList.innerHTML = data.alerts.sort((a, b) => b.time - a.time).map(a =>
                    `<div class="alert-item">${a.message} (${new Date(a.time * 1000).toLocaleTimeString()})</div>`
                ).join('');
            } else {
                alertsList.innerHTML = '<div class="no-alerts">경고 없음</div>';
            }

            // 차트 데이터 업데이트
            updateChart(data.robots);
        }

        function sendCommand(robotId, command) {
            fetch(`/api/charge?robot_id=${robotId}&command=${command}`)
                .then(r => r.json())
                .then(d => console.log('Command result:', d));
        }

        // SSE 연결
        function connectSSE() {
            const evtSource = new EventSource('/api/events');
            evtSource.onmessage = function(e) {
                const data = JSON.parse(e.data);
                updateDashboard(data);
                document.getElementById('connection-status').textContent = '실시간 연결됨';
                document.getElementById('connection-status').style.color = '#00d4aa';
            };
            evtSource.onerror = function() {
                document.getElementById('connection-status').textContent = '연결 끊어짐 (재연결 중...)';
                document.getElementById('connection-status').style.color = '#e94560';
            };
        }

        // 폴링 방식 (SSE 대안)
        function pollData() {
            fetch('/api/data')
                .then(r => r.json())
                .then(data => {
                    updateDashboard(data);
                    document.getElementById('connection-status').textContent = '연결됨';
                    document.getElementById('connection-status').style.color = '#00d4aa';
                })
                .catch(() => {
                    document.getElementById('connection-status').textContent = '연결 끊어짐';
                    document.getElementById('connection-status').style.color = '#e94560';
                });
        }

        // 차트 그리기 (간단한 Canvas 차트)
        function updateChart(robots) {
            const canvas = document.getElementById('history-chart');
            const ctx = canvas.getContext('2d');
            const width = canvas.parentElement.clientWidth - 40;
            const height = 200;
            canvas.width = width;
            canvas.height = height;

            ctx.clearRect(0, 0, width, height);

            const colors = ['#e94560', '#00d4aa', '#fdcb6e', '#74b9ff', '#a29bfe',
                           '#fd79a8', '#55efc4', '#ffeaa7', '#dfe6e9', '#636e72'];
            const legendY = 10;
            let legendX = 10;

            Object.entries(robots).forEach(([id, robot], idx) => {
                if (!robot.history || robot.history.length < 2) return;

                const color = colors[(parseInt(id) - 1) % colors.length];
                const history = robot.history;
                const padding = { top: 30, bottom: 30, left: 10, right: 10 };
                const chartW = width - padding.left - padding.right;
                const chartH = height - padding.top - padding.bottom;

                // 레전드
                ctx.fillStyle = color;
                ctx.fillRect(legendX, legendY, 12, 12);
                ctx.fillStyle = '#aaa';
                ctx.font = '11px sans-serif';
                ctx.fillText(`Robot ${id}`, legendX + 16, legendY + 10);
                legendX += 80;

                // 선 그리기
                ctx.beginPath();
                ctx.strokeStyle = color;
                ctx.lineWidth = 2;

                history.forEach((point, i) => {
                    const x = padding.left + (i / (history.length - 1)) * chartW;
                    const y = padding.top + chartH - (point[1] / 100) * chartH;
                    if (i === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                });
                ctx.stroke();
            });

            // Y축 라벨
            ctx.fillStyle = '#666';
            ctx.font = '10px sans-serif';
            ctx.fillText('100%', 2, 35);
            ctx.fillText('50%', 2, height / 2);
            ctx.fillText('0%', 2, height - 25);
            ctx.fillText('15%', 2, height - 25 + (1 - 15/100) * (height - 55));
        }

        // 초기 데이터 로드 및 폴링 시작
        pollData();
        setInterval(pollData, 1000);

        // SSE도 시도
        try { connectSSE(); } catch(e) {}
    </script>
</body>
</html>
"""


# ============================================================
# 메인 함수
# ============================================================
def ros_thread_func(num_robots):
    """ROS2 스레드 실행."""
    rclpy.init()
    node = DashboardRosNode(num_robots=num_robots)
    DashboardHandler.ros_node = node

    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        node.destroy_node()


def main():
    """메인 함수."""
    import sys

    num_robots = 3
    port = 8080

    # 명령줄 인자 처리
    for arg in sys.argv[1:]:
        if arg.startswith('--robots='):
            num_robots = int(arg.split('=')[1])
        elif arg.startswith('--port='):
            port = int(arg.split('=')[1])

    print(f'=== 공장 다중로봇 관제 대시보드 ===')
    print(f'로봇 수: {num_robots}대')
    print(f'포트: {port}')
    print(f'접속: http://localhost:{port}')
    print(f'================================')

    # ROS2 스레드 시작
    ros_thread = threading.Thread(target=ros_thread_func, args=(num_robots,), daemon=True)
    ros_thread.start()

    # ROS2 초기화 (메인 스레드에서)
    rclpy.init()

    # 웹 서버 시작
    server = HTTPServer(('0.0.0.0', port), DashboardHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n서버 종료')
    finally:
        server.server_close()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
