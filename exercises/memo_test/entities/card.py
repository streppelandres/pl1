import pygame
from config import gameplay_cfg
from utils import colors


class Card(pygame.sprite.Sprite):
    def __init__(self, number: int, color: tuple, width: float, height: float):
        super().__init__()
        self.number = number
        self.color = color
        self.flipped = False
        self.surface = pygame.Surface([width, height])
        self.surface.fill(gameplay_cfg.FLIPPED_CARD_COLOR)
        self.rect = self.surface.get_rect()

    def set_position(self, x: float, y: float):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def face_toogle(self, screen, toggle=True):
        if toggle:
            self.__face_up(screen)
        else:
            self.__face_down(screen)

    def __face_up(self, screen):
        self.surface.fill(self.color)
        self.flipped = True
        self.__draw_txt(str(self.number))
        self.draw(screen)

    def __face_down(self, screen):
        self.surface.fill(gameplay_cfg.FLIPPED_CARD_COLOR)
        self.flipped = False
        self.__draw_txt(gameplay_cfg.FLIPPED_CARD_TXT)
        self.draw(screen)

    def __draw_txt(self, txt: str):
        # TODO: Move something to a utils
        font = pygame.font.Font(None, 36)
        text_surface = font.render(txt, True, colors.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.rect.w // 2, self.rect.h // 2)
        self.surface.blit(text_surface, text_rect)
