# This is my MiPi module, it will contain the MiPi class and all of its
# Functions, methods and variables.

import pygame
from pygame import *

# Gonna use tkinter for my gui module, but due to utilizing only one main instance at a time with pygame,
# I am going to have to just use the pygame window as my main engine frame and reserve an area on the
# frame for creating a game, then just launch a seperate pygame window for testing/playing a game.
import tkinter as tk
from tkinter import *

import logging
import datetime


# Initialize pygame
pygame.init()


# All Global Variables
GREEN = (0,255,0)
LIGHT_BLUE = (173,216,230)
WHITE = (255,255,255)
LIGHTCOLOR = (170,170,170)
DARKSHADE = (100,100,100)
CorbelFont = pygame.font.SysFont('Corbel', 35)
guitext = CorbelFont.render('File', True, WHITE)
verts = [(50, 0), (100, 50), (50, 50), (0, 50)]
size = (145, 145)

# Creating the dimensions for the game engine screen
width = 800
height = 625

# Datetime vars
current_date = datetime.datetime.now()
screen = pygame.display.set_mode((width, height))

class MiPi:
    def __init__(self):
        self

    @staticmethod
    def EngineScreen():

        # Pygame
        title = "MiPi Engine"
        pygame.display.set_caption(title)
        screen.fill(LIGHT_BLUE)

        # Loop used to keep the engine window running until the user closes it
        running = True

        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width/17 <= mouse[0] <= width/17+140 and height/17 <= mouse[1] <= height/17+40:
                        print(current_date, "File button was clicked on submenu!")

            mouse = pygame.mouse.get_pos()

            # If mouse is over a button it changes its shade color
            if width/17 <= mouse[0] <= width/17+140 and height/17 <= mouse[1] <= height/17+40:
                pygame.draw.rect(screen, LIGHTCOLOR, [width / 17, height / 17, 140, 40])
            else:
                pygame.draw.rect(screen, DARKSHADE, [width / 17, height / 17, 140, 40])

            # Setting the text on the button
            screen.blit(guitext, (width / 17 + 50, height / 17))

            # Calling my DrawTriangle() method
            MiPi.DrawTriangle()

            # This is needed to display the window
            pygame.display.flip()


    @staticmethod
    def EngineInit():
        # This method is called upon starting the MiPi engine
        logging.basicConfig(filename='mipi.log', level=logging.INFO)
        print(current_date, ": MiPi Engine v1.0 has been initialized")
        logging.info(current_date)
        logging.info("MiPi Engine v1.0 has been initialized.")

    @staticmethod
    def DrawTriangle():
        # Example code to draw a triangle
        triangle = pygame.Surface(size)
        pygame.draw.polygon(triangle, GREEN, verts)
        screen.blit(triangle, (70, 90))


