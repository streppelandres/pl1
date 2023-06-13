import random
import pygame
from config import game_cfg, video_cfg, gameplay_cfg
from utils import colors

pygame.init()
pygame.display.set_caption(game_cfg.TITLE)
screen = pygame.display.set_mode((video_cfg.WIDTH, video_cfg.HEIGHT))
clock = pygame.time.Clock()
delta_time = 0
is_running = True

# ------- INIT CARDS
cards = []
for _ in range(0, gameplay_cfg.NUMBER_OF_CARDS):
    while True:
        card = colors.get_random_color()
        if not card in cards:
            cards.append(card)
            break

cards = cards + cards # cards duplication
random.shuffle(cards)

#print(cards)

# ------- INIT BOARD
rows = int(len(cards) ** 0.5)
columns = len(cards) // rows

card_width = video_cfg.WIDTH // (gameplay_cfg.NUMBER_OF_CARDS)
card_height = video_cfg.HEIGHT // (gameplay_cfg.NUMBER_OF_CARDS // 1.5)

print(f'card_width -> {card_width}, card_height -> {card_height}')

board = []
index = 0
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(cards[index])
        pygame.draw.rect(screen, cards[index], (i * card_width, j * card_height, card_width, card_height))
        index += 1
    board.append(row)

#print(board)

# -------------------------------------------

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('cya 👋')
            is_running = False

    # game code here

    pygame.display.flip()
    delta_time = clock.tick(video_cfg.FPS) / 1000

pygame.quit()
