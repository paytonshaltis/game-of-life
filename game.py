"""Contains the Game class to create instances of the New Game of Life."""
from typing import Tuple
import pygame, pygame.display, pygame.event, pygame.rect, pygame.draw, pygame.mouse
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

        # initialize the grid
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
                # store the Rect in a list with its color (rect, color)
                row.append((rect, self.settings.bg_color))

            # add the current row to the grid instance variable
            self.grid.append(row)


    def _update_grid(self):
        """Updates the grid each for each pass of the main game loop."""
        
        # use the rect and color from each tuple in self.grid
        for row in self.grid:
            for tup in row:
                pygame.draw.rect(
                    self.screen,
                    tup[1],
                    tup[0],
                )


    def _update_borders(self):
        """Updates the borders of the grid for each pass of the main game loop."""

        self._update_vertical_borders()
        self._update_horizontal_borders()


    def _update_vertical_borders(self):
        """Updates the vertical borders on the screen."""  

        # draws the vertical lines on the screen
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
        
    def _update_horizontal_borders(self):
        """Updates the horizontal borders on the screen."""

        # draws the horizontal lines on the screen
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


    def _is_alive(self, row, col):
        """Returns True if the cell at (row, col) is alive."""
        return self.grid[row][col][1] != self.settings.bg_color


    def _total_surround(self, row, col):
        """Returns the total number of living cells surrounding the one at (row, col)."""

        right_pos = int(self.settings.screen_width / self.settings.square_size) - 1
        bottom_pos = int(self.settings.screen_height / self.settings.square_size) - 1
        count = 0

        # deal with the 4 corners
        if row == 0 and col == 0:
            if self._is_alive(0, 1):
                count += 1
            if self._is_alive(1, 1):
                count += 1
            if self._is_alive(1, 0):
                count += 1
        elif row == 0 and col == right_pos:
            if self._is_alive(0, right_pos - 1):
                count += 1
            if self._is_alive(1, right_pos - 1):
                count += 1
            if self._is_alive(1, right_pos):
                count += 1
        elif row == bottom_pos and col == 0:
            if self._is_alive(bottom_pos - 1, 0):
                count += 1
            if self._is_alive(bottom_pos - 1, 1):
                count += 1
            if self._is_alive(bottom_pos, 1):
                count += 1            
        elif row == bottom_pos and col == right_pos:
            if self._is_alive(bottom_pos, right_pos - 1):
                count += 1
            if self._is_alive(bottom_pos - 1, right_pos - 1):
                count += 1
            if self._is_alive(bottom_pos - 1, right_pos):
                count += 1
            
        return count


    def _check_mouse_click(self, mouse_pos):
        """
        Checks to see if a square was clicked with the mouse. The square
        will then be toggled if it happened to be clicked on
        """

        # traverse the entire list of Rect objects
        row_count = 0
        col_count = 0
        
        for row in self.grid:
            
            col_count = 0
            for tup in row:
                # if a mouse point collides with a rectangle, toggle it
                if tup[0].collidepoint(mouse_pos):
                    self._toggle_square(row_count, col_count)
                    return

                col_count += 1
            
            row_count += 1


    def _toggle_square(self, row, col):
        """Toggles the state of a square at row, col."""

        if not self._is_alive(row, col):
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
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        print(
                            'Enter Pressed:',
                            self._total_surround(0, 0),
                            self._total_surround(0, int(self.settings.screen_width / self.settings.square_size) - 1),
                            self._total_surround(int(self.settings.screen_height / self.settings.square_size) - 1, 0),
                            self._total_surround(int(self.settings.screen_height / self.settings.square_size) - 1, int(self.settings.screen_width / self.settings.square_size) - 1),
                        )
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == pygame.BUTTON_LEFT:
                        mouse_pos = pygame.mouse.get_pos()
                        print(mouse_pos)
                        self._check_mouse_click(mouse_pos)

            self.screen.fill(self.settings.bg_color)
            self._update_grid()
            self._update_borders()
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()