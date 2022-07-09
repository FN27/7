import random


class Enemy:
    def __init__(self, health, attack, armor, name):
        self.health = health
        if self.health <= 0:
            self.health=0
        self.attack = attack
        self.armor = armor
        self.name = name


    def be_attacked(self, attack):
        self.armor -= attack
        if self.armor < 0:
            self.health += self.armor
            if self.health <= 0:
                self.health = 0
            print(f"Броня {self.name} пробита, остаточный урон вычтен из здоровья, здоровье {self.name}: {self.health}")


class User(Enemy):
    def __init__(self, health, attack, armor, name):
        super().__init__(health, attack, armor, name)
        self.bonus = 3
        self.first_health=health

    def heal(self):
        heal = 20
        if self.health != user.health and self.bonus > 0:
            self.bonus -= 1
            self.health = self.health + heal
            print(f"Здоровье востановленно, текущее здоровье: {user.health}")
        if self.health == user.health:
            print(f"Личение не доступно, здоровье {user.health} из {user.first_health}")


user = User(130, 50, 20,  input("Введите имя: "))
print(f"Твоё здоровье: {user.health}, броня: {user.armor}, а атака: {user.attack}")
e1 = Enemy(170, 54, 0, "Kate")
e2 = Enemy(200, 36, 50, "Nick")
e3 = Enemy(100, 65, 20, "Jean")
e4 = Enemy(250, 13, 10, "Rex")
enemies = [e1, e2, e3, e4]
enemy = random.choice(enemies)
print(f"Соперник {enemy.name}")
print(f"Здоровье соперника: {enemy.health}, броня: {enemy.armor}, а атака: {enemy.attack}")
while True:
    print("")
    print("противник атаковал")
    user.be_attacked(enemy.attack)
    if user.health <= 0:
        print(f"Игра окончена, победил {enemy.name}")
        break
    elif enemy.health <= 0:
        print(f"{user.name}, ты победил!")
        break
    input_user = int(input("Введите число(1=восстановление здоровья(лечение восстонавливает 20 hp), 2=атака): "))
    if input_user == 1:
        user.heal()
    elif input_user == 2:
        enemy.be_attacked(user.attack)
    print("")
    print(f"Твоё здоровье: {user.health}, броня: {user.armor}, а атака: {user.attack} ")
    print(f"Здоровье соперника: {enemy.health}, броня: {enemy.armor}, а атака: {enemy.attack}")
    if user.health <= 0:
        print(f"Игра окончена, победил {enemy.name}")
        break
    elif enemy.health <= 0:
        print(f"{user.name}, ты победил!")
        break
