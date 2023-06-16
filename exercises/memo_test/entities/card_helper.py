import pygame
import random
from config import gameplay_cfg, video_cfg
from utils import colors
from entities.card import Card


def create_cards() -> list[Card]:
    card_width = video_cfg.WIDTH // (gameplay_cfg.NUMBER_OF_CARDS // 2)
    card_height = video_cfg.HEIGHT // (gameplay_cfg.NUMBER_OF_CARDS // 2)
    cards = []
    duplicated_cards = []

    for i in range(0, gameplay_cfg.NUMBER_OF_CARDS):
        while True:
            color = colors.get_random_color()
            card = Card(i+1, color, card_width, card_height)
            if not card in cards:
                cards.append(card)
                # FIXME: copy created, otherwise use the same reference
                duplicated_cards.append(Card(i+1, color, card_width, card_height))
                break

    cards = cards + duplicated_cards
    random.shuffle(cards)

    return cards


def on_click_card_collider(screen, cards: list[Card]):
    mouse_pos = pygame.mouse.get_pos()
    for card in cards:
        if card.rect.collidepoint(mouse_pos):
            print(f'Flipping card {card.number} clicked!')
            card.face_toogle(screen, True)
