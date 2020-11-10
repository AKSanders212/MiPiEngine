# This is my MiPi module, it will contain the MiPi class and all of its
# Functions, methods and variables.

import pygame
import logging
import datetime

# global variables

# Creating the dimensions for the game engine screen
width = 600
height = 600

current_date = datetime.datetime.now()


class MiPi:
    def __init__(self):
        self

    @staticmethod
    def EngineScreen():
        screen = pygame.display.set_mode((width, height))

        # This is needed to display the window
        pygame.display.flip()

        # Loop used to keep the engine window running until the user closes it
        running = True

        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # This method is called upon starting the MiPi engine.
    @staticmethod
    def EngineInit():
        logging.basicConfig(filename='mipi.log', level=logging.INFO)
        print(current_date, ": MiPi Engine v1.0 has been initialized")
        logging.info(current_date)
        logging.info("MiPi Engine v1.0 has been initialized.")