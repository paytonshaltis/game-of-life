"""Holds information related to the game menu."""
import pygame, pygame.rect, pygame.draw
from menu_element import MenuElement

class Menu:
    """Instance of the Menu class that contains menu elements."""

    def __init__(self, game):
        """Creates the Menu object with these attributes."""
        
        # general instance variables
        self.game = game
        self.settings = self.game.settings
        self.size = None
        self.menu_rect = None

        # menu elements
        self.element_title = None

        # initialize the menu (only done once)
        self._initialize_menu()


    def _initialize_menu(self):
        """Initializes Menu attributes. Only needs to be done once."""
        
        # general instance variables
        self.size = (
            self.settings.menu_size * self.settings.screen_width, 
            self.settings.menu_size * self.settings.screen_height
        )
        self.menu_rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.menu_rect.center = self.game.screen.get_rect().center

        # menu elements
        self.element_title = MenuElement(self.game, 'Menu', (200, 100), (0, 0, 0), (100, 100))

    
    def draw_menu(self):
        """Draws the menu to the screen."""

        # the background of the menu itself
        pygame.draw.rect(
            self.game.screen,
            self.settings.menu_color,
            self.menu_rect
        )

        # the menu elements
        self.element_title.draw_menu_element()