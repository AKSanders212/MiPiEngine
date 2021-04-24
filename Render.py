# MiPi Engine alpha v1.0 - © Aaron Keith Sanders - All Rights Reserved

import pygame
from pygame import *
import MiPi
from MiPi import *
import MiPiSettings

pygame.init()
size = (800, 625)
triangle = pygame.Surface(size)

# Color constants
GREEN = (0, 255, 0)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)
DARKGRAY = (169, 169, 169)
LIGHTCOLOR = (170, 170, 170)
DARKSHADE = (80, 80, 80)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
TRANSPARENCY = (0, 0, 0, 0)
RED = (255, 0, 0)


class Shapes:
    def __init__(self):
        return self

    @staticmethod
    def CreateTriangle():
        verts = [(50, 0), (100, 50), (50, 50), (0, 50)]
        triangle.fill(DARKGRAY)
        pygame.draw.polygon(triangle, GREEN, verts)