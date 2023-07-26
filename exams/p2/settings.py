import enum
from pygame.locals import (K_a, K_s, K_d, K_w, K_e)
from random import randint

GAME_VERSION = '0.0.0'
GAME_TITLE = f'Generic plataform game - v{GAME_VERSION}'
FPS = 60

TILE_SIZE = 64

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
VERTICAL_TILE_NUMBER = 15

PLAYER_SPEED = 8
PLAYER_GRAVITY = 0.5
PLAYER_JUMP_SPEED = -16
PLAYER_ANIMATION_SPEED = 0.09
PLAYER_ARROW_SPEED = 7.5
PLAYER_BOW_CD = 0.8
PLAYER_ARROW_DAMAGE = randint(1, 5)
PLAYER_MELEE_DAMAGE = randint(1, 5)

class PlayerControls(enum.Enum):
    UP = K_w
    DOWN = K_s
    RIGHT = K_d
    LEFT = K_a
    INTERACT = K_e

DEFAULT_ANIMATION_SPEED = 0.1

ENEMY_SPEED = randint(1, 3)

ASSETS_GFX_FOLDER = './assets/gfx'
SPRITESHEET_PATH = f'{ASSETS_GFX_FOLDER}/spritesheet_by_Alpatyk.png'
CURRENT_SPRITESHEET_TILE_SIZE = 16

DEBUG = False