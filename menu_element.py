"""Allows for the creation of different menu elements."""
import pygame, pygame.font

class MenuElement:
    """Instance of a single element in the menu."""

    def __init__(self, game, text, font, font_size, color, position, bold):
        """Creates a new MenuElement from the given parameters."""

        # instance variables
        self.game = game
        self.text = text
        self.color = color
        self.position = position
        self.bold = bold
        self.font = pygame.font.SysFont(font, font_size, bold=self.bold)
        self.rect = None
        self.text_image = None
        
        # prepare the menu element
        self._set_text()

        # build the element's Rect object and position it
        self.rect = self.text_image.get_rect()
        self.rect.midtop = self.position 

    
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