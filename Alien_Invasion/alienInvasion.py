import sys, pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a chip object
    ship = Ship(screen)

    # main loop of the game
    while True:
        for event in pygame.event.get():
            # stop the program when window is terminated
            if event.type == pygame.QUIT:
                sys.exit()

        # change bg color for each loop
        screen.fill(my_settings.bg_color)
        ship.blitme()

        # show next frame
        pygame.display.flip()

run_game()