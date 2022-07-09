import arcade
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'MY GAME'


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMBER)
        self.user = User('d353fb5506c37ef6ef1e7662dbbebe9e.png', 3)
        self.enemy = Enemy('transparent-sprite-character-61.png', 0.5)
        self.user_game = UserGame(100, 20, 50, 'User')
        self.enemy_game = EnemyGame(80, 15, 45, 'Enemy')
        self.setup()

    def setup(self):
        self.user.center_x = 10
        self.user.center_y = 100
        self.user.change_x = 0
        self.enemy.center_x = 550
        self.enemy.center_y = 100
        self.enemy.change_x = 0

    def on_draw(self):
        self.clear(arcade.set_background_color(arcade.color.AERO_BLUE))
        self.user.draw()
        self.enemy.draw()

    def update(self, delta_time):
        self.user.update()
        self.enemy.update()
        if self.user_game.health <= 0:
            self.user_game.life = False
        elif self.enemy_game.life <= 0:
            self.enemy_game.life = False
        # TODO: сделать условие: если life == false проигрыш одного или другого

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.user.change_x = -5
        if symbol == arcade.key.RIGHT:
            self.user.change_x = 5
        if symbol == arcade.key.LEFT and modifiers == arcade.key.LSHIFT:
            self.user.change_x = -10
        if symbol == arcade.key.RIGHT and modifiers == arcade.key.LSHIFT:
            self.user.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.user.change_x = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.user = User('d353fb5506c37ef6ef1e7662dbbebe9e(2).png)', 3)
            # только анимация атаки
            if arcade.check_for_collision(self.user, self.enemy):
                self.user_game.attack()
                # изменение характеристик

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.user = User('d353fb5506c37ef6ef1e7662dbbebe9e.png', 3)
            # Возврат анимации обратно


class UserGame:
    def __init__(self, health, damage, armor, name):
        super().__init__()
        self.health = health
        self.max_health = health
        self.attack = damage
        self.armor = armor
        self.name = name
        self.life = True

    def attack(self):
        pass
        # TODO: attack func(only parameter change)


class EnemyGame:
    def __init__(self, health, damage, armor, name):
        super().__init__()
        self.health = health
        self.max_health = health
        self.attack = damage
        self.armor = armor
        self.name = name
        self.life = True


class User(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > 600:
            self.right = 600
        if self.left < 0:
            self.left = 0

    def attack(self):
        pass
        # TODO: attack func(only skin change)


class Enemy(arcade.Sprite):
    pass


def main():
    game = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()

# первая часть не анимируемая