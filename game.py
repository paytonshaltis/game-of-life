"""Contains the Game class to create instances of the New Game of Life."""
import pygame, pygame.display, pygame.event, pygame.rect
import sys
from settings import Settings

class Game:
    """An instance of the Game class."""
    
    def __init__(self):
        """Creates an instance of the Game class"""
        pygame.init()

        # create a Settings object
        self.settings = Settings(self)

        # set up the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('New Game of Life')

    def run_game(self):
        """The main game loop."""
        while True:
            
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # flip to the newest screen
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run_game()