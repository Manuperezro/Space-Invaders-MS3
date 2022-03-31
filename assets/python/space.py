# sys modules used when user decided to exit game
import sys

# pygame module used to add functionality to the game
import pygame

from configurations import Configurations

def run_game():
    """
    Initialize the game, the configurations and create and screen object
    """
    pygame.init()
    ai_configurations = Configurations()

    # Create a screen to visualize the game 800pxiles width 600px height
    screen = pygame.display.set_mode((ai_configurations.screen_width, 
    ai_configurations.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Loop to repeat the game
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw the screen everytime the loop is activated
        screen.fill(ai_configurations.bg_color)

        # Update continiusly the elements on the screem, to show new positions 
        # of the elements in the most recent screen
        pygame.display.flip()

run_game()


