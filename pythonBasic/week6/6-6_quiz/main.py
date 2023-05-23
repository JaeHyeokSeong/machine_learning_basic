from random import randrange

print("6-6 quiz")

customer = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        customer += 1
        print(f"[O] {i}번째 손님 (소요시간 : {time})")
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {time})")

print(f"총 탑승 승객 : {customer} 분")
