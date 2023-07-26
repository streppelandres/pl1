import pygame
from tiles import AnimatedTile, StaticTile
from settings import ASSETS_GFX_FOLDER
from ui import Score

GOLD_COIN_SPRITES = f'{ASSETS_GFX_FOLDER}/misc/coins/gold'
SILVER_COIN_SPRITES = f'{ASSETS_GFX_FOLDER}/misc/coins/silver'
CHEST_SPRITES = f'{ASSETS_GFX_FOLDER}/misc/chest'


class Coin(AnimatedTile):
    def __init__(self, size, x, y, sprite_path, group):
        super().__init__(size, x, y, sprite_path, group)
    
    def kill(self):
        print(f'Picking coin and killing from parent class')
        Score.add_score(self.score)
        super().kill()

class GoldCoin(Coin):
    def __init__(self, size, x, y, group):
        super().__init__(size, x, y, GOLD_COIN_SPRITES, group)
        self.score = 5

class SilverCoin(Coin):
    def __init__(self, size, x, y, group):
        super().__init__(size, x, y, SILVER_COIN_SPRITES, group)
        self.score = 10

class Chest(AnimatedTile):
    def __init__(self, size, x, y, group):
        super().__init__(size, x, y, CHEST_SPRITES, group)
    
    def animate(self):
        # TODO: Make open chest animation
        pass

# TODO: Usea animated tile
class ChestCoverBlock(StaticTile):
    def __init__(self, size, x, y, tile_gfx, group):
        super().__init__(size, x, y, tile_gfx, group)
    
    def kill(self):
        print(f'Block destroyed')
        Score.add_score(5)
        super().kill()