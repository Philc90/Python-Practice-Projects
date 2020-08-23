import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings & screen obj.
    pygame.init()
    ai_settings = Settings()
    #screen is an example of a pygame surface, which is any element in the game
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion (AKA Space Invaders bro)")

    # Make a ship.
    ship = Ship(screen)

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        # event: action the user performs while playing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass thru the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()