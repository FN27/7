"""
Platformer Game
"""
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

PLAYER_MOVEMENT_SPEED = 2
GRAVITY = 1.4
PLAYER_JUMP_SPEED = 20

PLAYER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 2
PLAYER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 3

LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_WALLS = "Walls"
LAYER_NAME_BACKGROUND= "Background"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None

        # Our Scene Object
        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        self.camera = None

        self.gui_camera = None

        self.score = 0

        self.reset_score = True

        self.end_of_map = 0

        self.level = 1

        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        map_name = "C:/Users/User/Desktop/Федя/Assets/platformer/безымянный.json"

        layer_options = {
            LAYER_NAME_WALLS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_FOREGROUND: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND: {
                'use spatial_hash': True
            }
        }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        if self.reset_score:
            self.score = 0
        self.reset_score = True

        # Add Player Spritelist before "Foreground" layer. This will make the foreground
        # be drawn after the player, making it appear to be in front of the Player.
        # Setting before using scene.add_sprite allows us to define where the SpriteList
        # will be in the draw order. If we just use add_sprite, it will be appended to the
        # end of the order.
        self.scene.add_sprite_list_after("", LAYER_NAME_FOREGROUND, use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = "C:/Users/User/Desktop/Федя/Assets/platformer/Sprite_Player/Medieval Warrior(Version 1.2)/Medieval Warrior Pack/idol1.png"
        self.player_sprite = arcade.Sprite("C:/Users/User/Desktop/Федя/Assets/platformer/Sprite_Player/idle1.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("", self.player_sprite)

        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=GRAVITY,
            walls=self.scene[LAYER_NAME_WALLS]
        )

    def on_draw(self):
        """Render the screen."""

        self.clear()

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.BLACK,
            18,
        )

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = (self.player_sprite.center_x - (self.camera.viewport_width / 4))
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 4
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x + 70, screen_center_y

        self.camera.move_to(player_centered)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if x == arcade.MOUSE_BUTTON_LEFT:
            print("Z")

    def update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.update()

        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            arcade.play_sound(self.game_over)

        # # Did the player touch something they should not?
        # if arcade.check_for_collision_with_list(
        #     self.player_sprite, self.scene[LAYER_NAME_DONT_TOUCH]
        # ):
        #     self.player_sprite.change_x = 0
        #     self.player_sprite.change_y = 0
        #     self.player_sprite.center_x = PLAYER_START_X
        #     self.player_sprite.center_y = PLAYER_START_Y

            arcade.play_sound(self.game_over)

        if self.player_sprite.center_x >= self.end_of_map:

            self.level += 1

            self.reset_score = False

            self.setup()

        # Position the camera
        self.center_camera_to_player()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
