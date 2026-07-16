import rclpy
from rclpy.node import Node
from my_interfaces.msg import ArithmeticArgument
from my_interfaces.srv import ArithmeticOperator

class Operator(Node):
    def __init__(self):
        super().__init__('operator')
        # 노드의 역할
        # a, b값 구독 -> 저장 -> 연산 요청시 처리
        self.a = 0.0
        self.b = 0.0
        self.create_subscription(ArithmeticArgument, 'arithmetic/argument', self.on_arg, 10)
        # 서비스 구현
        self.create_service(ArithmeticOperator, 'arithmetic/operator', self.on_calc)

    # on_arg 콜백 함수의 역할
    # 구독된 값을 어떻게 처리하는가를 정한다.
    def on_arg(self, msg):
        self.a = msg.argument_a
        self.b = msg.argument_b
        self.get_logger().info(f"a : {self.a}  b : {self.b}")

    # on_calc 콜백 함수
    # 서비스 처리 서버 -> 요청(req)이 왔을 때, 요청과 응답을 콜백 함수에 전달
    def on_calc(self, req, res):
        # req에서 온 연산을 받아서 -> 1이면 PLUS, 2이면 MINUS, 3이면 MULTIPLY, 4이면 DIVISION
        op = req.arithmetic_operator
        if op == req.PLUS : res.arithmetic_result = self.a + self.b
        elif op == req.MINUS : res.arithmetic_result = self.a - self.b
        elif op == req.MULTIPLY : res.arithmetic_result = self.a * self.b
        elif op == req.DIVISION : 
            try:
                res.arithmetic_result = self.a / self.b
            except ZeroDivisionError:
                self.get_logger().error("Zero Division Error!")
        else:
            res.arithmetic_result = float('nan')
            self.get_logger().warning(f"알 수 없는 연산자 : {str(op)}")
        self.get_logger().info(f"정상 처리되었습니다. 연산자 : {str(op)}")

        return res
        # 계산하고, 결과를 res에 담고,
        # 이 res를 return해 준다.

def main():
    rclpy.init()
    node = Operator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()