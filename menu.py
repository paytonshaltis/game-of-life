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
        self.all_menu_items = []
        self.element_title = None
        self.element_controls = None
        self.element_control1 = None

        # initialize the menu (only done once)
        self._initialize_menu()


    def draw_menu(self):
        """Draws the menu to the screen."""

        # the background of the menu itself
        pygame.draw.rect(
            self.game.screen,
            self.settings.menu_color,
            self.menu_rect
        )

        # the menu elements
        for element in self.all_menu_items:
            element.draw_menu_element()


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
        self.element_title = MenuElement(
            game=self.game, 
            text='MENU', 
            font=self.settings.font,
            font_size=int(
                (self.settings.screen_width * self.settings.screen_height) / 12500),
            color=(0, 0, 0), 
            position=self.menu_rect.midtop,
            anchor='midtop'
        )
        self.element_controls = MenuElement(
            game=self.game,
            text='Controls:',
            font=self.settings.font,
            font_size=int(
                (self.settings.screen_width * self.settings.screen_height) / 25000),
            color=(0, 0, 0),
            position=self.menu_rect.midleft,
            anchor='midleft',
            deltax=int((1/40) * self.size[0]),
            deltay= -int((1/4) * self.size[1])
        )
        self.element_control1 = MenuElement(
            game=self.game,
            text='\'Enter\' - begin simulation',
            font=self.settings.font,
            font_size=int(
                (self.settings.screen_width * self.settings.screen_height) / 40000),
            color=(0, 0, 0),
            position=self.element_controls.rect.bottomleft,
            anchor='topleft',
        )

        # append all elements to the list
        self.all_menu_items.append(self.element_title)
        self.all_menu_items.append(self.element_controls)
        self.all_menu_items.append(self.element_control1)