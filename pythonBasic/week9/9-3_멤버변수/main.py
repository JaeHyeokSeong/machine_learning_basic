print("9-3 멤버 변수 practise\n")


class Unit:

    def __init__(self, name: str, hp: int, damage: int):
        self.__name = name
        self.__hp = hp
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def damage(self):
        return self.__damage

    @name.setter
    def name(self, name: str):
        self.__name = name


marine1 = Unit("marine", 30, 5)
print(f"name: {marine1.name}, hp: {marine1.hp}, damage: {marine1.damage}")


def add(a, b, c):
    print(a + b + c)


def add_menu_price(pizza, hamburger, coke):
    print(pizza + hamburger + coke)


# unpacking practise
numbers = [1, 2, 3]
add(*numbers)  # unpacking

menus = {"pizza": 10, "hamburger": 10, "coke": 4}
add_menu_price(*menus)  # key 들의 합
add_menu_price(**menus)  # value 들의 합
