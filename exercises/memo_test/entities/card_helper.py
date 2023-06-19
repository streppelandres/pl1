import pygame
import random
from config import gameplay_cfg, video_cfg
from utils import colors
from entities.card import Card
from entities.game import Game


def create_cards() -> list[Card]:
    card_width = video_cfg.WIDTH // (gameplay_cfg.NUMBER_OF_CARDS // 2)
    card_height = video_cfg.HEIGHT // (gameplay_cfg.NUMBER_OF_CARDS // 2)
    cards, duplicated_cards = [], []

    for i in range(0, gameplay_cfg.NUMBER_OF_CARDS):
        while True:
            color = colors.get_random_color()
            card = Card(i+1, color, card_width, card_height)
            if not card in cards:
                cards.append(card)
                # FIXME: copy created, otherwise use the same reference
                duplicated_cards.append(
                    Card(i+1, color, card_width, card_height))
                break

    cards = cards + duplicated_cards
    random.shuffle(cards)

    return cards

#TODO:
# - Verify when the same card is clicked
# - FIXME: Show the second card clicked
# - Discount one attempt in failed case
# - Win the game when is no more card to be clicked
# - Lose the game when is no more attempts
def on_click_card_collider(screen, cards: list[Card], game: Game):
    mouse_pos = pygame.mouse.get_pos()
    for card in cards:
        if card.rect.collidepoint(mouse_pos): #and not card.disabled:
            print(f'Card {card.number} clicked!')
            
            if id(card) == game.last_card_id:
                print('Clicking the same card...')
                return

            if card.disabled:
                print('The clicked card is disabled')
                return

            card.face_toogle(screen, True)

            if not game.last_card_id:
                print('There is not last saved card')
                game.last_card_id = id(card)
                return

            last_card = get_card_by_id(cards, game.last_card_id)
            if last_card.number == card.number:
                print('Good! Same cards clicked, they are inactive now')
                game.enable_card_click = False
                # FIXME: Find a better solution for these cards param
                pygame.time.set_timer(pygame.event.Event(game.SAME_CARDS_CLICKED, cards=[card, last_card]), gameplay_cfg.SAME_CARDS_TIME)
            else:
                print('Bad! The cards are differents')
                game.miss_count += 1
                game.enable_card_click = False
                # FIXME: Find a better solution for these cards param
                pygame.time.set_timer(pygame.event.Event(game.DIFFERENT_CARDS_CLICKED, cards=[card, last_card]), gameplay_cfg.DIFFERENT_CARDS_TIME)
                
            
            game.last_card_id = None


def get_card_by_id(cards:list[Card], card_id:int):
    return [card for card in cards if id(card) == card_id][0]