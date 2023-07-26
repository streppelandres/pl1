import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# FIXME: Bad naming
class Score:
    global_score = 0
    player_life = 3

    @staticmethod
    def add_score(score):
        Score.global_score += score
    
    @staticmethod
    def draw_score(display_surface):
        font = pygame.font.Font(None, 32)
        text = font.render(f' Total points: {Score.global_score} ', True, 'white', 'black')
        text_rect = text.get_rect()
        text_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        display_surface.blit(text, text_rect)
    
    @staticmethod
    def add_player_life():
        Score.player_life += 1
    
    @staticmethod
    def remove_player_life():
        Score.player_life -= 1

    @staticmethod
    def draw_player_life(display_surface):
        font = pygame.font.Font(None, 32)
        text = font.render(f' Player life: {Score.player_life} ', True, 'red', 'white')
        text_rect = text.get_rect()
        display_surface.blit(text, text_rect)