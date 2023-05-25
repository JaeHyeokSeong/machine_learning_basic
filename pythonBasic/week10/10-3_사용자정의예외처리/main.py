print("10-3 사용자 정의 예외처리\n")


class BigNumberError(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message


try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    if a >= 10 or b >= 10:
        raise BigNumberError(f"입력된 값들 : {a}, {b}")
    print(f"{a} / {b} = {a/b}")
except BigNumberError as err:
    print(f"한자리 수 만 입력해 주세요 -> {err}")
else:
    print("올바른 값들이 입력되었습니다.")
finally:
    print("finally 이 실행 되었습니다.")

print("program end")
