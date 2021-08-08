"""Contains the Game class to create instances of the New Game of Life."""
import pygame, pygame.display, pygame.event, pygame.rect
from settings import Settings

class Game:
    """An instance of the Game class."""
    
    def __init__(self):
        """Creates an instance of the Game class"""
        pygame.init()
        self.settings = Settings(self)
    
