import pygame
from pygame import *
import pygame_gui
from pygame_gui import *

# Global vars
mainframe = pygame_gui.UIManager((800, 625))

# Pygame_gui UI elements
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((475, 25), (100, 50)),
                                           text='Test Game', manager=mainframe)

dropmenu = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((20, 25), (400, 50)), starting_option=
                                              "File", options_list=["Run", "Import Sprite", "Close"], manager=mainframe)