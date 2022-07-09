import tkinter as tk


class Enemy:
    def __init__(self, health, attack, armor, name):
        self.health = health
        self.max_health = health
        self.attack = attack
        self.armor = armor
        self.name = name

    def be_attacked(self):
        self.health -= user.attack
        root.create_window()
        # user.be_attacked()


class User:
    def __init__(self, health, attack, armor, name):
        self.health = health
        self.max_health = health
        self.attack = attack
        self.armor = armor
        self.name = name

    def be_attacked(self):
        self.health -= enemy.attack
        root.create_window()

    def heal(self):
        self.health += 20
        self.be_attacked()
        root.create_window()


user = User(100, 10, 50, "Alex")
enemy = Enemy(100, 10, 0, "Shadow")


class Window:
    def __init__(self, name, one_geometry, two_geometry):
        self.name = name
        self.one_geometry = one_geometry
        self.two_geometry = two_geometry

    def create_window(self):
        window = tk.Tk()
        window.title(self.name)
        window.geometry(str(self.one_geometry) + "x" + str(self.two_geometry))
        c = tk.Canvas(window, width=550, height=20, bg='white')
        c.pack()
        c.create_rectangle(10, 10, user.max_health * 2, 20, fill="grey")
        c.create_rectangle(10, 10, user.health * 2, 20, fill="red")
        name_u = tk.Label(window, text=user.name)
        name_u.place(x=10, y=25)
        c.create_rectangle(345, 10, enemy.max_health * 2 + user.max_health * 2 + 135, 20, fill="grey")
        x = enemy.health - enemy.max_health
        c.create_rectangle(345 + -x, 10, enemy.max_health * 2 + user.max_health * 2 + 135, 20, fill="red")
        name_e = tk.Label(window, text=enemy.name)
        name_e.place(x=490, y=25)
        user_attack_button = tk.Button(window,  text="Атака", command=enemy.be_attacked(), width=20)
        user_attack_button.place(x=10, y=45)
        # user_heal_button = tk.Button(window, text="Лечение", command=user.heal(), width=20)
        # user_heal_button.place(x=100, y=30)
        window.mainloop()
        return window


root = Window("Окно", 550, 350)
root.create_window()
root.create_window().mainloop()
