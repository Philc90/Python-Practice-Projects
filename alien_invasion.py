import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings & screen obj.
    pygame.init()
    ai_settings = Settings()
    #screen is an example of a pygame surface, which is any element in the game
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion (AKA Space Invaders bro)")

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()