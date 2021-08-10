"""Allows for the creation of different menu elements."""
import pygame, pygame.font

class MenuElement:
    """Instance of a single element in the menu."""

    def __init__(self, game, text, size, color, position):
        """Creates a new MenuElement from the given parameters."""

        # instance variables
        self.game = game
        self.text = text
        self.size = size
        self.color = color
        self.position = position
        self.font = pygame.font.SysFont('applegothic', 48)
        self.rect = None
        self.text_image = None

        # build the element's Rect object
        self.rect = pygame.Rect(
            position[0], 
            position[1],
            size[0],
            size[1]
        )
        
        # prepare the menu element
        self._set_text()

    
    def draw_menu_element(self):
        """Draws the menu element to the screen."""

        self.game.screen.blit(
            self.text_image,
            self.rect
        )


    def _set_text(self):
        """Turn 'text' into a rendered image."""
        
        self.text_image = self.font.render(
            self.text,
            True,
            self.color,
            None
        )        