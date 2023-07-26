import enum
import pygame
from settings import PlayerControls, PLAYER_SPEED, PLAYER_GRAVITY, PLAYER_JUMP_SPEED, PLAYER_ANIMATION_SPEED
from utils import import_image_folder
from player_belt import PlayerBeltGroup
from items import Chest, Coin
from level_data import LEVEL_0
from ui import Score

class PlayerStatus(enum.Enum):
    IDLE = 'idle'
    RUN = 'run'
    JUMP = 'jump'
    FALL = 'fall'


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites, enemies_sprites, breakable_sprites, interactable_sprites, game):
        super().__init__(groups)
        self.import_gfx()
        self.frame_index = 0
        self.animation_speed = PLAYER_ANIMATION_SPEED
        self.image = self.animations[PlayerStatus.IDLE][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        self.screen = pygame.display.get_surface()
        self.obstacle_sprites = obstacle_sprites
        self.enemies_sprites = enemies_sprites
        self.breakable_sprites = breakable_sprites
        self.interactable_sprites = interactable_sprites

        self.current_x = 0

        # Movement:
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.gravity = PLAYER_GRAVITY
        self.jump_speed = PLAYER_JUMP_SPEED

        self.status = PlayerStatus.IDLE
        # FIXME: These booleans
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_right = False
        self.on_left = False

        self.belt = PlayerBeltGroup(position, groups, self)
        self.game = game


    def import_gfx(self):
        asset_path = './assets/gfx/player/'
        # keys must be the same name as the sprites folder
        self.animations = { PlayerStatus.IDLE: [], PlayerStatus.RUN: [],
                           PlayerStatus.JUMP: [], PlayerStatus.FALL: [] }
        for animation in self.animations.keys():
            full_path = asset_path + animation.value
            self.animations[animation] = import_image_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[PlayerControls.RIGHT.value]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[PlayerControls.LEFT.value]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[PlayerControls.UP.value] and self.on_ground:
            self.jump()
        
        if keys[PlayerControls.INTERACT.value]:
            self.interact()

    def jump(self):
        self.direction.y = self.jump_speed

    def move(self):
        self.rect.x += self.direction.x * self.speed

    def get_status(self):
        if self.direction.y < 0:
            self.status = PlayerStatus.JUMP
        elif self.direction.y > 1:  # must be greater than gravity
            self.status = PlayerStatus.FALL
        else:
            if self.direction.x != 0:
                self.status = PlayerStatus.RUN
            else:
                self.status = PlayerStatus.IDLE

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def x_collission(self):
        player = self
        player.move()

        # TODO: Use '+' to add more sprites to detect collision
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                # Check where the player is looking, if is moving left or right
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False

    def y_collission(self):
        player = self
        player.apply_gravity()

        # TODO: Use '+' to add more sprites to detect collision
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ciling = False
    
    def interact(self):
        for thing in self.interactable_sprites.sprites():
            if thing.rect.colliderect(self.rect):
                print('Interacting with: ', thing)
                if isinstance(thing, Chest):
                    print('Level wining')
                    # FIXME: Do other stuff
                    self.game.change_level(self.game.current_level + 1)
                if isinstance(thing, Coin):
                    print('Coing picked')
                    # TODO: Add points
                thing.kill()

    def enemies_collide(self):
        for thing in self.enemies_sprites.sprites():
            if thing.rect.colliderect(self.rect):
                print('Touched by a enemy')
                Score.remove_player_life()
                self.game.change_level(self.game.current_level - 1)

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.x_collission()
        self.y_collission()
        self.belt.update(self)
        self.enemies_collide()