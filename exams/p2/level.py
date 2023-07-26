import pygame
from tiles import Tile, StaticTile
from player import Player
from settings import TILE_SIZE, SPRITESHEET_PATH, SCREEN_HEIGHT
from utils import import_csv_layout, import_and_slice_gfx_tiles
from level_data import LayoutKey
from enemy import SkeletonEnemy, KnightEnemy, BatEnemy
from items import GoldCoin, SilverCoin, Chest, ChestCoverBlock
from camera import CameraGroup
from decorations import Sky, Clouds


class Level:
    def __init__(self, level_map, game):
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_constraint_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.breakable_sprites = pygame.sprite.Group()
        self.interactable_sprites = pygame.sprite.Group()

        self.game = game
        self.setup_layouts(level_map)

        self.sky = Sky(8)
        level_width = len(self.obstacle_sprites) * TILE_SIZE
        self.clouds = Clouds(400, level_width, 20)

    def setup_layouts(self, level_map):
        self.level_map = level_map
        self.all_gfx_tiles = import_and_slice_gfx_tiles(SPRITESHEET_PATH)

        for layout in LayoutKey:
            self.load_layout(import_csv_layout(self.level_map[layout]), layout)


    def load_layout(self, layout_data, tile_type):
        for row_index, row in enumerate(layout_data):
            for col_index, cell in enumerate(row):
                x = TILE_SIZE * col_index
                y = TILE_SIZE * row_index
            
                if cell == '-1': continue

                tile_gfx = self.all_gfx_tiles[int(cell)]

                if cell == '196':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites, self.enemies_sprites, self.breakable_sprites, self.interactable_sprites, self.game)

                elif tile_type == LayoutKey.TERRAIN:
                    StaticTile(TILE_SIZE, x, y, tile_gfx, [self.visible_sprites, self.obstacle_sprites])
                elif tile_type in [LayoutKey.TERRAIN_BG, LayoutKey.GRASS, LayoutKey.BUSHES, LayoutKey.TREES,
                        LayoutKey.FLOWERS, LayoutKey.VINES, LayoutKey.WATER, LayoutKey.STONES,
                        LayoutKey.CRATES, LayoutKey.CHEST_WIN_BG, LayoutKey.TERRAIN_BG]:
                    StaticTile(TILE_SIZE, x, y, tile_gfx, [self.visible_sprites])

                # TODO: Create a enemy factory
                elif tile_type == LayoutKey.ENEMIES_CONSTRAINTS:
                    Tile(TILE_SIZE, x, y, [self.visible_sprites, self.enemy_constraint_sprites])
                elif tile_type == LayoutKey.ENEMIES_SKELETON:
                    SkeletonEnemy(TILE_SIZE, x, y, [self.visible_sprites, self.enemies_sprites], self.enemy_constraint_sprites)
                elif tile_type == LayoutKey.ENEMIES_KNIGHT:
                    KnightEnemy(TILE_SIZE, x, y, [self.visible_sprites, self.enemies_sprites], self.enemy_constraint_sprites)
                elif tile_type == LayoutKey.ENEMIES_BAT:
                    BatEnemy(TILE_SIZE, x, y, [self.visible_sprites, self.enemies_sprites], self.enemy_constraint_sprites)
                
                # Coins
                elif tile_type == LayoutKey.COINS_GOLD:
                    GoldCoin(TILE_SIZE, x, y, [self.visible_sprites, self.interactable_sprites])
                elif tile_type == LayoutKey.COINS_SILVER:
                    SilverCoin(TILE_SIZE, x, y, [self.visible_sprites, self.interactable_sprites])

                # Chest win
                elif tile_type == LayoutKey.CHEST_WIN:
                    Chest(TILE_SIZE, x, y, [self.visible_sprites, self.interactable_sprites])
                elif tile_type == LayoutKey.CHEST_WIN_FRONT:
                    ChestCoverBlock(TILE_SIZE, x, y, tile_gfx, [self.visible_sprites, self.obstacle_sprites, self.breakable_sprites])

    def run(self):
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()