import pygame
from weapons import Weapon, MeleeSlash
from settings import DEBUG

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            sprite.rect.x -= self.offset.x
            sprite.rect.y -= self.offset.y

            if not isinstance(sprite, Weapon) and not isinstance(sprite, MeleeSlash):
                if DEBUG: pygame.draw.rect(self.display_surface, 'blue', sprite.rect, 1)
                self.display_surface.blit(sprite.image, sprite.rect.topleft)
            else:
                flipped_img = pygame.transform.flip(sprite.image, not player.facing_right, False)
                if DEBUG: pygame.draw.rect(self.display_surface, 'red', sprite.rect, 1)
                self.display_surface.blit(flipped_img, (sprite.rect.x, sprite.rect.y))