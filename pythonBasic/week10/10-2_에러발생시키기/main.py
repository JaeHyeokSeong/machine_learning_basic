print("10-2 에러 발생 시키기\n")

try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    if a >= 10 or b >= 10:
        raise ValueError("두자리 이상 숫자 입니다.")
    print(f"{a} / {b} = {a/b}")
except ValueError as err:
    print(f"한자리 수 만 입력해 주세요 -> {err}")