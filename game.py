"""Contains the Game class to create instances of the New Game of Life."""
import pygame, pygame.display, pygame.event, pygame.rect, pygame.draw
import sys
from settings import Settings

class Game:
    """An instance of the Game class."""

    def __init__(self):
        """Creates an instance of the Game class"""
        
        # instance variables
        self.settings = None
        self.screen = None
        
        # initialize Pygame 
        pygame.init()

        # create a Settings object
        self.settings = Settings(self)

        # set up the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption('New Game of Life')

        # create the grid
        self._draw_grid()
        
    def _draw_grid(self):
        """Draws the grid on the main screen surface."""
        
        for x in range(self.settings.screen_width):
            for y in range(self.settings.screen_height):
                
                # create a temporary Rect to be drawn
                rect = pygame.Rect(
                    x * self.settings.square_size,
                    y * self.settings.square_size,
                    self.settings.square_size,
                    self.settings.square_size
                )

                # draw the temp Rect with proper settings
                pygame.draw.rect(
                    self.screen, 
                    self.settings.square_color, 
                    rect, 
                    self.settings.square_bord_thick
                )



        

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