print("5-5 자룍구조의 변경")

menu = {"coffee", "coke", "water"}
print(menu, type(menu))

menu = tuple(menu);
print(menu, type(menu))

menu = list(menu);
menu.append("juice")
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
