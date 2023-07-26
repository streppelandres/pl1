import pygame
from settings import TILE_SIZE
from weapons import Sword, Bow, Pickaxe


class PlayerBeltGroup(pygame.sprite.Group):
    def __init__(self, position, groups, player):
        super().__init__()
        self.slots = {
            pygame.K_1: Sword(TILE_SIZE, position[0], position[1], groups, player),
            pygame.K_2: Bow(TILE_SIZE, position[0], position[1], groups, player),
            pygame.K_3: Pickaxe(TILE_SIZE, position[0], position[1], groups, player)
        }
        [self.add(self.slots[item]) for item in self.slots]
        self.current_item = None

    def update(self, player):
        keys = pygame.key.get_pressed()

        for key, item in self.slots.items():
            if keys[key]:
                if self.current_item:
                    self.current_item.hide()
                self.current_item = item
                self.current_item.show()
                break