import sys
import pygame
from bullet import Bullet


def check_events(my_settings, screen, ship, bullets):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
        # stop the program when window is terminated
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, my_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(my_settings, screen, ship, bullets):
    # change bg color for each loop
    screen.fill(my_settings.bg_color)
    # redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # show next frame
    pygame.display.flip()


def check_keydown_events(event, my_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(my_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """update the position of bullets and get rid of old bullets"""
    bullets.update()
    # remove the bullets that passed the screen above
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))


def fire_bullet(my_settings, screen, ship, bullets):
    """Fire a bullet if limit is not reached yet"""
    # create a new bullet and add it to the bullets group
    if len(bullets) < my_settings.bullets_allowed:
        new_bullet = Bullet(my_settings, screen, ship)
        bullets.add(new_bullet)