import pygame
from config import game_cfg, video_cfg, gameplay_cfg
from entities import card_helper, board_helper
from entities.game import Game

pygame.init()
pygame.display.set_caption(game_cfg.TITLE)
screen = pygame.display.set_mode((video_cfg.WIDTH, video_cfg.HEIGHT))
clock = pygame.time.Clock()
delta_time = 0
is_running = True

game = Game()

cards = card_helper.create_cards()
board = board_helper.create_board_with_cards(screen, cards)

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('cya 👋')
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game.enable_card_click:
            card_helper.on_click_card_collider(screen, cards, game)
        elif event.type == game.SAME_CARDS_CLICKED:
            [card.set_inactive(screen) for card in event.cards]
            pygame.time.set_timer(game.SAME_CARDS_CLICKED, 0)
            game.enable_card_click = True
            game.discovered_cards += 1
        elif event.type == game.DIFFERENT_CARDS_CLICKED:
            [card.face_toogle(screen, False) for card in event.cards]
            pygame.time.set_timer(game.DIFFERENT_CARDS_CLICKED, 0)
            game.enable_card_click = True

    if game.discovered_cards == gameplay_cfg.NUMBER_OF_CARDS:
        # TODO: Make a win screen or some succes message
        print(f'All cards discovered in {game.miss_count} tries, ending game!')
        is_running = False
    
    game.draw_misses_text(screen)

    pygame.display.flip()
    delta_time = clock.tick(video_cfg.FPS) / 1000

pygame.quit()
