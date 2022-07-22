import pygame 
from pygame.sprite import Sprite
from random import choice
from ship import Ship

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.ship = ai_game.ship

        self.settings = ai_game.settings

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Move the alien to the right"""
        # self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        # self.rect.x = self.x
        self.attack_ship()

    def attack_ship(self):
        """make aliens attack the ship"""
        if self.rect.x - self.ship.rect.x > 0:
            # alien moving to the left
            self.x += (self.settings.alien_speed * -1)
            self.rect.x = self.x

        elif self.rect.x - self.ship.rect.x < 0:
            # alien moving to the right
            self.x +=  self.settings.alien_speed
            self.rect.x = self.x
        
        elif self.rect.y - self.ship.rect.y > 0:
            # alien moving down
            self.y += (self.settings.alien_speed * -1)
            self.rect.y = self.y

        elif self.rect.y - self.ship.rect.y < 0:
                # alien moving up
            self.y += self.settings.alien_speed
            self.rect.y = self.y


    # def random(self):
    #     """Move the alien randomly"""
    #     self.x +=  (choice([0,1,2,3])*choice([-1,1]))
    #     self.rect.x = self.x



      # To make eliens moving inside the screen just edit the check_dedges() as below:
      # screen_rect = self.screen.get_rect()
      #   print(f"self.rect.right = {self.rect.right}")
      #   print(f"screen_rect.right = {screen_rect.right}")
      #   print("------------------")
      #   if self.rect.right*(screen_rect.right//self.rect.right)  >= screen_rect.right or self.rect.left <= 0:
      #       return True