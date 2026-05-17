from operations.A.add_sub import add, sub
from operations.B.mul_div import mul, div


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return div(a, b)


def main():
    print("[계산기] / 종료: q")
    print("예: 1 + 1 (공백 필수)")

    while True:
        expr = input("입력: ")

        if expr.lower() == "q":
            break

        try:
            parts = expr.split()

            if len(parts) != 3:
                print("공백이 없거나 입력 형식이 잘못되었습니다.(올바른 예: 1 + 1)")
                continue

            a, op, b = parts

            a = float(a)
            b = float(b)

            result = calculate(a, op, b)

            print(f"{a} {op} {b} = {result}")

        except ValueError as e:
            print("에러:", e)
        except Exception as e:
            print("입력 오류:", e)


if __name__ == "__main__":
    main()