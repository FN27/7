"""
Platformer Game
"""
import os
import time
import arcade


class TimerError(Exception):
    """Пользовательское исключение, используемое для сообщения об ошибках при использовании класса Timer"""


class Timer:

    def __init__(self):
        self._start_time = None

    def start(self):
        """Запуск нового таймера"""

        if self._start_time is not None:
            raise TimerError(f"Таймер уже работает. Используйте .stop() чтобы его остановить")

        self._start_time = time.perf_counter()

    def stop(self):
        """Отстановить таймер и сообщить о времени вычисления"""

        if self._start_time is None:
            raise TimerError(f"Таймер не работает. Используйте .start() для его запуска")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Вычисление заняло {elapsed_time:0.4f} секунд")


# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 1.5
COIN_SCALING = TILE_SCALING
SPRITE_PIXEL_SIZE = 96
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 20

PLAYER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 3
PLAYER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 4

VILLAGER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 49
VILLAGER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 4.5

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_WALLS = "Walls"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_ELSE_SPRITE = "Else Sprite"


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
    ]


class ElseSprite(arcade.Sprite):
    def __init__(self, main_path):
        super().__init__()

        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        self.character_face_direction = RIGHT_FACING
        self.main_path = main_path

        self.idle_texture_pair = load_texture_pair(self.main_path)

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]
        self.hit_box = self.texture.hit_box_points


class Aim(ElseSprite):
    def __init__(self, main_path):
        super().__init__(main_path)


class VillagerSeller(ElseSprite):
    def __init__(self, main_path):
        super().__init__(main_path)


