import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a chip object
    ship = Ship(my_settings, screen)

    # make a group for bullets
    bullets = Group()

    # main loop of the game
    while True:
        gf.check_events(my_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(my_settings, screen, ship, bullets)


run_game()