print("10-1 예외처리 practise\n")

print("나눈기 전용 계산기 입니다")

try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))

    print(f"{a} / {b} = {a / b}")
except ValueError as err:
    print(f"enter number : {err}")
except ZeroDivisionError as err:
    print(f"cannot divide it by zero : {err}")
except Exception as err:
    print(f"error happened : {err}")
