import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, FPS
from level import Level
from level_data import ALL_LEVELS
from ui import Score


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_level = 0
        self.level = Level(ALL_LEVELS[self.current_level], self)
        self.win = False

    # FIXME: Do different this
    def change_level(self, new_level_index):
        print(f'Changing level to {new_level_index}')
        self.current_level = new_level_index
        if self.current_level < 0:
            self.current_level = 0
        if self.current_level > len(ALL_LEVELS) - 1:
            self.win = True
            return
        self.level = Level(ALL_LEVELS[self.current_level], self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('grey')
            self.level.run()

            if Score.player_life == -1:
                print(f'No more life, game over')
                pygame.quit()
                sys.exit()
            
            if self.win:
                print(f'No more levels, you win')
                pygame.quit()
                sys.exit()

            Score.draw_player_life(self.screen)
            Score.draw_score(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Game().run()
