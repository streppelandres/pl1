import pygame
from tiles import Tile, AnimatedTile
from settings import ASSETS_GFX_FOLDER, ENEMY_SPEED
from ui import Score


SKELETON_SPRITES = f'{ASSETS_GFX_FOLDER}/enemies/skeleton/run'
KNIGHT_SPRITES = f'{ASSETS_GFX_FOLDER}/enemies/knight/run'
BAT_SPRITES = f'{ASSETS_GFX_FOLDER}/enemies/bat/fly'

class Enemy(AnimatedTile):
    def __init__(self, size, x, y, sprites_folder_path, group, constraints):
        super().__init__(size, x, y, sprites_folder_path, group)
        self.rect.y += size - self.image.get_size()[1]
        self.speed = ENEMY_SPEED
        self.constraints = constraints

    def move(self):
        self.rect.x -= self.speed

    def reverse_img(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def collision_reverse(self):
        for sprite in self.constraints.sprites():
            if sprite.rect.colliderect(self.rect):
                self.reverse()
    
    def kill(self, damage):
        print(f'Damage received: {damage}, score added: {self.score}')
        Score.add_score(self.score)
        super().kill()

    def update(self):
        self.animate()
        self.move()
        self.collision_reverse()
        self.reverse_img()


class SkeletonEnemy(Enemy):
    def __init__(self, size, x, y, group, constraints):
        super().__init__(size, x, y, SKELETON_SPRITES, group, constraints)
        self.score = 10


class KnightEnemy(Enemy):
    def __init__(self, size, x, y, group, constraints):
        super().__init__(size, x, y, KNIGHT_SPRITES, group, constraints)
        self.score = 15


class BatEnemy(Enemy):
    def __init__(self, size, x, y, group, constraints):
        super().__init__(size, x, y, BAT_SPRITES, group, constraints)
        self.score = 20
    
    def move(self):
        self.rect.x += self.speed