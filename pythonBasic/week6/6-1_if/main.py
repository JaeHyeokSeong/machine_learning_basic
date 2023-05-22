print("if 문 연습")

temp = int(input("enter temperature: "))

if temp >= 30:
    print("too hot, bring water")
elif 10 <= temp < 30:
    print("perfect weather")
elif 0 <= temp < 10:
    print("bring a jacket")
else:
    print("very cold")

