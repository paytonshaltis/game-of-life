"""Contains the Game class to create instances of the New Game of Life."""
import pygame, pygame.display, pygame.event, pygame.rect, pygame.draw
import sys, time
from settings import Settings

class Game:
    """An instance of the Game class."""

    def __init__(self):
        """Creates an instance of the Game class"""
        
        # instance variables
        self.settings = None
        self.screen = None
        self.grid = []

        # initialize Pygame 
        pygame.init()

        # create a Settings object
        self.settings = Settings(self)

        # set up the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption('New Game of Life')

        # create the grid
        self._initialize_grid()


    def _initialize_grid(self):
        """
        Initializes the grid on the main screen surface. Stores each Rect
        object into 'self.grid' for use by the class later.
        """
        
        # for each row in the grid
        for y in range(0, self.settings.screen_height, self.settings.square_size):
            
            # clear the 'row' and begin traversing columns
            row = []
            for x in range(0, self.settings.screen_width, self.settings.square_size):
                
                # create a Rect object at (x, y)
                rect = pygame.Rect(
                    x,
                    y,
                    self.settings.square_size,
                    self.settings.square_size
                )

                # store the Rect in a list with its color (current row)
                row.append((rect, self.settings.bg_color))

                # draw the temp Rect with proper settings
                pygame.draw.rect(
                    self.screen, 
                    self.settings.bg_color, 
                    rect,
                )

            # add the current row to the grid instance variable
            self.grid.append(row)


    def _update_grid(self):
        """Updates the grid each for each pass of the main game loop."""
        for row in self.grid:
            for tup in row:
                pygame.draw.rect(
                    self.screen,
                    tup[1],
                    tup[0],
                )


    def _update_borders(self):
        """Updates the borders of the grid for each pass of the main game loop."""
        for i in range(int(self.settings.screen_width / self.settings.square_size)):
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                pygame.Rect(
                    self.settings.square_size * i, 
                    0, 
                    1, 
                    self.settings.screen_height
                )
            )
        for i in range(int(self.settings.screen_height / self.settings.square_size)):
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                pygame.Rect(
                    0,
                    self.settings.square_size * i,
                    self.settings.screen_width,
                    1
                )
            )


    def _toggle_square(self, row, col):
        """Toggles the state of a square at row, col."""
        if self.grid[row][col][1] == self.settings.bg_color:
            self.grid[row][col] = (self.grid[row][col][0], self.settings.square_color)
        else:
            self.grid[row][col] = (self.grid[row][col][0], self.settings.bg_color)


    def run_game(self):
        """The main game loop."""
        while True:
            
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self._toggle_square(10, 10)

            self.screen.fill(self.settings.bg_color)
            self._update_grid()
            self._update_borders()
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()