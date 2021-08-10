"""Contains the Settings class to manage game settings."""
import pygame, pygame.font

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (200, 200, 200)
COLOR_DGRAY = (155, 155, 155)
COLOR_ORANGE = (255, 164, 32)

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
        self.border_color = COLOR_GRAY
        
        # square settings
        self.square_color = COLOR_ORANGE
        self.square_size = 10

        # game speed settings
        self.evolution_speed = .001

        # menu settings
        self.menu_size = 5/6
        self.menu_color = COLOR_DGRAY
        self.font = 'optima'

        # test for the font
        if self.font not in pygame.font.get_fonts():
            self.font = None