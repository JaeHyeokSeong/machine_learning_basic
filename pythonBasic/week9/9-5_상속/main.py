print("9-5 상속 practise\n")


class Unit:

    def __int__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit):

    def __init__(self, name, hp, damage):
        super().__int__(name, hp)
        self.damage = damage

    def attack(self, location):
        print(f"unit: {self.name} attacked {location}")

    def damaged(self, damage):
        self.hp -= damage
        print(f"unit: {self.name} damaged {damage} [remaining hp : {self.hp}]")
        if self.hp <= 0:
            print(f"unit: {self.name} destroyed")


marine1 = AttackUnit("marine", 30, 5)
marine1.attack("5'o clock")
marine1.damaged(20)
marine1.damaged(20)
