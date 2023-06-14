import pygame
from config import game_cfg, video_cfg, gameplay_cfg
from entities import card_helper, board_helper

pygame.init()
pygame.display.set_caption(game_cfg.TITLE)
screen = pygame.display.set_mode((video_cfg.WIDTH, video_cfg.HEIGHT))
clock = pygame.time.Clock()
delta_time = 0
is_running = True

# -------------------------------------------


# -------------------------------------------


# ------- INIT CARDS
cards = card_helper.init_cards()
[print('[' + card.__str__() + ']') for card in cards]

board = board_helper.init_board(screen, cards)

# -------------------------------------------

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('cya 👋')
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            card_helper.on_click_card_collider(screen, cards)

    # game code here

    pygame.display.flip()
    delta_time = clock.tick(video_cfg.FPS) / 1000

pygame.quit()
