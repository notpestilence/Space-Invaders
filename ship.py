import pygame as pg

class Ship:
    def __init__(self, game):
        #Set first position of our ship
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        #Get the image of the ship
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Initialize first False values for movement
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #Initialize the ship

    def update(self):
        if self.moving_right:
            # Increment movement by 3 units
            # to the right
            self.rect.x += 3
        if self.moving_left:
            # Increment movement by 3 units
            # to the right
            self.rect.x -= 3

