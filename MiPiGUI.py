import pygame
from pygame import *
import pygame_gui
from pygame_gui import *
import Render
from Render import *
import math
from math import *
import MiPi
from MiPi import *

# Global vars
mainframe = pygame_gui.UIManager((800, 625))

# Pygame_gui UI elements
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((475, 25), (100, 50)),
                                           text='Test Game', manager=mainframe)

dropmenu = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((20, 25), (400, 50)), starting_option=
                                              "File", options_list=["Run", "Import Sprite", "Close"], manager=mainframe)

import_sprite = None

# Max dimmensions for the game screen - Make sure that no sprite will be bigger than 1/3 of the overall screen size.
g_screen_x = 800
g_screen_y = 625
max_image_display_dimensions = (g_screen_x / 4, g_screen_y / 4)

size = (375,275)
screensize = (200,156,200,156)
editorscreen = pygame.Surface(size)

edx = 100
edy = 165

# Label fonts for engine screen, etc.
smallfont = pygame.font.Font('freesansbold.ttf', 16)
editorlabel = smallfont.render('Game Editor', True, Render.WHITE, Render.DARKSHADE)
editorborder = editorlabel.get_rect()
editorborder.center = (edx,edy)

class GUI:

    def __init__(self):
        return self

    @classmethod
    def EditorScreen(cls):
        editorscreen.fill(Render.WHITE)
        pygame.draw.rect(editorscreen, Render.WHITE, screensize)
        MiPi.enginescreen.blit(editorscreen, (50,185))

