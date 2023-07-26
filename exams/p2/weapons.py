from items import ChestCoverBlock
import pygame, math, time
from tiles import AnimatedTile, StaticTile
from settings import ASSETS_GFX_FOLDER, PLAYER_ARROW_SPEED, PLAYER_BOW_CD, TILE_SIZE, PLAYER_ARROW_DAMAGE, PLAYER_MELEE_DAMAGE
from utils import import_image
from enemy import Enemy

SWORD_SPRITE = f'{ASSETS_GFX_FOLDER}/items/weapons/sword'
BOW_SPRITE = f'{ASSETS_GFX_FOLDER}/items/weapons/bow'
PICKAXE_SPRITE = f'{ASSETS_GFX_FOLDER}/items/tools/pickaxe'
ARROW_SPRITE = f'{ASSETS_GFX_FOLDER}/items/weapons/arrow.png'
MELEE_SLASH_SPRITE = f'{ASSETS_GFX_FOLDER}/effects/melee_slash'

# FIXME: Change nama to something more generic for tools and weapons at same time
class Weapon(AnimatedTile):
    def __init__(self, size, x, y, sprite, group, player):
        super().__init__(size, x, y, sprite, group)
        self.group = group
        self.hide()
        self.player = player
        self.offset_x = 43
        self.offset_y = 0
        self.damage = 5
        self.melee_slash = None
        self.can_dash = True
        self.dash_cooldown = 2
        self.last_dash_time = 0

    def flip(self):
        if self.player.facing_right:
            self.rect.x = self.player.rect.x + self.offset_x
            self.rect.y = self.player.rect.y + self.offset_y
        else:
            self.rect.x = self.player.rect.x - self.offset_x
            self.rect.y = self.player.rect.y - self.offset_y

    def get_input(self):
        if pygame.mouse.get_pressed()[0] and self.visible:
            self.attack()

    def attack(self):
        if self.can_dash:
            print('Melee attack!')
            colliable_sprites = self.player.enemies_sprites.sprites() + self.player.breakable_sprites.sprites()
            is_from_pickaxe = isinstance(self.player.belt.current_item, Pickaxe)
            offset_x = self.rect.x + 30
            if not self.player.facing_right:
                offset_x = self.rect.x - 30
            self.melee_slash = MeleeSlash(TILE_SIZE, offset_x, self.rect.y, self.group, colliable_sprites, is_from_pickaxe)
            self.can_dash = False
            self.last_dash_time = time.time()

    def update(self):
        self.flip()
        self.get_input()

        if not self.can_dash:
            current_time = time.time()
            elapsed_time = current_time - self.last_dash_time

            if elapsed_time >= self.dash_cooldown:
                self.can_dash = True


class Sword(Weapon):
    def __init__(self, size, x, y, group, player):
        super().__init__(size, x, y, SWORD_SPRITE, group, player)


class Bow(Weapon):
    def __init__(self, size, x, y, group, player):
        super().__init__(size, x, y, BOW_SPRITE, group, player)
        self.bullets = pygame.sprite.Group()
        self.cooldown = 0
    
    # TODO: Bow animation
    def attack(self):
        current_time = time.time()
        if self.cooldown < current_time:
            mouse_pos = pygame.mouse.get_pos()
            direction = math.atan2(mouse_pos[1] - self.rect.centery, mouse_pos[0] - self.rect.centerx)
            self.bullets.add(Arrow(self.rect.centerx, self.rect.centery, direction, self.group, self.player.enemies_sprites.sprites() + self.player.obstacle_sprites.sprites()))
            self.cooldown = current_time + PLAYER_BOW_CD
        else:
            # TODO: Do something, a sound or animation
            print('Bow cooldown')

    def update(self):
        super().update()
        self.bullets.update()
        self.bullets.draw(self.player.screen)


class Pickaxe(Weapon):
    def __init__(self, size, x, y, group, player):
        super().__init__(size, x, y, PICKAXE_SPRITE, group, player)

# TODO: Add fall gravity
# FIXME: Big arrow rect
class Arrow(StaticTile):
    def __init__(self, x, y, direction, group, collidable_sprites):
        super().__init__(TILE_SIZE, x, y, import_image(ARROW_SPRITE), group)
        self.group = group
        self.rect.center = (x, y)
        self.direction = direction
        self.speed = PLAYER_ARROW_SPEED
        self.angle = math.degrees(direction)
        self.image_original = self.image.copy()
        self.collidable_sprites = collidable_sprites
        self.damage = PLAYER_ARROW_DAMAGE

    def update(self):
        self.image = pygame.transform.rotate(self.image_original, -self.angle)
        self.rect.x += math.cos(self.direction) * self.speed
        self.rect.y += math.sin(self.direction) * self.speed

        # Esto podes hacer que sea una funcion del padre quizas
        sprites_hit = pygame.sprite.spritecollide(self, self.collidable_sprites, False)
        if sprites_hit:
            for thing in sprites_hit:
                if isinstance(thing, Enemy) and self.speed > 0:
                    thing.kill(self.damage)
                    self.kill()
                else:
                    self.speed = 0

# FIXME: Semitransparent pixels from the sprite
class MeleeSlash(AnimatedTile):
    def __init__(self, size, x, y, group, collidable_sprites, is_from_pickaxe):
        super().__init__(size, x, y, MELEE_SLASH_SPRITE, group, 0.2)
        self.collidable_sprites = collidable_sprites
        self.damage = PLAYER_MELEE_DAMAGE
        self.duration = 0.3
        self.start_time = time.time()
        self.is_from_pickaxe = is_from_pickaxe

    def update(self):
        super().update()
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        sprites_hit = pygame.sprite.spritecollide(self, self.collidable_sprites, False)
        if sprites_hit:
            for thing in sprites_hit:
                if isinstance(thing, Enemy):
                    thing.kill(self.damage)
                elif isinstance(thing, ChestCoverBlock) and self.is_from_pickaxe:
                    thing.kill()
        
        if elapsed_time >= self.duration:
            self.kill()
            return