class PlayerCharacter(arcade.Sprite):
    """Player Sprite"""

    def __init__(self):

        super().__init__()

        self.dialog_variant_0_0 = "(Что - то соврать)"
        self.dialog_text_0_0 = "Да...я тут с мамой..."
        self.dialog_text_0_0_1 = "то есть с девушкой...живу...давно"
        self.dialog_variant_0_1 = "Я не от сюда"
        self.dialog_text_0_1 = "Нет, я не от сюда, "
        self.dialog_text_0_1_1 = "я вообще не знаю откуда я..."

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        self.jumping = False
        self.climbing = False
        self.is_on_ladder = False

        main_path = ":resources:images/animated_characters/male_person/malePerson"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        self.jump_texture_pair = load_texture_pair(f"{main_path}_jump.png")
        self.fall_texture_pair = load_texture_pair(f"{main_path}_fall.png")

        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        self.climbing_textures = []
        texture = arcade.load_texture(f"{main_path}_climb0.png")
        self.climbing_textures.append(texture)
        texture = arcade.load_texture(f"{main_path}_climb1.png")
        self.climbing_textures.append(texture)

        self.texture = self.idle_texture_pair[0]
        self.hit_box = self.texture.hit_box_points

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Climbing animation
        if self.is_on_ladder:
            self.climbing = True
        if not self.is_on_ladder and self.climbing:
            self.climbing = False
        if self.climbing and abs(self.change_y) > 1:
            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
        if self.climbing:
            self.texture = self.climbing_textures[self.cur_texture // 4]
            return

        # Jumping animation
        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.fall_texture_pair[self.character_face_direction]
            return

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer for the game
        """

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the path to start with this program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Время
        self.stop_time = True
        self.total_time = 0.0
        self.seconds = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.space_pressed = False
        self.mouse_l_pressed = False
        self.skip_button_pressed = False
        self.E_pressed = False
        self.Z_pressed = False
        self.X_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        # тест коллизии игрока и жителя
        self.villager_collision_with_player = None

        self.set_mouse_visible(False)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.villager_sprite = None
        self.aim_sprite = None
        self.empty_text_background = None
        self.empty_text_background1 = None

        # Our 'physics' engine
        self.physics_engine = None

        self.physics_engine_for_else_sprites = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        self.end_of_map = 0
        self.camera_end = None

        # Keep track of the score
        self.score = 0

        # dialogs
        self.villager_dialog_text_place_x = None
        self.villager_dialog_text_place_y = None
        self.villager_dialog_text_color = None

        self.first_villager_phrase = True

        self.player_dialog_answer_variant_1_place_x = None
        self.player_dialog_answer_variant_1_place_y = None
        self.player_dialog_answer_variant_2_place_x = None
        self.player_dialog_answer_variant_2_place_y = None

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Map name
        map_name = "C:/Users/User/Desktop/Федя/Assets/platformer/безымянный.json"

        # Layer Specific Options for the Tilemap
        layer_options = {
            LAYER_NAME_WALLS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND: {
                "use_spatial_hash": False,
            },
            LAYER_NAME_FOREGROUND: {
                "use_spatial_hash": True,
            }
        }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.score = 0

        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player_sprite)

        self.villager_sprite = VillagerSeller(
            "C:/Users/User/Desktop/Федя/Assets/platformer/Sprite_Villager/Villager_idle_0.png")
        self.villager_sprite.center_x = VILLAGER_START_X
        self.villager_sprite.center_y = VILLAGER_START_Y
        self.scene.add_sprite(LAYER_NAME_ELSE_SPRITE, self.villager_sprite)

        self.aim_sprite = Aim("C:/Users/User/Desktop/Федя/Assets/platformer/Else/Aim.png")
        self.aim_sprite.center_x = 10
        self.aim_sprite.center_y = 10
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=GRAVITY,
            walls=self.scene[LAYER_NAME_WALLS]
        )

        self.physics_engine_for_else_sprites = arcade.PhysicsEnginePlatformer(
            self.villager_sprite,
            gravity_constant=GRAVITY,
            walls=self.scene[LAYER_NAME_WALLS]
        )

    def on_draw(self):
        """Render the screen."""

        self.clear()

        self.camera.use()

        self.scene.draw()

        self.villager_dialog_text_place_x = 2210
        self.villager_dialog_text_place_y = 300
        self.villager_dialog_text_color = arcade.csscolor.WHEAT

        self.player_dialog_answer_variant_1_place_x = 10
        self.player_dialog_answer_variant_1_place_y = 10
        self.player_dialog_answer_variant_2_place_x = 680
        self.player_dialog_answer_variant_2_place_y = 10

        if self.villager_collision_with_player and self.first_villager_phrase and not self.Z_pressed and not self.X_pressed:
            arcade.draw_text(self.villager_sprite.dialog_text_0, self.villager_dialog_text_place_x,
                             self.villager_dialog_text_place_y, self.villager_dialog_text_color, 13,
                             font_name="Sitka Subheading")
            arcade.draw_text(self.villager_sprite.dialog_text_0_1, self.villager_dialog_text_place_x,
                             self.villager_dialog_text_place_y - 17, self.villager_dialog_text_color, 13,
                             font_name="Sitka Subheading")
            if not self.E_pressed:
                arcade.draw_text("Говорить: E", self.player_sprite.center_x + 30,
                                 self.player_sprite.center_y, self.villager_dialog_text_color, 13,
                                 font_name="Sitka Subheading")
        if self.Z_pressed and not self.X_pressed and self.villager_collision_with_player:
            # Показ фразы при нажатии z
            self.stop_time = False

            if self.seconds < 5:
                arcade.draw_text(self.player_sprite.dialog_text_0_0, self.player_sprite.center_x + 30,
                                 self.player_sprite.center_y, self.villager_dialog_text_color, 13,
                                 font_name="Sitka Subheading")
                arcade.draw_text(self.player_sprite.dialog_text_0_0_1, self.player_sprite.center_x + 30,
                                 self.player_sprite.center_y - 30, self.villager_dialog_text_color, 13,
                                 font_name="Sitka Subheading")
            else:
                self.stop_time = True
        elif self.X_pressed and not self.Z_pressed and self.villager_collision_with_player and not self.skip_button_pressed and not self.stop_time:
            # Показ фразы при нажатии на x
            self.stop_time = False

            if self.seconds < 5:
                arcade.draw_text(self.player_sprite.dialog_text_0_1, self.player_sprite.center_x + 30,
                                 self.player_sprite.center_y, self.villager_dialog_text_color, 13,
                                 font_name="Sitka Subheading")
                arcade.draw_text(self.player_sprite.dialog_text_0_1_1, self.player_sprite.center_x + 30,
                                 self.player_sprite.center_y - 30, self.villager_dialog_text_color, 13,
                                 font_name="Sitka Subheading")
            else:
                self.stop_time = True

        self.gui_camera.use()

        self.aim_sprite.draw()

        # Проход мимо - показ фразы
        if self.villager_collision_with_player and self.villager_sprite.first_meet:
            if self.E_pressed:
                self.dialog_with_villager()

        score_text = f"Score: {self.score}"
        if not (self.score == 0):
            arcade.draw_text(score_text, 10, 10, arcade.csscolor.BLACK, 18)

    def dialog_with_villager(self):
        # Варианты ответа
        if not self.Z_pressed and not self.X_pressed:
            arcade.draw_text(self.player_sprite.dialog_variant_0_0, start_x=self.player_dialog_answer_variant_1_place_x,
                             start_y=self.player_dialog_answer_variant_1_place_y, font_name="Sitka Subheading")
            arcade.draw_text(self.player_sprite.dialog_variant_0_1, start_x=self.player_dialog_answer_variant_2_place_x,
                             start_y=self.player_dialog_answer_variant_2_place_y, font_name="Sitka Subheading")
            # название кнопки для выбора именно этого варианта ответа
            arcade.draw_text("Нажмите Z для этого варианта ответа:",
                             start_x=self.player_dialog_answer_variant_1_place_x,
                             start_y=self.player_dialog_answer_variant_1_place_y + 30, font_name="Sitka Subheading")

            arcade.draw_text("Нажмите X для этого варианта ответа:",
                             start_x=self.player_dialog_answer_variant_2_place_x,
                             start_y=self.player_dialog_answer_variant_2_place_y + 30, font_name="Sitka Subheading")


    def process_keychange(self):
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

        if self.physics_engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self.player_sprite.change_y = 0

        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        # Если нажата Е то E pressed, при отрицатеьной проверки на коллизию E not pressed
        if key == arcade.key.E and self.villager_collision_with_player:
            self.E_pressed = True
            print("e pressed")
        elif not self.villager_collision_with_player:
            self.E_pressed = False

        # Если нажата Z то Z pressed, при отрицатеьной проверки на коллизию Z not pressed
        if key == arcade.key.Z and self.villager_collision_with_player:
            self.Z_pressed = True
            print("z pressed")
        elif not self.villager_collision_with_player:
            self.Z_pressed = False

        # Если нажата Z то Z pressed, при отрицатеьной проверки на коллизию X not pressed
        if key == arcade.key.X and self.villager_collision_with_player:
            self.X_pressed = True
            print("x pressed")
        elif not self.villager_collision_with_player:
            self.X_pressed = False

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.aim_sprite.center_x = x
        self.aim_sprite.center_y = y

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

        self.camera_end = (SPRITE_PIXEL_SIZE * TILE_SCALING * 56, 0)
        # 56 у камеры для 78, 67 у спрайта для 78(тайлов)
        if self.player_sprite.center_x >= SPRITE_PIXEL_SIZE * TILE_SCALING * 67:
            self.camera.move_to(self.camera_end)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()
        self.physics_engine_for_else_sprites.update()

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

        self.villager_collision_with_player = arcade.check_for_collision(self.villager_sprite, self.player_sprite)

        if self.villager_collision_with_player and self.E_pressed:
            self.villager_sprite.texture = self.villager_sprite.idle_texture_pair[0]

        # Update Animations
        self.scene.update_animation(
            delta_time * 20, [LAYER_NAME_PLAYER]
        )

        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

        # Position the camera
        self.center_camera_to_player()

        if not self.stop_time:
            self.total_time += delta_time
            self.seconds = int(self.total_time) % 60
        else:
            self.seconds = 0
        return self.seconds


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
