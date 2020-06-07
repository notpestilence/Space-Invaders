import pygame as pg
from pygame.sprite import Sprite


class Ship:
    def __init__(self, game):
        # Initialize surface
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # Get the image of the ship
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a horizontal value for the ship position, self.x.
        self.x = float(self.rect.x)
        # Initialize first False values for movement
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Initialize the ship
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            # If our current ship position < right edge of the screen,
            # Increment movement by specified speed
            # units to the right
            self.x += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0):
            # If our current ship position > left edge of the screen,
            # Increment movement by specified speed
            # units to the left
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x


class Bullet(Sprite):
    def __init__(self, game):
        super(Bullet, self).__init__()
        self.ship = Ship(game)
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0)
        self.rect = pg.Rect(0, 0, self.settings.bullet_width,
                            self.settings.bullet_height)
        # Assigning correct position of bullet
        # based on where the ship is
        self.rect.midtop = game.ship.rect.midtop
        # Store a vertical value for the bullet position, self.y.
        self.y = float(self.rect.y)

    def update(self):
        # Method to animate firing bullets
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Method to initialize the bullet
        pg.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
    def __init__(self, game):
        super(Alien, self).__init__()
        # Initialize surface
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # Get the image of the alien
        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()  # Get rectangle attribute
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store a horizontal value for the alien position, self.x.
        # Used to move the alien left and right.
        self.x = float(self.rect.x)