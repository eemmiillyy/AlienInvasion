import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game, setttings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))

    # Screen is a surface like every other object in the game.
    pygame.display.set_caption("Alien Invasion")

    # Make play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game stats.
    stats = GameStats(ai_settings)

    # Create an instance of score board.
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make a group to store aliens in.
    aliens = Group()

    # Create fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main game loop.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
