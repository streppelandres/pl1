import pygame
from config import gameplay_cfg
from utils import colors

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
        self.__draw_txt()
        self.draw(screen)
    
    def __draw_txt(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(self.number), True, colors.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.rect.w // 2, self.rect.h // 2)
        self.surface.blit(text_surface, text_rect)

    def __str__(self):
        return ''.join([
            f'Number: {self.number} ',
            f'Color: {self.color} ',
            f'Flipped: {self.flipped}'
        ])
