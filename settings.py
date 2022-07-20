class Settings:
    """A class to store all settings for Alien Invation."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        # Ship settings
        self.ship_speed = 2
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,255,255)
        self.bullet_allowed = 20
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet_dirrction of 1 represents right: -1 represents left.
        self.fleet_direction = 1
        
