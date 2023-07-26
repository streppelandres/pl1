import pygame
from os import walk
from csv import reader
from settings import TILE_SIZE, CURRENT_SPRITESHEET_TILE_SIZE


def import_image(path, scaled_size=(TILE_SIZE, TILE_SIZE)):
    img_surface = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img_surface, scaled_size)


def import_image_folder(path, scaled_size=(TILE_SIZE, TILE_SIZE)):
    surfaces = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            surfaces.append(import_image(full_path, scaled_size))
    return surfaces


def import_csv_layout(level_data_path):
    terrain_map = []
    with open(level_data_path) as level_map:
        level = reader(level_map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map


def import_and_slice_gfx_tiles(path, sheet_tile_size=CURRENT_SPRITESHEET_TILE_SIZE):
    '''Loads a spritesheet image, slice and returns them'''
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / sheet_tile_size)
    tile_num_y = int(surface.get_size()[1] / sheet_tile_size)

    cuted_tiles = []
    for row in range(tile_num_x):
        for col in range(tile_num_y):
            x, y = col * sheet_tile_size, row * sheet_tile_size
            new_surface = pygame.Surface((sheet_tile_size, sheet_tile_size), flags = pygame.SRCALPHA)
            # Cuts a slice of the image tile:
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, sheet_tile_size, sheet_tile_size))
            new_surface = pygame.transform.scale(new_surface, (TILE_SIZE, TILE_SIZE))
            cuted_tiles.append(new_surface)

    return cuted_tiles