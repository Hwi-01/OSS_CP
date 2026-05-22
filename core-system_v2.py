def add(a, b):
    """두 수를 더한 결과를 반환합니다."""
    return a + b


def sub(a, b):
    """첫 번째 수에서 두 번째 수를 뺀 결과를 반환합니다."""
    return a - b


def mul(a, b):
    """두 수를 곱한 결과를 반환합니다."""
    return a * b


def div(a, b):
    """
    첫 번째 수를 두 번째 수로 나눈 결과를 반환합니다.
    분모가 0일 경우 ValueError를 발생시킵니다.
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / div_format_helper(b)  # 0.0 예외 처리 보완용


def div_format_helper(num):
    """부동소수점 -0.0 또는 0.0을 체크하기 위한 헬퍼 함수"""
    if num == 0:
        return 0
    return num


def calculate(a, op, b):
    """연산자에 따라 적절한 사칙연산 함수를 호출합니다."""
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)
    else:
        raise ValueError(f"지원하지 않는 연산자입니다: {op}")


def format_number(num):
    """
    출력 시 5.0 -> 5 와 같이 소수점 아래가 0이면 정수로 변환하고,
    5.5 -> 5.5 와 같이 소수점이 살아있으면 실수 그대로 반환하여 가독성을 높입니다.
    """
    if num.is_integer():
        return int(num)
    return num


def main():
    print("[계산기] / 종료: q")
    print("예: 1 + 1 (공백 필수)")

    while True:
        expr = input("입력: ")

        # 종료 조건 체크
        if expr.strip().lower() == "q":
            print("계산기를 종료합니다.")
            break

        try:
            parts = expr.split()

            # 입력 형식 검증 (피연산자1 연산자 피연산자2)
            if len(parts) != 3:
                print("공백이 없거나 입력 형식이 잘못되었습니다. (올바른 예: 1 + 1)")
                continue

            a_str, op, b_str = parts

            # 사칙연산자 유효성 검사
            if op not in ["+", "-", "*", "/"]:
                print("올바른 연산자를 입력하세요. (+, -, *, /)")
                continue

            # 숫자 변환 (실수형태까지 수용하기 위해 float 사용)
            a = float(a_str)
            b = float(b_str)

            # 연산 수행
            result = calculate(a, op, b)

            # 보기 좋게 숫자 포맷팅 (예: 1.0 -> 1)
            display_a = format_number(a)
            display_b = format_number(b)
            display_res = format_number(result)

            print(f"{display_a} {op} {display_b} = {display_res}")

        except ValueError as e:
            # 0으로 나눴을 때의 에러 및 숫자 변환 실패 에러 처리
            if "0으로 나눌 수 없습니다" in str(e):
                print(f"에러: {e}")
            else:
                print("에러: 유효한 숫자를 입력해 주세요.")
        except Exception as e:
            print("입력 오류가 발생했습니다:", e)


if __name__ == "__main__":
    main()