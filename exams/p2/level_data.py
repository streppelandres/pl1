import enum

LEVELS_FOLDER = './levels'

# Layouts keys
class LayoutKey(enum.Enum):
    ENEMIES_CONSTRAINTS = 'enemies_constraints'
    TERRAIN_BG = 'terrain_bg'
    BUSHES = 'bushes'
    COINS_GOLD = 'coins_gold'
    COINS_SILVER = 'coins_silver'
    CRATES = 'crates'
    ENEMIES_BAT = 'enemies_bat'
    ENEMIES_KNIGHT = 'enemies_knight'
    ENEMIES_SKELETON = 'enemies_skeleton'
    FLOWERS = 'flowers'
    GRASS = 'grass'
    STONES = 'stones'
    TREES = 'trees'
    TERRAIN = 'terrain'
    VINES = 'vines'
    WATER = 'water'
    CHEST_WIN_BG = 'chest_win_bg'
    CHEST_WIN = 'chest_win'
    CHEST_WIN_FRONT = 'chest_win_front'
    PLAYER = 'player'


LEVEL_0 = {
    LayoutKey.BUSHES: f'{LEVELS_FOLDER}/0/level_0_bushes.csv',
    LayoutKey.CHEST_WIN: f'{LEVELS_FOLDER}/0/level_0_chest_win.csv',
    LayoutKey.CHEST_WIN_BG: f'{LEVELS_FOLDER}/0/level_0_chest_win_bg.csv',
    LayoutKey.CHEST_WIN_FRONT: f'{LEVELS_FOLDER}/0/level_0_chest_win_front.csv',
    LayoutKey.COINS_GOLD: f'{LEVELS_FOLDER}/0/level_0_coins_gold.csv',
    LayoutKey.COINS_SILVER: f'{LEVELS_FOLDER}/0/level_0_coins_silver.csv',
    LayoutKey.CRATES: f'{LEVELS_FOLDER}/0/level_0_crates.csv',
    LayoutKey.ENEMIES_BAT: f'{LEVELS_FOLDER}/0/level_0_enemies_bat.csv',
    LayoutKey.ENEMIES_CONSTRAINTS: f'{LEVELS_FOLDER}/0/level_0_enemies_constraints.csv',
    LayoutKey.ENEMIES_KNIGHT: f'{LEVELS_FOLDER}/0/level_0_enemies_knight.csv',
    LayoutKey.ENEMIES_SKELETON: f'{LEVELS_FOLDER}/0/level_0_enemies_skeleton.csv',
    LayoutKey.FLOWERS: f'{LEVELS_FOLDER}/0/level_0_flowers.csv',
    LayoutKey.GRASS: f'{LEVELS_FOLDER}/0/level_0_grass.csv',
    LayoutKey.PLAYER: f'{LEVELS_FOLDER}/0/level_0_player.csv',
    LayoutKey.STONES: f'{LEVELS_FOLDER}/0/level_0_stones.csv',
    LayoutKey.TERRAIN: f'{LEVELS_FOLDER}/0/level_0_terrain.csv',
    LayoutKey.TERRAIN_BG: f'{LEVELS_FOLDER}/0/level_0_terrain_bg.csv',
    LayoutKey.TREES: f'{LEVELS_FOLDER}/0/level_0_trees.csv',
    LayoutKey.VINES: f'{LEVELS_FOLDER}/0/level_0_vines.csv',
    LayoutKey.WATER: f'{LEVELS_FOLDER}/0/level_0_water.csv',
}

LEVEL_1 = {
    LayoutKey.BUSHES: f'{LEVELS_FOLDER}/1/level_1_bushes.csv',
    LayoutKey.CHEST_WIN: f'{LEVELS_FOLDER}/1/level_1_chest_win.csv',
    LayoutKey.CHEST_WIN_BG: f'{LEVELS_FOLDER}/1/level_1_chest_win_bg.csv',
    LayoutKey.CHEST_WIN_FRONT: f'{LEVELS_FOLDER}/1/level_1_chest_win_front.csv',
    LayoutKey.COINS_GOLD: f'{LEVELS_FOLDER}/1/level_1_coins_gold.csv',
    LayoutKey.COINS_SILVER: f'{LEVELS_FOLDER}/1/level_1_coins_silver.csv',
    LayoutKey.CRATES: f'{LEVELS_FOLDER}/1/level_1_crates.csv',
    LayoutKey.ENEMIES_BAT: f'{LEVELS_FOLDER}/1/level_1_enemies_bat.csv',
    LayoutKey.ENEMIES_CONSTRAINTS: f'{LEVELS_FOLDER}/1/level_1_enemies_constraints.csv',
    LayoutKey.ENEMIES_KNIGHT: f'{LEVELS_FOLDER}/1/level_1_enemies_knight.csv',
    LayoutKey.ENEMIES_SKELETON: f'{LEVELS_FOLDER}/1/level_1_enemies_skeleton.csv',
    LayoutKey.FLOWERS: f'{LEVELS_FOLDER}/1/level_1_flowers.csv',
    LayoutKey.GRASS: f'{LEVELS_FOLDER}/1/level_1_grass.csv',
    LayoutKey.PLAYER: f'{LEVELS_FOLDER}/1/level_1_player.csv',
    LayoutKey.STONES: f'{LEVELS_FOLDER}/1/level_1_stones.csv',
    LayoutKey.TERRAIN: f'{LEVELS_FOLDER}/1/level_1_terrain.csv',
    LayoutKey.TERRAIN_BG: f'{LEVELS_FOLDER}/1/level_1_terrain_bg.csv',
    LayoutKey.TREES: f'{LEVELS_FOLDER}/1/level_1_trees.csv',
    LayoutKey.VINES: f'{LEVELS_FOLDER}/1/level_1_vines.csv',
    LayoutKey.WATER: f'{LEVELS_FOLDER}/1/level_1_water.csv',
}

ALL_LEVELS = [
    LEVEL_0,
    LEVEL_1
]