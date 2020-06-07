class Settings:
    """ A class to store all settings in the game <3 """

    def __init__(self):
        # Screen settings
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (28, 29, 33)  # HEX is #082051
        self.ship_speed = 3.0
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 228, 228)  # HEX is #FFE4E4
        self.bullet_allowed = 3

