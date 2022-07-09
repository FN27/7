"""
Platformer Game
"""
import arcade
import os

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Player starting position
PLAYER_START_X = 96
PLAYER_START_Y = 128

# Layer Names from our TileMap
LAYER_NAME_FOREGROUND_GRASS = "Foreground Grass"

LAYER_NAME_WALLS = "Walls"

LAYER_NAME_OBJECTS = "Objects"
LAYER_NAME_OBJECTS1 = "Objects1"
LAYER_NAME_OBJECTS2 = "Objects2"
LAYER_NAME_OBJECTS_EFFECTS = "Objects Effects"

LAYER_NAME_BACKGROUND_OBJECTS = "Background Objects"
LAYER_NAME_BACKGROUND_OBJECTS1 = "Background Objects1"
LAYER_NAME_BACKGROUND_OBJECTS2 = "Background Objects2"
LAYER_NAME_BACKGROUND_OBJECTS3 = "Background Objects3"
LAYER_NAME_BACKGROUND_OBJECTS4 = "Background Objects4"

LAYER_NAME_BACKGROUND_BUSHES = "Background Bushes"
LAYER_NAME_BACKGROUND_BUSHES1 = "Background Bushes1"

LAYER_NAME_BACKGROUND_TREES = "Background Trees"
LAYER_NAME_BACKGROUND_TREES1 = "Background Trees1"

LAYER_NAME_BACKGROUND_FENCE = "Background Fence"
LAYER_NAME_BACKGROUND_FENCE1 = "Background Fence1"

LAYER_NAME_BACKGROUND_HOUSES = "Background Houses"
LAYER_NAME_BACKGROUND_HOUSES1 = "Background Houses1"
LAYER_NAME_BACKGROUND_HOUSES2 = "Background Houses2"
LAYER_NAME_BACKGROUND_HOUSES3 = "Background Houses3"
LAYER_NAME_BACKGROUND_HOUSES4 = "Background Houses4"
LAYER_NAME_BACKGROUND_HOUSES5 = "Background Houses5"

LAYER_NAME_EMPTY_FIX_BACKGROUND = "Empty Fix Background"

# LAYER_NAME_BACKGROUND_COLOR = "Background Color"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        # Do we need to reset the score?
        self.reset_score = True

        # Where is the right edge of the map?
        self.end_of_map = 0

        # Level
        self.level = 1

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
        map_name = f"pre_game_map.json"

        # Layer Specific Options for the Tilemap
        layer_options = {
            LAYER_NAME_WALLS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_FOREGROUND_GRASS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_OBJECTS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_OBJECTS1: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_OBJECTS2: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_OBJECTS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_OBJECTS1: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_OBJECTS2: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_OBJECTS3: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_OBJECTS4: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_BUSHES: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_BUSHES1: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_TREES: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_TREES1: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_FENCE: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_FENCE1: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_HOUSES: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_HOUSES1: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_HOUSES2: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_HOUSES3: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_HOUSES4: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_BACKGROUND_HOUSES5: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_EMPTY_FIX_BACKGROUND: {
                "use_spatial_hash": True,
            },
            # LAYER_NAME_BACKGROUND_COLOR: {
            #     "use_spatial_hash": True,
            # },
        }

        # Load in TileMap
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initiate New Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Keep track of the score, make sure we keep the score if the player finishes a level
        if self.reset_score:
            self.score = 0
        self.reset_score = True

        # Add Player Spritelist before "Foreground" layer. This will make the foreground
        # be drawn after the player, making it appear to be in front of the Player.
        # Setting before using scene.add_sprite allows us to define where the SpriteList
        # will be in the draw order. If we just use add_sprite, it will be appended to the
        # end of the order.
        self.scene.add_sprite_list_after("Player", LAYER_NAME_FOREGROUND_GRASS)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ""
        self.player_sprite = arcade.Sprite("C:/Users/User/Desktop/Федя/Assets/platformer/Sprite_Player/Player_idol1.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=GRAVITY,
            walls=self.scene[LAYER_NAME_WALLS]
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
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
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # # See if we hit any coins
        # coin_hit_list = arcade.check_for_collision_with_list(
        #     self.player_sprite, self.scene[LAYER_NAME_COINS]
        # )
        #
        # # Loop through each coin we hit (if any) and remove it
        # for coin in coin_hit_list:
        #     # Remove the coin
        #     coin.remove_from_sprite_lists()
        #     # Play a sound
        #     arcade.play_sound(self.collect_coin_sound)
        #     # Add one to the score
        #     self.score += 1

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

        # Position the camera
        self.center_camera_to_player()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
