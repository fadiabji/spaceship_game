import sys
import pygame
import random
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvation:
    """Overall calss to mange game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invation")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() 
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self): 
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self._stars_background_on()

    def _check_events(self):
        """This method called helper method, it prfixs with _"""
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True 
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -(3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            

    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _stars_background_on(self):
        """ Making a three typs of stars on a black background"""
        #create the locations of the stars for when we animate the background
        star_field_slow = []
        star_field_medium = []
        star_field_fast = []

        for slow_stars in range(50): #birth those plasma balls, baby
            star_loc_x = random.randrange(0, self.settings.screen_width)
            star_loc_y = random.randrange(0, self.settings.screen_height)
            star_field_slow.append([star_loc_x, star_loc_y]) #i love your balls

        for medium_stars in range(35):
            star_loc_x = random.randrange(0, self.settings.screen_width)
            star_loc_y = random.randrange(0, self.settings.screen_height)
            star_field_medium.append([star_loc_x, star_loc_y])

        for fast_stars in range(15):
            star_loc_x = random.randrange(0, self.settings.screen_width)
            star_loc_y = random.randrange(0, self.settings.screen_height)
            star_field_fast.append([star_loc_x, star_loc_y])

        #my soul knows only darkness
        self.screen.fill((0, 0, 0))

        #animate some motherfucking stars
        for star in star_field_slow:
            star[1] += 1
            if star[1] > self.settings.screen_height:
                star[0] = random.randrange(0, self.settings.screen_width)
                star[1] = random.randrange(-10, 10)
            pygame.draw.circle(self.screen, (128, 128, 128), star, 3)

        for star in star_field_medium:
            star[1] += 4
            if star[1] > self.settings.screen_height:
                star[0] = random.randrange(0, self.settings.screen_width)
                star[1] = random.randrange(-10, 10)
            pygame.draw.circle(self.screen, (192, 192, 192), star, 2)

        for star in star_field_fast:
            star[1] += 8
            if star[1] > self.settings.screen_height:
                star[0] = random.randrange(0, self.settings.screen_width)
                star[1] = random.randrange(-10, 10)
            pygame.draw.circle(self.screen, (255, 255, 0), star, 1)

        #set frames per second
        pygame.time.Clock()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvation()
    ai.run_game()



