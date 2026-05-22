import ast
import operator as op

from add_sub import add, sub
from mul_div import mul, div


OPERATORS = {
    ast.Add: add,
    ast.Sub: sub,
    ast.Mult: mul,
    ast.Div: div,
}


def safe_eval(expr):
    node = ast.parse(expr, mode="eval").body

    def _eval(n):
        if isinstance(n, ast.Constant):
            return n.value

        if isinstance(n, ast.BinOp):
            left = _eval(n.left)
            right = _eval(n.right)

            return OPERATORS[type(n.op)](left, right)

        if isinstance(n, ast.UnaryOp):
            return -_eval(n.operand)

        raise ValueError("지원하지 않는 연산입니다")

    return _eval(node)


def main():
    print("[계산기] / 종료: q")

    while True:
        expr = input("입력: ")

        if expr.lower() == "q":
            break

        try:
            result = safe_eval(expr)
            print(f"{expr} = {result}")

        except Exception as e:
            print("에러:", e)


if __name__ == "__main__":
    main()