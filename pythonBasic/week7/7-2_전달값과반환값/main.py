print("7-2_전달값과 반환값 practise")


def deposit(balance, amount):
    print(f"{amount} 이 입금 되었습니다. 전체 잔액은 {balance + amount} 입니다.")
    return balance + amount


def withdraw(balance, amount):
    if amount > balance:
        print(f"잔액이 부족합니다. 현재 잔액 : {balance}, 출금 시도 금액 : {amount}")
        return balance
    else:
        print(f"{amount} 금액이 출금 되었습니다. 남은 잔액은 {balance - amount} 입니다.")
        return balance - amount


def withdraw_night(balance, amount):
    commission = 100
    if amount + commission > balance:
        print(f"잔액이 부족합니다. 현재 잔액 : {balance}, 출금 시도 금액 : {amount}, 수수료 : {commission}, 전체 출금 금액 : {amount + commission}")
        return commission, balance
    else:
        balance = balance - amount - commission
        print(f"{amount} 금액이 출금 되었습니다. 남은 잔액은 {balance} 입니다. (수수료 : {commission})")
        return commission, balance


my_balance = 0
my_balance = deposit(my_balance, 1000)
my_balance = withdraw(my_balance, 500)
# commission, my_balance = withdraw_night(my_balance, 500)
# print(commission, my_balance)

my_balance = withdraw_night(my_balance, 200)
print(my_balance)
