# This is my MiPi module, it will contain the MiPi class and all of its
# Functions, methods and variables.

# For the file system see the example from the pygame_gui devs github:
# https://github.com/MyreMylar/pygame_gui_examples/blob/master/file_dialog_test.py

import pygame
from pygame import *
import pygame_gui
from pygame_gui.core.utility import create_resource_path
from pygame_gui.elements import UIImage
from pygame_gui import *
import logging
import datetime
import Render
import MiPiGUI
from MiPiGUI import *
import MiPiSettings
from MiPiSettings import *

# Initialize pygame
pygame.init()

# --------------------------------- All Global Variables ----------------------------------------------------#
# Fonts
CorbelFont = pygame.font.SysFont('Corbel', 35)
guitext = CorbelFont.render('File', True, Render.WHITE)
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
gamescreen = pygame.display.set_mode((width, height), 0, 32)
enginescreen = pygame.display.set_mode((ewidth, eheight))

# Main engine variables and constants
sysclock = pygame.time.Clock()
mainFPS = 110
delta_time = sysclock.tick(mainFPS) / 1000.0
# Main engine frame settings
engine_title = "MiPi Engine"
pygame.display.set_caption(engine_title)
# Game window settings
game_title = "Gamescreen"

# Custom logging levels:
editor_error = ': The editor has no content to pass to the game screen!'

# File paths
# D:/dev/pythondev/MiPiEngine/MiPiEngine

warning = ('I appologize for the inconvenience, but this engine only works on Windows! Also, make sure all'
           ' of your assets used are in C:/ drive. I currently have no workaround for this...')

# Get slider values
getspritex = None
getspritey = None


# ---------------------------------------------------------------------------------------------------------#

