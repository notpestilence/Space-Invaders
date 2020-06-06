import sys
import os
import pygame as pg
from pygame.sprite import Sprite
from settings import Settings
from properties import Ship, Bullet


class SpaceInvaders:
    def __init__(self):
        pg.init()  # Initialize the module
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Space Invaders")  # Initialize surface
        self.bg_color = (28, 29, 33)  # HEX is #082051
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()

    def run_game(self):
        # Main loop for the game:
        while True:
            # Refactor helper method(s) defined below :)
            self._check_events()  # 1. Check player keystroke
            self.ship.update()  # 2a. If keystroke is move, then move the ship
            self._update_bullets()  # 2b. If keystroke is fire, then fire the bullet
            self._update_screen()  # Comes last to update all events above

    def _check_events(self):
        # Check keystrokes
        for keystroke in pg.event.get():
            if keystroke.type == pg.QUIT:
                sys.exit()
            elif keystroke.type == pg.KEYDOWN:
                self._check_keydown_events(keystroke)
            elif keystroke.type == pg.KEYUP:
                self._check_keyup_events(keystroke)

    def _update_screen(self):
        # Make the most recently drawn surface
        # visible for new keystrokes
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pg.display.flip()

    def _check_keydown_events(self, keystroke):
        # Helper function to respond to keystrokes in press
        if keystroke.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif keystroke.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif keystroke.key == pg.K_ESCAPE or keystroke.key == pg.K_q:
            sys.exit()
        elif keystroke.key == pg.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, keystroke):
        # Helper function to respond to keystrokes in release
        if keystroke.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif keystroke.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        # Add a new bullet object
        # and add to existing bullets group
        bullet = Bullet(self)
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.add(bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Get rid of offscreen bullets
        for offscreen in self.bullets.copy():
            if offscreen.rect.bottom <= 0:  # Check if it is indeed offscreen
                self.bullets.remove(offscreen)  # Remove fired bullet if it is


if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
