import pygame
from pygame import *
import pygame_gui
from pygame_gui import *
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from pygame_gui.elements.ui_horizontal_slider import UIHorizontalSlider
from pygame_gui.core.drawable_shapes.rect_drawable_shape import RectDrawableShape
import Render
from Render import *
import math
from math import *
import MiPi
from MiPi import *

# Initialize pygame
pygame.init()

# The resolution size of the engine frame
UIlimitwidth = 800
UIlimitheight = 625

# Global vars
mainframe = pygame_gui.UIManager((UIlimitwidth, UIlimitheight))

# Pygame_gui UI elements
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 35), (90, 50)),
                                           text='Test Game', manager=mainframe)

updatespr_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 230), (130, 50)),
                                                text='Update Location', visible=0, manager=mainframe)

dropmenu = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((35, 35), (150, 50)), starting_option=
"File", options_list=["Run", "Import Sprite", "Close"], manager=mainframe)

import_sprite = None
base_sprite = None
base_sprimg = None

# Max dimmensions for the game screen - Make sure that no sprite will be bigger than 1/3 of the overall screen size.
g_screen_x = 800
g_screen_y = 625
max_image_display_dimensions = (g_screen_x / 4, g_screen_y / 4)

size = (375, 275)
screensize = (200, 156, 200, 156)
editorscreen = pygame.Surface(size)

edx = 100
edy = 155

# Get the string value of the x and y sprite sliders
textx = ''
texty = ''

# Label fonts for engine screen, etc.
smallfont = pygame.font.Font('freesansbold.ttf', 16)
editorlabel = smallfont.render('Game Editor', True, Render.WHITE, Render.DARKSHADE)
editorborder = editorlabel.get_rect()
editorborder.center = (edx, edy)

spritelocationlabel = smallfont.render('Sprites Location', True, Render.WHITE, Render.DARKSHADE)
spriteborder = spritelocationlabel.get_rect()
spriteborder.center = (550, 140)

xlabel = smallfont.render('X Value', True, Render.WHITE, Render.DARKSHADE)
xborder = xlabel.get_rect()
xborder.center = (500, 165)

ylabel = smallfont.render('Y Value', True, Render.WHITE, Render.DARKSHADE)
yborder = ylabel.get_rect()
yborder.center = (600, 165)

engineborder_width = 800
engineborder_height = 10
enginebordersize = (engineborder_width, engineborder_height, engineborder_width, engineborder_height)

engineborder_north = smallfont.render('============================================================================'
                                      '============================================================================'
                                      '==========================', True, Render.DARKSHADE, Render.DARKSHADE)
set_engineborder_north = engineborder_north.get_rect()
set_engineborder_north.center = (0, 9)

engineborder_south = smallfont.render('============================================================================'
                                      '============================================================================'
                                      '==========================', True, Render.DARKSHADE, Render.DARKSHADE)
set_engineborder_south = engineborder_south.get_rect()
set_engineborder_south.center = (0, 617)

# Create the x and y horizontal float sliders
xlocbar = UIHorizontalSlider(relative_rect=pygame.Rect(450, 205, 100, 20), start_value=80,
                             value_range=(80, 400), visible=0,
                             manager=mainframe)

ylocbar = UIHorizontalSlider(relative_rect=pygame.Rect(550, 205, 100, 20), start_value=215,
                             value_range=(215, 425), visible=0,
                             manager=mainframe)


class GUI:

    def __init__(self):
        pass

    @classmethod
    def MiPiBorders(cls, surface, color, x, y, width, height, borderwidth):
        pygame.draw.lines(surface, color, True, [(x, y), (x + width, y), (x + width, y + height), (x, y + height)],
                          borderwidth)

    @classmethod
    def EditorScreen(cls):
        pygame.draw.rect(editorscreen, Render.BLUE, screensize)
        editorscreen.fill(Render.BLUE)
        MiPi.enginescreen.blit(editorscreen, (50, 185))
