# This is my MiPi module, it will contain the MiPi class and all of its
# Functions, methods and variables.

import pygame
from pygame import *
import pygame_gui
from pygame_gui import *
import logging
import datetime

# Initialize pygame
pygame.init()

# --------------------------------- All Global Variables ----------------------------------------------------#
# Color constants
GREEN = (0, 255, 0)
NOCOLOR = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)
DARKGRAY = (169, 169, 169)
LIGHTCOLOR = (170, 170, 170)
DARKSHADE = (100, 100, 100)
# Fonts
CorbelFont = pygame.font.SysFont('Corbel', 35)
guitext = CorbelFont.render('File', True, WHITE)
# Vertices, vertexes and sizes
verts = [(50, 0), (100, 50), (50, 50), (0, 50)]
size = (800, 625)

# Creating the dimensions for the game play screen
width = 800
height = 625

# Creating the dimensions for the main engine frame
ewidth = 800
eheight = 625

# Datetime vars
current_date = datetime.datetime.now()
# Engine screens
gamescreen = pygame.display.set_mode((width, height))
enginescreen = pygame.display.set_mode((ewidth, eheight))

# Main engine variables and constants
mainframe = pygame_gui.UIManager((800, 625))
sysclock = pygame.time.Clock()
mainFPS = 60
# Main engine frame settings
engine_title = "MiPi Engine"
pygame.display.set_caption(engine_title)
# Game window settings
game_title = "Gameplay Test"
# Pygame_gui UI elements
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 150), (100, 50)),
                                           text='Test Game', manager=mainframe)
dropmenu = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((25, 25), (400, 50)), starting_option=
                                              "File", options_list=["Run", "Close"], manager=mainframe)
# Running state vars
game_running = False
engine_running = True

# ---------------------------------------------------------------------------------------------------------#

class MiPi:
    def __init__(self):
        self

    @staticmethod
    def MainFunctions():

        delta_time = sysclock.tick(mainFPS) / 1000.0
        game_running = False
        engine_running = True

        while engine_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    engine_running = False

                enginescreen.fill(LIGHTCOLOR)

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
                        if event.ui_element == play_button:
                            print(current_date, "Gameplay test window has been launched!")
                            engine_running = False
                            game_running = True

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                        if event.text == "Run":
                            print(current_date, "Gameplay test window has been launched!")
                            engine_running = False
                            game_running = True
                        else:
                            print("Menu not found!")

                mainframe.process_events(event)
                mainframe.draw_ui(enginescreen)
                mainframe.update(delta_time)

            pygame.display.update()
            pygame.display.flip()


        while game_running:
            for game in pygame.event.get():
                if game.type == pygame.QUIT:
                    game_running = False

                mainframe.process_events(game)
                enginescreen.fill(NOCOLOR)
                gamescreen.fill(DARKGRAY)
                pygame.display.set_caption(game_title)
                MiPi.DrawTriangle()
                mainframe.update(delta_time)

            pygame.display.flip()
            pygame.display.update()

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
        gamescreen.blit(triangle, (0, 0))
        pygame.display.update()

