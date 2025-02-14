import math

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (60, 60, 60)
light_grey = (128, 128, 128)
orange = (255, 128, 0)
dark_green = (0, 128, 0)
sky_blue = (0, 186, 255)
dark_grey = (32, 32, 32)
# window settings
FPS = 60
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
d = 10
FPS_POS = (WIDTH - 65, 5)

# player settings
player_pos = (500, 500)
player_angle = 0
player_speed = 5

# map settings
TILE = 100

# FOV
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COOF = DIST * TILE
SCALE = WIDTH // NUM_RAYS

# minimap
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# mouse settings
MOUSE_SENSITIVITY = 0.0021
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 200
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

# texture settings
TEXTURE_WIDTH = 1280
TEXTURE_HEIGHT = 853
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# sprite settings
pi_2 = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
