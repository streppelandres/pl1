import pygame
import random
from config import gameplay_cfg, video_cfg
from utils import colors
from entities.card import Card


def init_cards() -> list:
    cards = []
    cards_copy = []

    for i in range(0, gameplay_cfg.NUMBER_OF_CARDS):
        while True:
            card = Card(number=i+1, color=colors.get_random_color())
            if not card in cards:
                cards.append(card)
                # FIXME: copy created, otherwise use the same reference
                cards_copy.append(Card(number=i+1, color=card.color))
                break

    cards = cards + cards_copy  # cards duplication
    random.shuffle(cards)

    return cards


def draw_card(screen, card:Card, x, y) -> Card:
    card_width = video_cfg.WIDTH // (gameplay_cfg.NUMBER_OF_CARDS)
    card_height = video_cfg.HEIGHT // (gameplay_cfg.NUMBER_OF_CARDS // 1.5)
    card_x_pos = x * card_width
    card_y_pos = y * card_height

    # saving rect for collitions
    card.rect = pygame.draw.rect(screen, card.color, (card_x_pos, card_y_pos, card_width, card_height))
    pygame.draw.rect(screen, colors.WHITE, (card_x_pos, card_y_pos, card_width, card_height), 3)

    text = pygame.font.Font(None, 48).render(str(card.number), True, colors.WHITE)
    text_rect = text.get_rect(center=(card_x_pos + 50, card_y_pos + 60)) # FIXME: More dynamic

    screen.blit(text, text_rect)

def on_click_card_collider(cards:list):
    mouse_pos = pygame.mouse.get_pos()
    for card in cards:
        if card.rect.collidepoint(mouse_pos):
            print(f'Card {card.number} clicked!')