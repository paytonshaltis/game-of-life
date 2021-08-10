"""Contains the Game class to create instances of the New Game of Life."""
import pygame, pygame.display, pygame.event, pygame.rect, pygame.draw, pygame.mouse, pygame.surface
import sys, time
from settings import Settings
from menu import Menu

class Game:
    """An instance of the Game class."""

    def __init__(self):
        """Creates an instance of the Game class"""
        
        # instance variables
        self.settings = None
        self.menu = None
        self.screen = None
        self.grid = []
        self.grid_copy = []
        self.simulation_running = False
        self.in_menu = False

        # create a Settings object
        self.settings = Settings(self)

        # check the dimensions & square size
        if not self._check_dimensions():
            print('Invalid dimensions!')
            sys.exit()

        # initialize Pygame 
        pygame.init()

        # set up the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption('New Game of Life')

        # create a Menu object
        self.menu = Menu(self)

        # initialize the grid
        self._initialize_grid()


    def _check_dimensions(self):
        """
        Makes sure that both the height and width are evenly
        divisible by the size of the square. Returns True if so.
        """
        return not (
            self.settings.screen_width % self.settings.square_size or
            self.settings.screen_height % self.settings.square_size)


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


    def _update_vertical_borders(self):
        """Updates the vertical borders on the screen."""  

        # draws the vertical lines on the screen
        for i in range(int(self.settings.screen_width / self.settings.square_size)):
            pygame.draw.rect(
                self.screen,
                self.settings.border_color,
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
                self.settings.border_color,
                pygame.Rect(
                    0,
                    self.settings.square_size * i,
                    self.settings.screen_width,
                    1
                )
            )


    def _update_borders(self):
        """Updates the borders of the grid for each pass of the main game loop."""

        self._update_vertical_borders()
        self._update_horizontal_borders()


    def _is_alive(self, row, col):
        """Returns True if the cell at (row, col) is alive."""
        return self.grid[row][col][1] != self.settings.bg_color


    def _get_next_generation(self, current_gen):
        """Returns a new List containing the next generation of cells."""

        # variables used and returned
        next_gen = []
        current_row = []
        row_count = 0
        col_count = 0

        # traverse through each cell and follow Conway's rules
        for row in current_gen:

            current_row = []
            col_count = 0
            for tup in row:
                
                # if the cell is alive
                if self._is_alive(row_count, col_count):
                    
                    # dies from not enough or too many surrounding cells
                    if self._total_surround(row_count, col_count) < 2 or self._total_surround(row_count, col_count) > 3:
                        current_row.append((tup[0], self.settings.bg_color))
                    # lives from enough surrounding cells
                    else:
                        current_row.append((tup[0], self.settings.square_color))
                
                # if the cell is dead
                else:
                    
                    # comes back to life if surrounded by exactly 3 cells
                    if self._total_surround(row_count, col_count) == 3:
                        current_row.append((tup[0], self.settings.square_color))
                    # stays dead from not enough or too many surrounding cells
                    else:
                        current_row.append((tup[0], self.settings.bg_color))

                # advance the column counter
                col_count += 1

            # add the next generation row and advance the row counter
            next_gen.append(current_row)
            row_count += 1

        # return the next generation of cells
        return next_gen


    def _print_next_generation(self):
        """
        Prints the next generation to the screen. At this point, the simulation
        is running, so no changes to the grid can be made.
        """

        # change self.grid to be the next generation, then print
        self.grid = self._get_next_generation(self.grid)

        for row in self.grid:
            for tup in row:
                pygame.draw.rect(
                    self.screen,
                    tup[1],
                    tup[0],
                )


    def _update_grid(self):
        """Updates the grid each for each pass of the main game loop."""
        
        # if the simulation is NOT running
        if not self.simulation_running:
            for row in self.grid:
                for tup in row:
                    pygame.draw.rect(
                        self.screen,
                        tup[1],
                        tup[0],
                    )
        # if the simulation IS running
        else:
            self._print_next_generation()
            time.sleep(self.settings.evolution_speed)


    def _total_surround(self, row, col):
        """Returns the total number of living cells surrounding the one at (row, col)."""

        # calculates the final row and col indices based on screen dimensions & screen size
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
        
        # deal with the outer edges
        elif row == 0:
            if self._is_alive(0, col - 1):
                count += 1
            if self._is_alive(0, col + 1):
                count += 1
            if self._is_alive(1, col - 1):
                count += 1
            if self._is_alive(1, col + 1):
                count += 1
            if self._is_alive(1, col):
                count += 1
        elif row == bottom_pos:
            if self._is_alive(bottom_pos, col - 1):
                count += 1
            if self._is_alive(bottom_pos, col + 1):
                count += 1
            if self._is_alive(bottom_pos - 1, col - 1):
                count += 1
            if self._is_alive(bottom_pos - 1, col + 1):
                count += 1
            if self._is_alive(bottom_pos - 1, col):
                count += 1
        elif col == 0:
            if self._is_alive(row + 1, 0):
                count += 1
            if self._is_alive(row + 1, 1):
                count += 1
            if self._is_alive(row - 1, 0):
                count += 1
            if self._is_alive(row - 1, 1):
                count += 1
            if self._is_alive(row, 1):
                count += 1            
        elif col == right_pos:
            if self._is_alive(row + 1, right_pos):
                count += 1
            if self._is_alive(row + 1, right_pos - 1):
                count += 1
            if self._is_alive(row - 1, right_pos):
                count += 1
            if self._is_alive(row - 1, right_pos - 1):
                count += 1
            if self._is_alive(row, right_pos - 1):
                count += 1   
    
        # deal with the inner squares
        else:
            if self._is_alive(row - 1, col - 1):
                count += 1
            if self._is_alive(row - 1, col):
                count += 1
            if self._is_alive(row - 1, col + 1):
                count += 1
            if self._is_alive(row, col - 1):
                count += 1
            if self._is_alive(row, col + 1):
                count += 1
            if self._is_alive(row + 1, col - 1):
                count += 1
            if self._is_alive(row + 1, col):
                count += 1
            if self._is_alive(row + 1, col + 1):
                count += 1

        return count


    def _toggle_square(self, row, col):
        """Toggles the state of a square at row, col."""

        if not self._is_alive(row, col):
            self.grid[row][col] = (self.grid[row][col][0], self.settings.square_color)
        else:
            self.grid[row][col] = (self.grid[row][col][0], self.settings.bg_color)


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


    def _clear_all_cells(self):
        """Resets all cells to 'dead' in self.grid."""

        # traverse self.grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.grid[row][col] = (self.grid[row][col][0], self.settings.bg_color)


    def _open_menu(self):
        """
        Opens the menu, freezing the current generation in place
        and giving the user a range of different options.
        """
        
        # pauses the game
        self.in_menu = True
        
        # draw the menu and its elements
        self.menu.draw_menu()
        pygame.display.flip()
        
        while self.in_menu:

            # check for events in the menu
            for event in pygame.event.get():
                
                # quits the game using the red 'x' on the window
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # closes out of the menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.in_menu = False


    def _check_keydown_events(self, event):
        """Check for (and service) any keydown events."""
        
        # enter key begins the simulation
        if event.key == pygame.K_RETURN:
            self.grid_copy = self.grid
            self.simulation_running = True
        
        # q key ends the simulation
        if event.key == pygame.K_q:
            self.grid = self.grid_copy
            self.simulation_running = False
        
        # escape key brings up the menu
        if event.key == pygame.K_ESCAPE:
            self._open_menu()

        # c key clears the board (when sim is not running)
        if event.key == pygame.K_c and not self.simulation_running:
            self._clear_all_cells()


    def run_game(self):
        """The main game loop."""
        while not self.in_menu:
            
            # check for events
            for event in pygame.event.get():
                
                # quits the game using the red 'x' on the window
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # check for keydown events
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                # fills a cell in the grid (when sim is not running)
                if event.type == pygame.MOUSEBUTTONUP and not self.simulation_running:
                    if event.button == pygame.BUTTON_LEFT:
                        mouse_pos = pygame.mouse.get_pos()
                        self._check_mouse_click(mouse_pos)

            # fill background, update grid and borders
            self.screen.fill(self.settings.bg_color)
            self._update_grid()
            self._update_borders()
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()