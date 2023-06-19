import pygame
from config import gameplay_cfg, video_cfg

# FIXME: No idea where to put these things, so i made this class, maybe i can add more stuff or the core of the game here
class Game:
    def __init__(self) -> None:
        self.last_card_id = None
        self.attempts_left = gameplay_cfg.MAX_ATTEMPTS
        self.SET_FACE_DOWN_CARDS_EVENT = pygame.USEREVENT + 1
        self.enable_card_click = True
        self.miss_count = 0
    
    def draw_misses_text(self, screen):
        font = pygame.font.Font(None, 32)
        text = font.render(f' Misses: {self.miss_count} ', True, 'white', 'black')
        textRect = text.get_rect()
        textRect.bottomright = (video_cfg.WIDTH - 20, video_cfg.HEIGHT - 20)
        screen.blit(text, textRect)