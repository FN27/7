import arcade
import time

# Constants
SCREEN_WIDTH = 1850
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Platformer"

x = None
# Constants used to scale our sprites from their original size
TILE_SCALING = 0.7
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
LAYER_NAME_OBJECTS = "Objects"


def load_texture_pair(filename):
    return [arcade.load_texture(filename), arcade.load_texture(filename, flipped_horizontally=True)]


class Objects(arcade.Sprite):
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


class Aim(Objects):
    def __init__(self, main_path):
        super().__init__(main_path)


class VillagerSeller(Objects):
    def __init__(self, main_path):
        super().__init__(main_path)


class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        super().__init__()
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


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
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
        self.E_pressed_and_villager_player_collision = False
        self.E_pressed = False
        self.Z_pressed = False
        self.X_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        # тест коллизии игрока и жителя
        self.villager_collision_with_player = None

        self.player_and_villager_first_meet = True

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
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)

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

        self.villager_sprite = VillagerSeller("C:/Users/User/Desktop/Федя/Assets/platformer/Sprite_Villager/Villager_idle_0.png")
        self.villager_sprite.center_x = VILLAGER_START_X
        self.villager_sprite.center_y = VILLAGER_START_Y
        self.scene.add_sprite(LAYER_NAME_OBJECTS, self.villager_sprite)

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



    def on_show_view(self):
        self.setup()

    def on_draw(self):
        """Render the screen."""

        self.clear()
        self.camera.use()
        self.scene.draw()
        self.gui_camera.use()
        self.aim_sprite.draw()
        self.camera.use()
        self.player_sprite.draw()

        if self.player_and_villager_first_meet and arcade.check_for_collision(self.player_sprite, self.villager_sprite):
            arcade.draw_text("Привет, не видела тебя здесь раньше,",
                             2210 * 1.5, 330,arcade.csscolor.WHEAT, 13, font_name="Sitka Subheading")
            arcade.draw_text("ты не местный, да?",
                             2210 * 1.5, 330 - 17 , arcade.csscolor.WHEAT, 13, font_name="Sitka Subheading")
            if not self.E_pressed_and_villager_player_collision:
                arcade.draw_text("Говорить: E", self.player_sprite.center_x + 30,
                                 self.player_sprite.center_y, arcade.csscolor.WHEAT, 13,
                                 font_name="Sitka Subheading")
                if self.E_relesed:
                    self.player_and_villager_first_meet = False


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
        if key == arcade.key.E:
            self.E_pressed = True
            print("e pressed")
            if self.E_pressed and arcade.check_for_collision(self.player_sprite, self.villager_sprite):
                self.E_pressed_and_villager_player_collision = True
                # dialog_view = DialogView()
                # self.window.show_view(dialog_view)
        elif not arcade.check_for_collision(self.player_sprite, self.villager_sprite):
            self.E_pressed_and_villager_player_collision = False

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
        if key == arcade.key.E:
            self.E_relesed = True

        self.process_keychange()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.aim_sprite.center_x = x
        self.aim_sprite.center_y = y

    def return_center_x(self):
        return self.player_sprite.center_x

    def center_camera_to_player(self, speed=0.2):
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
        self.player_sprite.update_animation(delta_time)

        # Position the camera
        self.center_camera_to_player()

# class DialogView(arcade.View):
#     def __init__(self):
#         super().__init__()
#         self.scene = None
#         self.tile_map = None
#         self.main_view = GameView()
#         self.setup()
#
#     def setup(self):
#         map_name = "C:/Users/User/Desktop/Федя/Assets/p"
#
#         # Layer Specific Options for the Tilemap
#         layer_options = {
#             LAYER_NAME_WALLS: {
#                 "use_spatial_hash": True,
#             },
#             LAYER_NAME_BACKGROUND: {
#                 "use_spatial_hash": False,
#             },
#         }
#
#         self.tile_map = arcade.load_tilemap("C:/Users/User/Desktop/Федя/Assets/platformer/безымянный.json", TILE_SCALING, layer_options)
#         self.scene = arcade.Scene.from_tilemap(self.tile_map)
#         self.camera = arcade.Camera(self.window.width, self.window.height)
#
#
#     def on_show_view(self):
#         arcade.set_background_color(arcade.color.BLACK)
#
#     def on_draw(self):
#         self.clear()
#         self.scene.draw()
#         self.camera.use()
#         self.camera.move_to()


def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = GameView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
