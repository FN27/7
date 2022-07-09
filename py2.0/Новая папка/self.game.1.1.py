import arcade
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = 'Fighting'
# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2
COIN_SCALING = TILE_SCALING
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING
# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 30

PLAYER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 2
PLAYER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 1

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"


def load_texture_pair(filename):
    return [arcade.load_texture(filename), arcade.load_texture(filename, flipped_horizontally=True)]


class User(arcade.Sprite):
    cur_texture: int
    character_face_direction: int

    def __init__(self):
        super().__init__()
        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        # stage
        self.jumping = False
        self.is_on_ladder = False

        # --- Load Textures ---

        main_path = 'Male adventurer/PNG/Poses HD/'
        male_first_name_part = 'character_maleAdventurer_'

        self.idle_texture_pair = load_texture_pair(f"{main_path}{male_first_name_part}idle.png")
        self.jump_texture_pair = load_texture_pair(f"{main_path}{male_first_name_part}jump.png")
        self.fall_texture_pair = load_texture_pair(f"{main_path}{male_first_name_part}fall.png")
        self.down_texture = load_texture_pair(f"{main_path}{male_first_name_part}down.png")

        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}{male_first_name_part}walk{i - 1}.png")
            self.walk_textures.append(texture)

        self.run_textures = []
        for i in range(3):
            texture = load_texture_pair(f"{main_path}{male_first_name_part}run{i - 1}.png")
            self.run_textures.append(texture)

        self.attack_textures = []
        for i in range(3):
            texture = load_texture_pair(f"{main_path}{male_first_name_part}attack{i - 1}.png")
            self.attack_textures.append(texture)

        self.texture = self.idle_texture_pair[0]

        self.hit_box = self.texture.hit_box_points

    def update_animation(self, delta_time: float = 1 / 60):
        # Изменение анимации в зависимости от направления движения
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.fall_texture_pair[self.character_face_direction]
            return

        # Изменение анимации в зависимости от направления движения
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]

        # Attacking animation
        self.cur_texture += 1
        if self.cur_texture > 2:
            self.cur_texture = 0
        self.texture = self.attack_textures[self.cur_texture][self.character_face_direction]

        # Running animation
        self.cur_texture += 1
        if self.cur_texture > 2:
            self.cur_texture = 0
        self.texture = self.run_textures[self.cur_texture][self.character_face_direction]


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # --- Don't really know what doing these code below ---

        self.up_pressed = True
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # stage
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        # --- Don't really know what doing these code below ---

        self.title_map = None

        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our 'physics' engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        self.end_of_map = 0

        # I do not really need score here, but why not.   :)

        self.score = 0

        # Load sounds

        self.game_over_sound = arcade.load_sound('mixkit-sad-game-over-trombone-471.wav')
        self.jump_sound = arcade.load_sound('mixkit-footsteps-on-tall-grass-532.wav')
        self.attack_sound = arcade.load_sound('mixkit-fighting-man-voice-2172.wav')
        self.user_hurting_sound = arcade.load_sound('mixkit-man-in-pain-2197.wav')
        self.background_sound = arcade.load_sound('purrple-cat-supernova.wav')

    def setup(self):
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)
        map_name = None

        layer_options = {
            LAYER_NAME_PLATFORMS: {"use_spatial_hash": True, },
            LAYER_NAME_MOVING_PLATFORMS: {"use_spatial_hash": False},
            LAYER_NAME_LADDERS: {"use_spatial_hash": True},
            LAYER_NAME_COINS: {"use_spatial_hash": True}
        }

        self.title_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.title_map)

        self.score = 0

        self.player_sprite = PlayerCharacter()

        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.user)

        self.end_of_map = self.title_map.width * GRID_PIXEL_SIZE

        if self.title_map.background_color:
            arcade.set_background_color(self.title_map.background_color)

        # physics

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            platforms=self.scene[LAYER_NAME_MOVING_PLATFORMS],
            gravity_constant=GRAVITY,
            ladders=self.scene[LAYER_NAME_LADDERS],
            walls=self.scene[LAYER_NAME_PLATFORMS]
        )

    def on_draw(self):
        self.clear()

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.BLACK, 18)

        # for wall if self.wall.list:
        #     wall.draw_hit_box(arcade.color.BLACK, 3)
        # self.player_sprite.draw_hit_box(arcade.color.RED, 3)

    def press_keychange(self):
        """
        Called when we change a key up/down or we move on/off a ladder.
        """
        # Process up/down
        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            elif (
                    self.physics_engine.can_jump(y_distance=10)
                    and not self.jump_needs_reset
            ):
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                self.jump_needs_reset = True
                arcade.play_sound(self.jump_sound)
        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

        # Process up/down when on a ladder and no movement
        if self.physics_engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self.player_sprite.change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            pass
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
                self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered, 0.2)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # Update animations
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        if self.physics_engine.is_on_ladder() and not self.physics_engine.can_jump():
            self.player_sprite.is_on_ladder = True
            self.process_keychange()
        else:
            self.player_sprite.is_on_ladder = False
            self.process_keychange()

        # Update Animations
        self.scene.update_animation(
            delta_time, [LAYER_NAME_COINS, LAYER_NAME_BACKGROUND, LAYER_NAME_PLAYER]
        )

        # Update walls, used with moving platforms
        self.scene.update([LAYER_NAME_MOVING_PLATFORMS])

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_COINS]
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:

            # Figure out how many points this coin is worth
            if "Points" not in coin.properties:
                print("Warning, collected a coin without a Points property.")
            else:
                points = int(coin.properties["Points"])
                self.score += points

                # Remove the coin
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)

        # Position the camera
        self.center_camera_to_player()


def main():
    """Main function"""
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
