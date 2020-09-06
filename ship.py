import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to represent the player's ship."""

    def __init__(self, ai_settings, screen):
        """Initialize the ship & set its starting pos. """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # get rect covering the surface
        self.screen_rect = screen.get_rect()

        """
        When you’re centering a game element, work with the center, centerx, or
        centery attributes of a rect. When you’re working at an edge of the screen,
        work with the top, bottom, left, or right attributes. When you’re adjusting
        the horizontal or vertical placement of the rect, you can just use the x and
        y attributes, which are the x- and y-coordinates of its top-left corner. 
        """

        # start each new ship at the bottom corner of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect obj from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current loc."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx