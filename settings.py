"""Contains the Settings class to manage game settings."""
from game import Game

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

class Settings:
    """Instance of the Settings class to manage game settings."""

    def __init__(self, game:Game):
        """Creates an instance of the Settings class using a Game instance."""
        
        # instance of the Game class for access to its attributes
        self.game = game

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = COLOR_BLACK
        
        # square settings
        self.square_color = COLOR_WHITE