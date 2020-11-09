# MiPiEngine v1.0 licensed under the Apache license 2.0
# Created by Aaron Keith Sanders
# Project start date 11/08/2020

import pygame

# Window initialization

# Creating the dimensions for the game engine screen
width = 600
height = 600

screen = pygame.display.set_mode((width,height))

# This is needed to display the window
pygame.display.flip()

# Loop used to keep the engine window running until the user closes it
running = True

while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



