import pygame
from config import gameplay_cfg

class Card(pygame.sprite.Sprite):
    def __init__(self, number: int, color: tuple):
        super().__init__()
        self.number = number
        self.color = color
        self.flipped = False

    def set_surface(self, width: float, height: float, x: float, y: float):
        self.surface = pygame.Surface([width, height])
        self.surface.fill(gameplay_cfg.FLIPPED_CARD_COLOR)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, screen):
        screen.blit(self.surface, self.rect)
    
    def flip(self, screen):
        self.surface.fill(self.color)
        self.flipped = True
        self.draw(screen)

    def __str__(self):
        return ''.join([
            f'Number: {self.number} ',
            f'Color: {self.color} ',
            f'Flipped: {self.flipped}'
        ])
