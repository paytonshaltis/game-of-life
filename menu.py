"""Holds information related to the game menu."""
from menu_element import MenuElement

class Menu:
    """Instance of the Menu class that contains menu elements."""

    def __init__(self, game):
        """Creates the Menu object with these attributes."""
        self.game = game
        self.element_title = MenuElement(self.game, 'Menu', (200, 100), (0, 0, 0), (100, 100))