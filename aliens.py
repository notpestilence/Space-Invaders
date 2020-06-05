import sys
import os
import pygame as pg
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship


class SpaceInvaders:
    def __init__(self):
        pg.init()  # Initialize the module
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Space Invaders")  # Initialize surface
        self.bg_color = (28, 29, 33)  # HEX is #082051
        self.ship = Ship(self)

    def run_game(self):
        # Main loop for the game:
        while True:
            self._check_events()  # Helper method defined below :)
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Check keystrokes
        for keystroke in pg.event.get():
            if keystroke.type == pg.QUIT:
                sys.exit()
            elif keystroke.type == pg.KEYDOWN:
                if keystroke.key == pg.K_RIGHT:
                    # Increment movement by 30 units
                    # to the right
                    self.ship.moving_right = True
                if keystroke.key == pg.K_LEFT:
                    # Increment movement by 30 units
                    # to the left
                    self.ship.moving_left = True
            elif keystroke.type == pg.KEYUP:
                if keystroke.key == pg.K_RIGHT:
                    # Increment movement by 30 units
                    # to the right
                    self.ship.moving_right = False
                if keystroke.key == pg.K_LEFT:
                    # Increment movement by 30 units
                    # to the left
                    self.ship.moving_left = False

    def _update_screen(self):
        # Make the most recently drawn surface
        # visible for new keystrokes
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pg.display.flip()

if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
