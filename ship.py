import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship & set its starting pos. """
        self.screen = screen

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

    def blitme(self):
        """Draw the ship at its current loc."""
        self.screen.blit(self.image, self.rect)