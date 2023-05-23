print("7-5 가변인자 practise")


# *menu 는 tuple 이 들어가게 된다
def restaurant_menu(category, *menu):
    print(category, menu)


restaurant_menu("korean", "비빔밥", "불고기", "김치", "후라이드")
restaurant_menu("japanese", "초밥", "우동", "회")


# **menu 는 dict 가 들어가게 된다
def restaurant_menu_price(category, **menu):
    print(category, menu)


restaurant_menu_price("korean", 비빔밥=20, 불고기=23)
