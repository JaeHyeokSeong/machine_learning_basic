print("9-4 메소드 practise\n")


class AttackUnit:

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} 이 {location} 방향을 공격 하였습니다")

    def damaged(self, damage):
        self.hp -= damage
        print(f"{self.name} 이 {damage} 양의 피해량을 받았습니다 [남은 체력 : {self.hp}]")

        if self.hp <= 0:
            print(f"{self.name} 이 파괴 되었습니다")


marine1 = AttackUnit("marine", 40, 5)
marine1.attack("5 시")
marine1.damaged(20)
marine1.damaged(20)
