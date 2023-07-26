import pygame
from tiles import AnimatedTile, StaticTile
from settings import ASSETS_GFX_FOLDER, VERTICAL_TILE_NUMBER, TILE_SIZE, SCREEN_WIDTH
from utils import import_image_folder
from random import choice, randint

SKY_TOP_PATH = f'{ASSETS_GFX_FOLDER}/decorations/sky/sky_top.png'
SKY_MIDDLE_PATH = f'{ASSETS_GFX_FOLDER}/decorations/sky/sky_middle.png'
SKY_BOTTOM_PATH = f'{ASSETS_GFX_FOLDER}/decorations/sky/sky_bottom.png'
CLOUDS_FOLDER_PATH = f'{ASSETS_GFX_FOLDER}/decorations/clouds'


class Sky:
    def __init__(self, horizon):
        self.horizon = horizon

        self.top = pygame.image.load(SKY_TOP_PATH).convert()
        self.middle = pygame.image.load(SKY_MIDDLE_PATH).convert()
        self.bottom = pygame.image.load(SKY_BOTTOM_PATH).convert()

        self.top = pygame.transform.scale(self.top, (SCREEN_WIDTH, TILE_SIZE))
        self.middle = pygame.transform.scale(self.middle, (SCREEN_WIDTH, TILE_SIZE))
        self.bottom = pygame.transform.scale(self.bottom, (SCREEN_WIDTH, TILE_SIZE))
    
    def draw(self, screen):
        for row in range(VERTICAL_TILE_NUMBER):
            y = row * TILE_SIZE
            if row < self.horizon:
                screen.blit(self.top, (0, y))
            elif row == self.horizon:
                screen.blit(self.middle, (0, y))
            else:
                screen.blit(self.bottom, (0, y))

class Clouds:
    def __init__(self, horizon, level_width, cloud_number):
        cloud_surf_list = import_image_folder(CLOUDS_FOLDER_PATH)
        min_x = -SCREEN_WIDTH
        max_x = level_width + SCREEN_WIDTH
        min_y = 0
        max_y = horizon
        self.cloud_sprites = pygame.sprite.Group()
    
        for _ in range(cloud_number):
            cloud = choice(cloud_surf_list)
            x = randint(min_x, max_x)
            y = randint(min_y, max_y)
            sprite = StaticTile(0, x, y, cloud, [])
            self.cloud_sprites.add(sprite)
    
    def draw(self, screen):
        self.cloud_sprites.update()
        self.cloud_sprites.draw(screen)
