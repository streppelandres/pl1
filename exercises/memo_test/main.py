import pygame
from config import game_cfg, video_cfg
from utils import colors

pygame.init()
pygame.display.set_caption(game_cfg.TITLE)
screen = pygame.display.set_mode((video_cfg.WIDTH, video_cfg.HEIGHT))
clock = pygame.time.Clock()
delta_time = 0
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('cya 👋')
            is_running = False

    screen.fill(colors.BLACK)

    # tutururu

    pygame.display.flip()
    delta_time = clock.tick(video_cfg.FPS) / 1000

pygame.quit()
