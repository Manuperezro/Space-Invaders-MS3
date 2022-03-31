# sys modules used when user decided to exit game
import sys

# pygame module used to add functionality to the game
import pygame


def run_game():
    """
    Initialize the game and create and screen object
    """
    pygame.init()

    # Create a screen to visualize the game 800pxiles width 600px height
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien Invasion")

    # Set up back gtoung color
    bg_color = (230, 230, 230)

    # Loop to repeat the game
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Draw the screen everytime the loop is activated
        screen.fill(bg_color)

        # Update continiusly the elements on the screem, to show new positions 
        # of the elements in the most recent screen
        pygame.display.flip()

run_game()


