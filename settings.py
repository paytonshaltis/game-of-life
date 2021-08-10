"""Contains the Settings class to manage game settings."""

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (200, 200, 200)
COLOR_DGRAY = (155, 155, 155)

class Settings:
    """Instance of the Settings class to manage game settings."""

    def __init__(self, game):
        """Creates an instance of the Settings class using a Game instance."""
        
        # instance variables
        # instance of the Game class for access to its attributes
        self.game = game

        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = COLOR_WHITE
        self.border_color = COLOR_GRAY
        self.pause_menu_color = COLOR_DGRAY
        
        # square settings
        self.square_color = COLOR_BLACK
        self.square_size = 20

        # game speed settings
        self.evolution_speed = 0.1