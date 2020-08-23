import sys

import pygame

def check_events(ship):
    """Respond to keypresses & mouse events."""
    # Watch for keyboard and mouse events.
    # event: action the user performs while playing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    """Update images on the creen and flip to the new screen."""
    # Redraw the screen during each pass thru the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()