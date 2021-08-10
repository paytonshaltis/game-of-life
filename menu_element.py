"""Allows for the creation of different menu elements."""
import pygame, pygame.font

class MenuElement:
    """Instance of a single element in the menu."""

    def __init__(self, game, text, font, font_size, color, position, anchor, deltax=0, deltay=0, bold=False):
        """Creates a new MenuElement from the given parameters."""

        # instance variables
        self.game = game
        self.text = text
        self.color = color
        self.position = position
        self.bold = bold
        self.anchor = anchor
        self.deltax = deltax
        self.deltay = deltay
        self.font = pygame.font.SysFont(font, font_size, bold=self.bold)
        self.rect = None
        self.text_image = None
        
        # prepare the menu element
        self._set_text()

        # build the element's Rect object and position it
        self.rect = self.text_image.get_rect()
        if self.anchor == 'midtop':
            self.rect.midtop = self.position
        elif self.anchor == 'midleft':
            self.rect.midleft = self.position
        elif self.anchor == 'topleft':
            self.rect.topleft = self.position

        self.rect.x += deltax
        self.rect.y += deltay

    
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