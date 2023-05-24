print("8-3 파일 입출력\n")

# file = open("menus.txt", "w")
#
# file.write("비빔밥 : 10,000 원\n")
# file.write("불고기 : 12,000 원\n")
# file.write("된장 찌깨 : 10,000 원\n")
#
# file.close()

# file = open("menus.txt", "a")
# file.write("김치 : 2000 원\n")
# file.close()

# file = open("menus.txt", "r")
# menus = file.read()
# print(menus)
# file.close()

# file = open("menus.txt", "r")
# print(file.readline())
# print(file.readline())
# file.close()

file = open("menus.txt", "r")
menus = file.readlines()
for menu in menus:
    print(menu, end="")
file.close()
