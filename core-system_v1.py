from operations.A.A import add, sub
from operations.B.B import mul, div


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)


def main():
    print("[계산기] / 종료: q")

    while True:
        expr = input("입력: ")

        if expr.lower() == "q":
            break

        try:
            a, op, b = expr.split()

            a = float(a)
            b = float(b)

            result = calculate(a, op, b)

            print(f"{a} {op} {b} = {result}")

        except Exception as e:
            print("에러:", e)


if __name__ == "__main__":
    main()