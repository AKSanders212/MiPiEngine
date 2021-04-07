# This is the physics engine for MiPi Engine

import pygame
from pygame import *

class Player:

    gravity = 0
    mass = 0
    boundary = False
    particles = 0
    isKinematic = False
    isPhasable = False
    velocity = 0
    acceleration = 0
    force = 0
    friction = 0
    rigidbody2D = False
    addphysics = None
    addboxcollider = None
    size = (300, 300)
    boxsurface = pygame.Surface(size)

    def __init__(self):
        pass

    @classmethod
    def BoxCollider2D(cls, surface, color, w, h, x, y):
        pygame.draw.rect(surface, color, pygame.Rect(w, h, x, y))

