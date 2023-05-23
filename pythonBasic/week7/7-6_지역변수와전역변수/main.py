print("7-6 지역 변수와 전역 변수 practise\n")

a = 10
b = 1000


def test():
    global a
    a = 100


def test1():
    b = 10

    def test2():
        nonlocal b
        b = 100
        print(b)

    test2()
    print(b)


# test()
# print(a)

test1()
# print(b)  # 1000

gun = 10


def checkpoint(soldier):
    global gun
    gun = gun - soldier


checkpoint(2)
print(f"남은 총 : {gun}")
