"""Contains the Settings class to manage game settings."""

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

class Settings:
    """Instance of the Settings class to manage game settings."""

    def __init__(self, game):
        """Creates an instance of the Settings class using a Game instance."""
        
        # instance variables
        # instance of the Game class for access to its attributes
        self.game = game

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = COLOR_WHITE
        
        # square settings
        self.square_color = COLOR_BLACK
        self.square_size = 40
        self.square_bord_thick = 1