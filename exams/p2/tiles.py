import pygame
from utils import import_image_folder
from settings import DEFAULT_ANIMATION_SPEED


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.visible = True

    def hide(self):
        self.image.set_alpha(0)
        self.visible = False
    
    def show(self):
        self.image.set_alpha(255)
        self.visible = True

class AnimatedTile(Tile):
    def __init__(self, size, x, y, path, group, animation_speed=DEFAULT_ANIMATION_SPEED):
        super().__init__(size, x, y, group)
        self.frames = import_image_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.animation_speed = animation_speed

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()


class StaticTile(Tile):
    def __init__(self, size, x, y, surface, group):
        super().__init__(size, x, y, group)
        self.image = surface