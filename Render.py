import pygame
from pygame import *
import MiPi

pygame.init()
size = (800, 625)
triangle = pygame.Surface(size)

class Shapes:

    def __init__(self):
        return self

    @staticmethod
    def CreateTriangle():
        GREEN = (0, 255, 0)
        verts = [(50, 0), (100, 50), (50, 50), (0, 50)]
        triangle.fill(MiPi.DARKGRAY)
        pygame.draw.polygon(triangle, GREEN, verts)
