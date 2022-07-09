import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png", 0.1)
        self.rocket = Rocket("bar.png", 0.1)
        self.score = 0
        self.attempts = 3
        self.setup()

    def update(self, delta_time):

        self.ball.update()
        self.rocket.update()
        if arcade.check_for_collision(self.ball, self.rocket):
            self.ball.bottom = self.rocket.top
            self.ball.change_y = -self.ball.change_y
            self.score += 1
            print(self.score)
        if self.ball.bottom < 0:
            self.attempts -= 1
            if self.attempts == 0:
                self.setup()
                self.rocket.stop()
                self.ball.stop()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.rocket.change_x = -5
        if symbol == arcade.key.RIGHT:
            self.rocket.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.rocket.change_x = 0

    def setup(self):
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 5
        self.ball.change_y = 4
        self.rocket.center_x = 300
        self.rocket.center_y = 70
        self.rocket.change_x = 0

    def on_draw(self):
        self.clear((93, 138, 168))
        self.ball.draw()
        self.rocket.draw()
        arcade.draw_text(f"score= {self.score}", 20, 600 - 30)
        arcade.draw_text(f"attempts= {self.attempts}", 20, 600 - 50)
        if self.attempts <= 0:
            arcade.draw_text("You loose", 250, 300)


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > 600 or self.left < 0:
            self.change_x = -self.change_x
        elif self.top > 600 or self.bottom < 0:
            self.change_y = -self.change_y


class Rocket(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > 600:
            self.right = 600
        if self.left < 0:
            self.left = 0


game = Game(600, 600, "game")
arcade.run()
