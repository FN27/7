import time
import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.filedialog
import random

window = tk.Tk()
window.title("ИМБИРЪ")
window.geometry("200x300")


class Character:
    def __init__(self, health, attack, armor, name):
        self.health = health
        if self.health <= 0:
            self.health = 0
        self.attack = attack
        self.armor = armor
        self.name = name


class Enemy(Character):
    def __init__(self, health, attack, armor, name):
        super().__init__(health, attack, armor, name)
        self.place_x_health = 120
        self.place_y_health = 10
        self.place_x_armor = 120
        self.place_y_armor = 30
        self.health_text = tk.Label(window, text=f"{self.health} hp")
        self.health_text.place(x=self.place_x_health, y=self.place_y_health)
        self.armor_text = tk.Label(window, text=f"armor: {self.armor}")
        self.armor_text.place(x=self.place_x_armor, y=self.place_y_armor)

        self.displayed_name = tk.Label(window, text=f"name: {self.name}")
        self.displayed_name.place(x=120, y=50)


class User(Character):
    def __init__(self, health, attack, armor, name):
        super().__init__(health, attack, armor, name)
        self.max_health = health

        self.place_x_health = 10
        self.place_y_health = 10
        self.place_x_armor = 10
        self.place_y_armor = 30
        self.health_text = tk.Label(window, text=f"{self.health} hp")
        self.health_text.place(x=self.place_x_health, y=self.place_y_health)
        self.armor_text = tk.Label(window, text=f"armor: {self.armor}")
        self.armor_text.place(x=self.place_x_armor, y=self.place_y_armor)

        self.heal_button = tk.Button(window, text='Heal', command=None, width=10)
        self.heal_button.place(x=100, y=90)
        self.hit_button = tk.Button(window, text='Hit!', command=None, width=10)
        self.hit_button.place(x=10, y=90)

        self.reset_button = tk.Button(window, text='RESET', command=None, width=23)
        self.reset_button.place(x=10, y=120)

        self.stop_button = tk.Button(window, text='STOP', command=None, width=23)
        self.stop_button.place(x=10, y=150)

        self.displayed_name = tk.Label(window, text=f"name: {self.name}")
        self.displayed_name.place(x=10, y=50)


user = User(130, 50, 20, "Ben")
e1 = Enemy(170, 54, 0, "Kate")
e2 = Enemy(200, 36, 50, "Nick")
e3 = Enemy(100, 65, 20, "Jean")
e4 = Enemy(250, 13, 10, "Rex")
enemies = [e1, e2, e3, e4]
enemy = random.choice(enemies)

window.mainloop()
