import random


class Insects:
    def __init__(self, name, food, hunger):
        self.name = name
        self.food = food
        self.hunger = hunger

    def eat(self):
        self.food -= 1
        self.hunger += 1
        print(f"{self.name} поел(а), уровень голода={self.hunger}, запас еды={self.food}")

    def find_food(self):
        a = random.randint(1, 3)
        self.food += a
        self.hunger -= 1
        print(f"найдено {a} единицы еды, уровень голода={self.hunger}, запас еды={self.food}")


class Bee(Insects):

    def __init__(self, name, food, hunger, honey_level):
        super().__init__(name, food, hunger)
        self.honey_level = honey_level

    def collecting_honey(self):
        self.honey_level += 1
        self.hunger -= 1
        print(f"найдена 1 единица мёда, пчела проголодалась, уровень голода={self.hunger}, запас еды={self.food}, "
              f"запас мёда={self.honey_level}")

    def live(self):
        if self.hunger <= 0:
            print(f'{self.name} died :(')
            return living
        action = random.randint(1, 3)
        if self.hunger < 4:
            if self.food <= 0:
                self.find_food()
            else:
                self.eat()
        else:
            if action == 1:
                self.collecting_honey()
            elif action == 2:
                if self.food > 0:
                    self.eat()
                else:
                    self.find_food()


bee = Bee("bee", 10, 1, 0)
for i in range(100):
    life = bee.live()
    if not life:
        print("пчела умерла")
        break
