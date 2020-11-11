# This is my MiPi module, it will contain the MiPi class and all of its
# Functions, methods and variables.

import pygame
import logging
import datetime

# Initialize pygame
pygame.init()

# global variables
GREEN = (0,255,0)
verts = [(50, 0), (100, 50), (50, 50), (0, 50)]
size = (200, 200)

# Creating the dimensions for the game engine screen
width = 600
height = 600

current_date = datetime.datetime.now()


class MiPi:
    def __init__(self):
        self

    @staticmethod
    def EngineScreen():
        title = "MiPi Engine"
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # This is needed to display the window
        pygame.display.flip()

        # Loop used to keep the engine window running until the user closes it
        running = True

        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Example code to draw a triangle
            triangle = pygame.Surface(size)
            pygame.draw.polygon(triangle, GREEN, verts)
            screen.blit(triangle, (275, 300))
            pygame.display.update()


    @staticmethod
    def EngineInit():
        # This method is called upon starting the MiPi engine
        logging.basicConfig(filename='mipi.log', level=logging.INFO)
        print(current_date, ": MiPi Engine v1.0 has been initialized")
        logging.info(current_date)
        logging.info("MiPi Engine v1.0 has been initialized.")

