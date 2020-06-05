import pygame as pg


class Ship:
    def __init__(self, game):
        # Set first position of our ship
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # Get the image of the ship
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a horizontal value for the ship position.
        self.x = float(self.rect.x)
        # Initialize first False values for movement
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Initialize the ship
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right:
            # Increment movement by specified speed
            # units to the right
            self.x += self.settings.ship_speed
        if self.moving_left:
            # Increment movement by specified speed
            # units to the left
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x