class MiPi:
    def __init__(self):
        self

    @classmethod
    def Main(cls):
        game_running = False
        engine_running = True
        speed = 5
        pos_x = 0
        pos_y = 0
        editableContent = False
        edMouseX = 0
        edMouseY = 0
        inputx = 0
        inputy = 0

        Render.Shapes.CreateTriangle()

        while engine_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    engine_running = False

                enginescreen.fill(Render.LIGHTCOLOR)
                MiPiGUI.GUI.EditorScreen()

                # edMouseX, edMouseY = pygame.mouse.get_pos()
                # MiPiGUI Labels
                enginescreen.blit(MiPiGUI.editorlabel, MiPiGUI.editorborder)
                enginescreen.blit(MiPiGUI.spritelocationlabel, MiPiGUI.spriteborder)
                enginescreen.blit(MiPiGUI.xlabel, MiPiGUI.xborder)
                enginescreen.blit(MiPiGUI.ylabel, MiPiGUI.yborder)

                spritexlabel = MiPiGUI.smallfont.render(MiPiGUI.textx, True, Render.WHITE, Render.DARKSHADE)
                spritexborder = spritexlabel.get_rect()
                spritexborder.center = (500, 185)
                enginescreen.blit(spritexlabel, spritexborder)

                spriteylabel = MiPiGUI.smallfont.render(MiPiGUI.texty, True, Render.WHITE, Render.DARKSHADE)
                spriteyborder = spriteylabel.get_rect()
                spriteyborder.center = (600, 185)
                enginescreen.blit(spriteylabel, spriteyborder)

                # UI Horizontal sliders
                MiPiGUI.xlocbar.enable()
                MiPiGUI.ylocbar.enable()

                # Get current slider values
                getspritex = MiPiGUI.xlocbar.get_current_value()
                getspritey = MiPiGUI.ylocbar.get_current_value()
                MiPiGUI.textx = str(getspritex)
                MiPiGUI.texty = str(getspritey)

                # if event.type == pygame.MOUSEMOTION:
                # print("X: %d, Y: %d" % (edMouseX, edMouseY))

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
                        if event.ui_element == MiPiGUI.play_button:
                            if not MiPiSettings.editor_has_content:
                                print(current_date, editor_error)
                                logging.warning(current_date, editor_error)
                            else:
                                print(current_date, "Gameplay test window has been launched!")
                                engine_running = False
                                game_running = True

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                        if event.text == "Run":
                            print(current_date, "Gamescreen window has been launched!")
                            engine_running = False
                            game_running = True
                        if event.text == "Close":
                            print(current_date, "Application has been closed")
                            engine_running = False
                            game_running = False
                        else:
                            print(current_date, "Application failed to close")
                        if event.text == "Import Sprite":
                            spritemenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                rect=pygame.Rect((200, 200), (260, 300)),
                                manager=MiPiGUI.mainframe, window_title="Select a sprite file",
                                initial_file_path="C:/",
                                allow_existing_files_only=True, visible=True)
                            MiPiSettings.editableSprite = True

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                        if MiPiGUI.import_sprite is not None:
                            MiPiGUI.import_sprite.kill()

                        try:
                            MiPiSettings.sprite_path = create_resource_path(event.text)
                            MiPiSettings.sprite_image = pygame.image.load(MiPiSettings.sprite_path).convert_alpha()
                            sprite_rect = MiPiSettings.sprite_image.get_rect()
                            aspect_ratio = sprite_rect.width / sprite_rect.height
                            scalability = False

                            if sprite_rect.width > MiPiGUI.max_image_display_dimensions[0]:
                                sprite_rect.width = MiPiGUI.max_image_display_dimensions[0]
                                sprite_rect.height = int(sprite_rect.width / aspect_ratio)
                                scalability = True

                            if sprite_rect.height > MiPiGUI.max_image_display_dimensions[1]:
                                sprite_rect.height = MiPiGUI.max_image_display_dimensions[1]
                                sprite_rect.width = int(sprite_rect.height * aspect_ratio)
                                scalability = True

                            if scalability:
                                MiPiSettings.sprite_image = pygame.transform.smoothscale(MiPiSettings.sprite_image,
                                                                                         sprite_rect.size)

                            # Boundary values are subject to change based on image size and scaling!
                            # Make these values editable in a gui by the user: x range: 80-400
                            # y range: 215-425  Best default: 80,425
                            inputx = 80
                            inputy = 215
                            x = inputx
                            y = inputy

                            # Get current slider values
                            getspritex = MiPiGUI.xlocbar.get_current_value()
                            getspritey = MiPiGUI.ylocbar.get_current_value()
                            MiPiGUI.textx = str(getspritex)
                            MiPiGUI.texty = str(getspritey)

                            x = getspritex
                            y = getspritey

                            sprite_rect.x = x
                            sprite_rect.y = y

                            if sprite_rect.x < 80 or sprite_rect.x > 400:
                                print("Value out of range! Setting to default")
                                sprite_rect.x = 80

                            if sprite_rect.y < 215 or sprite_rect.y > 425:
                                print("Value out of range! Setting to default")
                                sprite_rect.y = 425

                            sprite_rect.center = (sprite_rect.x, sprite_rect.y)

                            # UI manager mainframe has now been created after pygame.init()
                            # Thank you MyreMylar(pygame_gui) for your help in spotting this :)
                            # Currently see line 14 of MiPiGUI file for pygame.init()
                            MiPiGUI.import_sprite = UIImage(relative_rect=sprite_rect,
                                                            image_surface=MiPiSettings.sprite_image,
                                                            manager=MiPiGUI.mainframe)

                            MiPiSettings.editor_has_content = True

                        except pygame.error:
                            pass

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        engine_running = False

                # Updates: Tried de-indenting MiPiGUI updates, but this caused instability in all
                # looped events including gui elements. Also tried setting updates in a method, but
                # this caused pygame.event to throw an error. So instead, I indented pygame display
                # updates and everything seems to still work correctly. Will keep an eye on updates.
                # I did notice that de-indenting update methods will put them outside the main engine's
                # while loop. For now, just gonna keep them in the while loop unless I can find a
                # workaround.
                MiPiGUI.mainframe.process_events(event)
                MiPiGUI.mainframe.draw_ui(enginescreen)
                MiPiGUI.mainframe.update(delta_time)
                pygame.display.flip()
                pygame.display.update()

        while game_running:
            for game in pygame.event.get():
                if game.type == pygame.QUIT:
                    pygame.display.set_caption(engine_title)
                    MiPi.Main()
                    game_running = False

                gamescreen.fill(Render.BLUE)

                pygame.key.set_repeat(1, 10)  # Not a friendly way of movement while key is held down, but works!
                # Movement loop
                if game.type == pygame.KEYDOWN:
                    if game.key == pygame.K_LEFT:
                        pos_x -= speed
                        print("Left key pressed")
                    if game.key == pygame.K_RIGHT:
                        pos_x += speed
                        print("Right key pressed")
                    if game.key == pygame.K_UP:
                        pos_y -= speed
                        print("Up key pressed")
                    if game.key == pygame.K_DOWN:
                        pos_y += speed
                        print("Down key pressed")
                elif game.type == pygame.KEYUP:
                    if game.key == pygame.K_LEFT:
                        pos_x -= 0
                        print("Left key released")
                    if game.key == pygame.K_RIGHT:
                        pos_x += 0
                        print("Right key released")
                    if game.key == pygame.K_UP:
                        pos_y -= 0
                        print("Up key released")
                    if game.key == pygame.K_DOWN:
                        pos_y += 0
                        print("Down key released")
                    if game.key == pygame.K_ESCAPE:
                        pygame.display.set_caption(engine_title)
                        MiPi.Main()
                        game_running = False

                pygame.display.set_caption(game_title)
                # MiPi.RenderTest(pos_x, pos_y)
                MiPi.LoadSprite(pos_x, pos_y)
                # The below is commented out, because UI is NOT being drawn to the game screen.
                # If you decide to add pygame_gui UI elements, then please use these!
                # mainframe.process_events(game)
                # mainframe.update(delta_time)
                sysclock.tick(mainFPS)
                pygame.display.flip()
                pygame.display.update()

        return MiPiSettings.sprite_image, MiPiSettings.sprite_path

    @classmethod
    def RenderTest(cls, x, y):
        gamescreen.blit(Render.triangle, (x, y))

    @classmethod
    def LoadSprite(cls, x, y):
        try:
            loadsprite = MiPiSettings.sprite_image
            gamescreen.blit(loadsprite, (x, y))
            if loadsprite is None:
                print(editor_error)
        except IOError as e:
            pass

    @staticmethod
    def EngineInit():
        # This method is called upon starting the MiPi engine
        print(warning)
        logging.basicConfig(filename='mipi.log', level=logging.INFO)
        print(current_date, ": MiPi Engine v1.0 has been initialized")
        logging.info(current_date)
        logging.info("MiPi Engine v1.0 has been initialized.")
