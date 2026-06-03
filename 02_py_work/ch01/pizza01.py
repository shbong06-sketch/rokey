import tkinter as tk
from tkinter import messagebox

# 피자 종류
pizza_types = [
    "페퍼로니 피자",
    "야채 피자",
    "치즈 피자",
    "불고기 피자",
    "포테이토 피자",
    "고구마 피자"
]

# 피자 크기별 가격 (조각당)
pizza_prices = {
    "Small": 2500,
    "Medium": 3000,
    "Large": 3500
}

# 음료 가격
drink_prices = {
    "콜라": 1500,
    "사이다": 1500,
    "오렌지 주스": 2000
}


class OrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("피자 & 음료 주문 프로그램")

        title_label = tk.Label(root, text="피자와 음료 주문", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # ---------------- 피자 주문 영역 ----------------
        pizza_frame = tk.LabelFrame(root, text="피자 주문", padx=10, pady=10)
        pizza_frame.pack(padx=10, pady=5, fill="x")

        # 피자 종류 선택
        tk.Label(pizza_frame, text="피자 종류 선택:").grid(row=0, column=0, sticky="w")

        self.type_var = tk.StringVar(value=pizza_types[0])

        col = 1
        for p_type in pizza_types:
            tk.Radiobutton(
                pizza_frame,
                text=p_type,
                variable=self.type_var,
                value=p_type
            ).grid(row=0, column=col, padx=5)
            col += 1

        # 피자 크기 선택
        tk.Label(pizza_frame, text="피자 크기 선택:").grid(row=1, column=0, sticky="w", pady=5)

        self.size_var = tk.StringVar(value="Medium")

        col = 1
        for size in pizza_prices.keys():
            tk.Radiobutton(
                pizza_frame,
                text=f"{size} ({pizza_prices[size]}원/조각)",
                variable=self.size_var,
                value=size
            ).grid(row=1, column=col, padx=5)
            col += 1

        # 조각 수 입력
        tk.Label(pizza_frame, text="조각 개수:").grid(row=2, column=0, sticky="w", pady=5)

        self.slice_spinbox = tk.Spinbox(pizza_frame, from_=0, to=20, width=5)
        self.slice_spinbox.grid(row=2, column=1, pady=5)

        # ---------------- 음료 주문 영역 ----------------
        drink_frame = tk.LabelFrame(root, text="음료 주문", padx=10, pady=10)
        drink_frame.pack(padx=10, pady=5, fill="x")

        self.drink_quantities = {}

        row = 0
        for drink, price in drink_prices.items():
            tk.Label(
                drink_frame,
                text=f"{drink} ({price}원)",
                width=20,
                anchor="w"
            ).grid(row=row, column=0, padx=5, pady=5)

            spinbox = tk.Spinbox(drink_frame, from_=0, to=10, width=5)
            spinbox.grid(row=row, column=1, padx=5, pady=5)

            self.drink_quantities[drink] = spinbox
            row += 1

        # ---------------- 버튼 영역 ----------------
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        calc_button = tk.Button(
            button_frame,
            text="총 금액 계산",
            command=self.calculate_total
        )
        calc_button.grid(row=0, column=0, padx=5)

        order_button = tk.Button(
            button_frame,
            text="주문하기",
            command=self.place_order
        )
        order_button.grid(row=0, column=1, padx=5)

        self.total_label = tk.Label(root, text="총 금액: 0원", font=("Arial", 12))
        self.total_label.pack(pady=10)

    # 총 금액 계산
    def calculate_total(self):
        total = 0

        # 피자 계산
        p_type = self.type_var.get()
        size = self.size_var.get()
        slices = int(self.slice_spinbox.get())

        pizza_total = pizza_prices[size] * slices
        total += pizza_total

        # 음료 계산
        for drink, spinbox in self.drink_quantities.items():
            qty = int(spinbox.get())
            total += qty * drink_prices[drink]

        self.total_label.config(text=f"총 금액: {total}원")
        return total

    # 주문 처리
    def place_order(self):
        total = self.calculate_total()

        p_type = self.type_var.get()
        size = self.size_var.get()
        slices = int(self.slice_spinbox.get())

        if total == 0:
            messagebox.showwarning("경고", "주문한 항목이 없습니다.")
            return

        order_summary = "주문 내역:\n"

        # 피자 주문 내역
        if slices > 0:
            order_summary += (
                f"- {p_type}: {size} 사이즈 {slices}조각\n"
            )

        # 음료 주문 내역
        for drink, spinbox in self.drink_quantities.items():
            qty = int(spinbox.get())
            if qty > 0:
                order_summary += f"- {drink}: {qty}개\n"

        order_summary += f"\n총 금액: {total}원"

        messagebox.showinfo("주문 완료", order_summary)


if __name__ == "__main__":
    root = tk.Tk()
    app = OrderApp(root)
    root.mainloop()