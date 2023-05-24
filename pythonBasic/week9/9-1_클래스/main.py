print("9-1 클래스 practise\n")


class Unit:
    total_unit = 0

    def __init__(self, name: str, hp: int, damage: int):
        self.__name = name
        self.__hp = hp
        self.__damage = damage
        Unit.total_unit += 1

    def info(self):
        print(f"name: {self.__name}, hp: {self.__hp}, damage: {self.__damage}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


marine1 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
marine1.info()
tank1.info()
print(Unit.total_unit)
print(marine1.name)
marine1.name = "marine"
marine1.info()
tank1.info()
