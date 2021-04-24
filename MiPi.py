# MiPi Engine alpha v1.3 - © Aaron Keith Sanders - All Rights Reserved

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
import platform
import os
import random

# Initialize pygame
from MiPiEngine import MiPiPhysics

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

# Message to be displayed when something isn't finished yet
inprogress = 'This feature is still in development'

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
engine_title = "MiPi Engine alpha v1.3 - © Aaron Keith Sanders"
pygame.display.set_caption(engine_title)
# Game window settings
game_title = "Gamescreen"

# Custom logging levels:
editor_error = ': The editor has no content to pass to the game screen!'

# File paths
# D:/dev/pythondev/MiPiEngine/MiPiEngine


# Get slider values
getspritex = None
getspritey = None

e_moverandx = 0
e_moverandy = 0

configuresize = ''
box_x = 200
box_y = 200

col_range_x = range(170, 200)
col_range_y = range(200, 220)


# ---------------------------------------------------------------------------------------------------------#

class MiPi:
    def __init__(self, msg):
        self.msg = ''

    @classmethod
    def Main(cls):
        game_running = False
        engine_running = True
        speed_x = 5
        speed_y = 5
        player_pos_x = (MiPiGUI.g_screen_x * MiPiSettings.playerx_to_editor)
        player_pos_y = (MiPiGUI.g_screen_y * MiPiSettings.playery_to_editor)
        npc_pos_x = (MiPiGUI.g_screen_x * MiPiSettings.npcx_to_editor)
        npc_pos_y = (MiPiGUI.g_screen_y * MiPiSettings.npcy_to_editor)
        MiPiSettings.enemy_x = 800 / 2
        MiPiSettings.enemy_y = 600 / 2
        e_moverandx = 0
        e_moverandy = 0
        editableContent = False
        edMouseX = 0
        edMouseY = 0
        inputx = 0
        inputy = 0
        m_forwards = 'moving forwards'
        m_backwards = 'moving backwards'
        m_up = 'moving up'
        m_down = 'moving down'
        currentposition = ''
        Render.Shapes.CreateTriangle()
        MiPiPhysics.Player.BoxCollider2D(enginescreen, Render.GREEN, 30, 30, 60, 60)

        while engine_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    engine_running = False

                enginescreen.fill(Render.LIGHTCOLOR)
                MiPiGUI.GUI.EditorScreen()
                MiPiGUI.GUI.MiPiBorders(enginescreen, Render.DARKSHADE, 45, 176, 385, 292, 15)
                enginescreen.blit(MiPiGUI.editorlabel, MiPiGUI.editorborder)
                enginescreen.blit(MiPiGUI.engineborder_north, MiPiGUI.set_engineborder_north)
                enginescreen.blit(MiPiGUI.engineborder_south, MiPiGUI.set_engineborder_south)

                # edMouseX, edMouseY = pygame.mouse.get_pos()
                # MiPiGUI Labels

                MiPi.EditSprite()

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
                        if event.text == "Import Sprite":
                            MiPiGUI.spritesubmenu.show()

                        # ------------------------ Import Sprite --------------------------------------------------#
                        if event.text == "Player":
                            if platform.system() == MiPiSettings.Windows:
                                MiPiGUI.playermenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                    rect=pygame.Rect((200, 200), (260, 300)),
                                    manager=MiPiGUI.mainframe, window_title="Select a player sprite",
                                    initial_file_path="C:/",
                                    allow_existing_files_only=True, visible=True)
                                MiPiSettings.playersprite = True
                                MiPiSettings.editablePlayerSprite = True
                                MiPiSettings.editableNPCSprite = False
                                MiPi.EraseUI()
                                MiPiGUI.spritesubmenu.hide()
                            elif platform.system() == MiPiSettings.Mac:
                                MiPiGUI.playermenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                    rect=pygame.Rect((200, 200), (260, 300)),
                                    manager=MiPiGUI.mainframe, window_title="Select a player sprite",
                                    initial_file_path="~/Desktop",
                                    allow_existing_files_only=True, visible=True)
                                MiPiSettings.playersprite = True
                                MiPiSettings.editablePlayerSprite = True
                                MiPiSettings.editableNPCSprite = False
                                MiPiGUI.spritesubmenu.hide()
                            elif platform.system() == MiPiSettings.Linux:
                                MiPiGUI.playermenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                    rect=pygame.Rect((200, 200), (260, 300)),
                                    manager=MiPiGUI.mainframe, window_title="Select a player sprite",
                                    initial_file_path="/bin",
                                    allow_existing_files_only=True, visible=True)
                                MiPiSettings.playersprite = True
                                MiPiSettings.editablePlayerSprite = True
                                MiPiSettings.editableNPCSprite = False
                                MiPiGUI.spritesubmenu.hide()
                            else:
                                print(current_date, MiPiSettings.platform_error)
                                logging.warning(current_date, MiPiSettings.platform_error)

                        if event.text == "NPC":
                            MiPiGUI.npcmenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                rect=pygame.Rect((200, 200), (260, 300)),
                                manager=MiPiGUI.mainframe, window_title="Select an npc sprite",
                                initial_file_path="C:/",
                                allow_existing_files_only=True, visible=True)

                            MiPi.UnderDev(MiPiSettings.underdevelopment)
                            MiPiSettings.npcsprite = True
                            MiPiSettings.editableNPCSprite = True
                            MiPiSettings.editablePlayerSprite = False
                            MiPi.EraseUI()
                            MiPiGUI.spritesubmenu.hide()
                        if event.text == "Object":
                            MiPi.UnderDev(MiPiSettings.underdevelopment)
                            MiPiGUI.spritesubmenu.hide()
                        # ------------------------ Import Sprite --------------------------------------------------#

                        # -------------- Import Tilemap -----------------------------------------------------------#

                        if event.text == "Import Tilemap":
                            print(MiPiSettings.underdevelopment)
                            if platform.system() == MiPiSettings.Windows:
                                MiPiGUI.tilemapmenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                    rect=pygame.Rect((200, 200), (260, 300)),
                                    manager=MiPiGUI.mainframe, window_title="Select a tilemap",
                                    initial_file_path="C:/",
                                    allow_existing_files_only=True, visible=True)
                                MiPiSettings.tilemap_chosen = True
                                MiPiSettings.tilemap_ready = True
                            elif platform.system() == MiPiSettings.Mac:
                                MiPiGUI.tilemapmenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                    rect=pygame.Rect((200, 200), (260, 300)),
                                    manager=MiPiGUI.mainframe, window_title="Select a tilemap",
                                    initial_file_path="~/Desktop",
                                    allow_existing_files_only=True, visible=True)
                                MiPiSettings.tilemap_chosen = True
                                MiPiSettings.tilemap_ready = True
                            elif platform.system() == MiPiSettings.Linux:
                                MiPiGUI.tilemapmenu = pygame_gui.windows.ui_file_dialog.UIFileDialog(
                                    rect=pygame.Rect((200, 200), (260, 300)),
                                    manager=MiPiGUI.mainframe, window_title="Select a tilemap",
                                    initial_file_path="/bin",
                                    allow_existing_files_only=True, visible=True)
                                MiPiSettings.tilemap_chosen = True
                                MiPiSettings.tilemap_ready = True
                            else:
                                print(current_date, MiPiSettings.platform_error)
                                logging.warning(current_date, MiPiSettings.platform_error)

                        # -------------- Import Tilemap -----------------------------------------------------------#

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:

                        # ----------- NPC Sprite Import --------------------------------------------------------------#
                        if MiPiSettings.npcsprite:
                            try:
                                if not MiPiSettings.playersprite_available:
                                    print("Import  a player sprite first: <- Replace this with a message box!")
                                else:
                                    MiPiSettings.npc_path = create_resource_path(event.text)
                                    MiPiSettings.npc_img = pygame.image.load(MiPiSettings.npc_path).convert_alpha()
                                    npc_rect = MiPiSettings.npc_img.get_rect()
                                    aspect_ratio = npc_rect.width / npc_rect.height
                                    scalability = False

                                    if npc_rect.width > MiPiGUI.max_image_display_dimensions[0]:
                                        npc_rect.width = MiPiGUI.max_image_display_dimensions[0]
                                        npc_rect.height = int(npc_rect.width / aspect_ratio)
                                        scalability = True

                                    if npc_rect.height > MiPiGUI.max_image_display_dimensions[1]:
                                        npc_rect.height = MiPiGUI.max_image_display_dimensions[1]
                                        npc_rect.width = int(npc_rect.height * aspect_ratio)
                                        scalability = True

                                    if scalability:
                                        MiPiSettings.npc_img = pygame.transform.smoothscale(MiPiSettings.npc_img,
                                                                                            npc_rect.size)

                                    # Boundary values are subject to change based on image size and scaling!
                                    # Make these values editable in a gui by the user: x range: 80-400
                                    # y range: 215-425  Best default: 80,425

                                    npcinputx = 80
                                    npcinputy = 215
                                    npcx = npcinputx
                                    npcy = npcinputy

                                    # Get current slider values
                                    getnpcspritex = MiPiGUI.npcxlocbar.get_current_value()
                                    getnpcspritey = MiPiGUI.npcylocbar.get_current_value()
                                    MiPiGUI.npctextx = str(getnpcspritex)
                                    MiPiGUI.npctexty = str(getnpcspritey)
                                    MiPiGUI.npcxlocbar.update(delta_time)
                                    MiPiGUI.npcylocbar.update(delta_time)

                                    npcx = getnpcspritex
                                    npcy = getnpcspritey

                                    npc_rect.x = npcx
                                    npc_rect.y = npcy

                                    if npc_rect.x < 80 or npc_rect.x > 400:
                                        print("Value out of range! Setting to default")
                                        npc_rect.x = 80

                                    if npc_rect.y < 215 or npc_rect.y > 425:
                                        print("Value out of range! Setting to default")
                                        npc_rect.y = 425

                                    npc_rect.center = (npc_rect.x, npc_rect.y)

                                    # UI manager mainframe has now been created after pygame.init()
                                    # Thank you MyreMylar(pygame_gui) for your help in spotting this :)
                                    # Currently see line 14 of MiPiGUI file for pygame.init()
                                    MiPiSettings.import_npc_sprite = UIImage(relative_rect=npc_rect,
                                                                             image_surface=MiPiSettings.npc_img,
                                                                             manager=MiPiGUI.mainframe)

                                    MiPiSettings.npcx_to_editor = (npc_rect.x / 400)
                                    MiPiSettings.npcy_to_editor = (npc_rect.y / 425)
                                    npc_pos_x = (MiPiGUI.g_screen_x * MiPiSettings.npcx_to_editor)
                                    npc_pos_y = (MiPiGUI.g_screen_y * MiPiSettings.npcy_to_editor)
                                    npc_pos_x = npc_pos_x - MiPiSettings.offset_x
                                    npc_pos_y = npc_pos_y - MiPiSettings.offset_y

                                    MiPiSettings.npcsprite = False
                                    MiPiSettings.editor_has_content = True

                            except pygame.error:
                                pass
                        # --------------------------------------------------------------------------------------------#

                        if MiPiSettings.tilemap_chosen:
                            try:

                                MiPiSettings.tile_path = create_resource_path(event.text)
                                MiPiSettings.tilemap_img = pygame.image.load(MiPiSettings.tile_path).convert_alpha()
                                tilemap_rect = MiPiSettings.tilemap_img.get_rect()
                                scalability = False

                                if tilemap_rect.width >= MiPiGUI.max_image_display_dimensions[0]:
                                    tilemap_rect.width = MiPiGUI.edwidth
                                    tilemap_rect.height = MiPiGUI.edheight
                                    scalability = True

                                if tilemap_rect.height > MiPiGUI.max_image_display_dimensions[1]:
                                    tilemap_rect.height = MiPiGUI.tilemap_height
                                    tilemap_rect.width = MiPiGUI.tilemap_width
                                    scalability = True

                                if tilemap_rect.width <= MiPiGUI.max_image_display_dimensions[0]:
                                    tilemap_rect.width = MiPiGUI.tilemap_width
                                    tilemap_rect.height = MiPiGUI.tilemap_height
                                    scalability = True

                                if tilemap_rect.height < MiPiGUI.max_image_display_dimensions[1]:
                                    tilemap_rect.height = MiPiGUI.tilemap_height
                                    tilemap_rect.width = MiPiGUI.tilemap_width
                                    scalability = True

                                if scalability:
                                    MiPiSettings.tilemap_img = pygame.transform.smoothscale(MiPiSettings.tilemap_img,
                                                                                            tilemap_rect.size)

                                tilemap_rect.x = 238
                                tilemap_rect.y = 321
                                tilemap_rect.center = (tilemap_rect.x, tilemap_rect.y)

                                MiPiSettings.import_tilemap = UIImage(relative_rect=tilemap_rect,
                                                                      image_surface=MiPiSettings.tilemap_img,
                                                                      manager=MiPiGUI.mainframe)

                                MiPiSettings.tilemap_chosen = False
                                MiPiSettings.tilemap_available = True
                            except pygame.error:
                                pass

                        # ----------- Player Sprite Import -----------------------------------------------------------#
                        if MiPiSettings.playersprite:
                            try:
                                if not MiPiSettings.tilemap_available:
                                    print("Please import a tilemap first! <- Replace this with a message box!")
                                if MiPiSettings.playersprite_available:
                                    print("Player sprite available. <- Replace this with a message box!")
                                else:
                                    MiPiSettings.sprite_path = create_resource_path(event.text)
                                    MiPiSettings.player_img = pygame.image.load(
                                        MiPiSettings.sprite_path).convert_alpha()
                                    sprite_rect = MiPiSettings.player_img.get_rect()
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
                                        MiPiSettings.player_img = pygame.transform.smoothscale(MiPiSettings.player_img,
                                                                                               sprite_rect.size)

                                    # Removes any duplicate copies of player sprites in the editor
                                    if MiPiSettings.player_removeduplicates >= 1:
                                        MiPiSettings.player_img.fill(Render.TRANSPARENCY)
                                        MiPiSettings.player_removeduplicates = 0

                                    # Boundary values are subject to change based on image size and scaling!
                                    # Make these values editable in a gui by the user: x range: 80-400
                                    # y range: 215-425  Best default: 80,425

                                    inputx = 80
                                    inputy = 215
                                    x = inputx
                                    y = inputy

                                    # Get current slider values
                                    getspritex = MiPiGUI.playerxlocbar.get_current_value()
                                    getspritey = MiPiGUI.playerylocbar.get_current_value()
                                    MiPiGUI.textx = str(getspritex)
                                    MiPiGUI.texty = str(getspritey)
                                    MiPiGUI.playerxlocbar.update(delta_time)
                                    MiPiGUI.playerylocbar.update(delta_time)

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
                                    MiPiSettings.import_player_sprite = UIImage(relative_rect=sprite_rect,
                                                                                image_surface=MiPiSettings.player_img,
                                                                                manager=MiPiGUI.mainframe)

                                    MiPiSettings.playerx_to_editor = (sprite_rect.x / 400)
                                    MiPiSettings.playery_to_editor = (sprite_rect.y / 425)
                                    player_pos_x = (MiPiGUI.g_screen_x * MiPiSettings.playerx_to_editor)
                                    player_pos_y = (MiPiGUI.g_screen_y * MiPiSettings.playery_to_editor)
                                    player_pos_x = player_pos_x - MiPiSettings.offset_x
                                    player_pos_y = player_pos_y - MiPiSettings.offset_y

                                    MiPiSettings.playersprite_available = True
                                    MiPiSettings.playersprite = False
                                    MiPiSettings.editor_has_content = True

                            except pygame.error:
                                pass
                        # --------------------------------------------------------------------------------------------#

                    # ------------------- UPDATE PLAYER BUTTON CONTROLS ---------------------------------------------------#
                    if event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
                        if event.ui_element == MiPiGUI.updateplayer_button:
                            print(inprogress)
                            MiPiSettings.import_player_sprite.hide()

                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == MiPiGUI.updateplayer_button:
                            change_rect = MiPiSettings.player_img.get_rect()
                            movex = MiPiGUI.playerxlocbar.get_current_value()
                            movey = MiPiGUI.playerylocbar.get_current_value()
                            change_rect.x = movex
                            change_rect.y = movey
                            change_rect.center = (change_rect.x, change_rect.y)
                            MiPiSettings.import_player_sprite = UIImage(relative_rect=change_rect,
                                                                        image_surface=MiPiSettings.player_img,
                                                                        manager=MiPiGUI.mainframe)

                            MiPiSettings.playerx_to_editor = (change_rect.x / 400)
                            MiPiSettings.playery_to_editor = (change_rect.y / 425)
                            player_pos_x = (MiPiGUI.g_screen_x * MiPiSettings.playerx_to_editor)
                            player_pos_y = (MiPiGUI.g_screen_y * MiPiSettings.playery_to_editor)
                            player_pos_x = player_pos_x - MiPiSettings.offset_x
                            player_pos_y = player_pos_y - MiPiSettings.offset_y

                            getspritex = MiPiGUI.playerxlocbar.get_current_value()
                            getspritey = MiPiGUI.playerylocbar.get_current_value()
                            MiPiGUI.textx = str(getspritex)
                            MiPiGUI.texty = str(getspritey)
                            MiPiGUI.playerxlocbar.update(delta_time)
                            MiPiGUI.playerylocbar.update(delta_time)

                    # ----------------------------------------------------------------------------------------------------#

                    # ------------------- UPDATE NPC BUTTON CONTROLS -----------------------------------------------------#

                    if event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
                        if event.ui_element == MiPiGUI.updatenpc_button:
                            print(inprogress)
                            MiPiSettings.import_npc_sprite.hide()

                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == MiPiGUI.updatenpc_button:
                            change_rect_npc = MiPiSettings.npc_img.get_rect()
                            movenpcx = MiPiGUI.npcxlocbar.get_current_value()
                            movenpcy = MiPiGUI.npcylocbar.get_current_value()
                            change_rect_npc.x = movenpcx
                            change_rect_npc.y = movenpcy
                            change_rect_npc.center = (change_rect_npc.x, change_rect_npc.y)
                            MiPiSettings.import_npc_sprite = UIImage(relative_rect=change_rect_npc,
                                                                     image_surface=MiPiSettings.npc_img,
                                                                     manager=MiPiGUI.mainframe)

                            MiPiSettings.npcx_to_editor = (change_rect_npc.x / 400)
                            MiPiSettings.npcy_to_editor = (change_rect_npc.y / 425)
                            npc_pos_x = (MiPiGUI.g_screen_x * MiPiSettings.npcx_to_editor)
                            npc_pos_y = (MiPiGUI.g_screen_y * MiPiSettings.npcy_to_editor)
                            npc_pos_x = npc_pos_x - MiPiSettings.offset_x
                            npc_pos_y = npc_pos_y - MiPiSettings.offset_y

                            getnpcspritex = MiPiGUI.npcxlocbar.get_current_value()
                            getnpcspritey = MiPiGUI.npcylocbar.get_current_value()
                            MiPiGUI.npctextx = str(getnpcspritex)
                            MiPiGUI.npctexty = str(getnpcspritey)
                            MiPiGUI.npcxlocbar.update(delta_time)
                            MiPiGUI.npcylocbar.update(delta_time)

                # ----------------------------------------------------------------------------------------------------#

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

                # The screen gets rendered a color to be tested regardless if a tilemap is ready to be tested.
                gamescreen.fill(Render.BLUE)
                # Collider box2D
                MiPi.DrawBoxCol(box_x, box_y)
                # Remove this later
                MiPi.ShowPlayerPos(player_pos_x, player_pos_y)

                # If the user has placed a tilemap and is ready to test with a tilemap, then blit it to the test screen
                if MiPiSettings.tilemap_ready:
                    gamescreen.blit(
                        pygame.transform.scale(MiPiSettings.tilemap_img, (MiPiGUI.g_screen_x, MiPiGUI.g_screen_y)),
                        (0, 0))

                # Player movement boundaries
                if player_pos_x > MiPiGUI.g_screen_x - 1:
                    player_pos_x = 0
                elif player_pos_x < 0:
                    player_pos_x = MiPiGUI.g_screen_x

                if player_pos_y > MiPiGUI.g_screen_y - 1:
                    player_pos_y = 0
                elif player_pos_y < 0:
                    player_pos_y = MiPiGUI.g_screen_y

                # Enemy movement boundaries
                if MiPiSettings.enemy_x > MiPiGUI.g_screen_x - 1:
                    MiPiSettings.enemy_x = 0
                elif MiPiSettings.enemy_x < 0:
                    MiPiSettings.enemy_x = MiPiGUI.g_screen_x

                if MiPiSettings.enemy_y > MiPiGUI.g_screen_y - 1:
                    MiPiSettings.enemy_y = 0
                elif MiPiSettings.enemy_y < 0:
                    MiPiSettings.enemy_y = MiPiGUI.g_screen_y

                e_moverandx = random.randint(1, 3)
                e_moverandy = random.randint(4, 6)

                if 1 <= e_moverandx <= 2:
                    MiPiSettings.enemy_x -= MiPiSettings.enemy_speed
                elif e_moverandx == 3:
                    MiPiSettings.enemy_x += MiPiSettings.enemy_speed

                if 4 <= e_moverandy <= 5:
                    MiPiSettings.enemy_y -= MiPiSettings.enemy_speed
                elif e_moverandy == 6:
                    MiPiSettings.enemy_y += MiPiSettings.enemy_speed

                pygame.key.set_repeat(1, 10)  # Not a friendly way of movement while key is held down, but works!
                # Movement loop
                if game.type == pygame.KEYDOWN:
                    if game.key == pygame.K_LEFT:
                        player_pos_x -= speed_x
                        print("(<) Left key pressed", currentposition)
                        currentposition = m_backwards
                    if game.key == pygame.K_RIGHT:
                        player_pos_x += speed_x
                        print("(>) Right key pressed", currentposition)
                        currentposition = m_forwards
                    if game.key == pygame.K_UP:
                        player_pos_y -= speed_y
                        print("(^) Up key pressed", currentposition)
                        currentposition = m_up
                    if game.key == pygame.K_DOWN:
                        player_pos_y += speed_y
                        print("(v)Down key pressed", currentposition)
                        currentposition = m_down
                    if game.key == pygame.K_a:
                        player_pos_x -= speed_x
                        print("(a) Left key pressed", currentposition)
                        currentposition = m_backwards
                    if game.key == pygame.K_d:
                        player_pos_x += speed_x
                        print("(d) Right key pressed", currentposition)
                        currentposition = m_forwards
                    if game.key == pygame.K_w:
                        player_pos_y -= speed_y
                        print("(w) Up key pressed", currentposition)
                        currentposition = m_up
                    if game.key == pygame.K_s:
                        player_pos_y += speed_y
                        print("(s) Down key pressed", currentposition)
                        currentposition = m_down
                    # Collisions ------------------------------------
                    if player_pos_x in range(170, 200) and player_pos_y in range(170, 200):
                        print('Player is in collision RANGE!')
                        if currentposition == m_forwards and game.key == pygame.K_RIGHT or game.key == pygame.K_d:
                            player_pos_x = 170
                            speed_x = 0
                        elif game.key == pygame.K_a:
                            speed_x = 5
                            player_pos_x -= speed_x
                        elif game.key == pygame.K_LEFT:
                            speed_x = 5
                            player_pos_x -= speed_x

                elif game.type == pygame.KEYUP:
                    if game.key == pygame.K_LEFT:
                        player_pos_x -= 0
                        print("Left key released")
                    if game.key == pygame.K_RIGHT:
                        player_pos_x += 0
                        print("Right key released")
                    if game.key == pygame.K_UP:
                        player_pos_y -= 0
                        print("Up key released")
                    if game.key == pygame.K_DOWN:
                        player_pos_y += 0
                        print("Down key released")
                    if game.key == pygame.K_ESCAPE:
                        pygame.display.set_caption(engine_title)
                        MiPi.Main()
                        game_running = False

                MiPi.DrawBoxCol(box_x, box_y)
                MiPi.CheckForCollision(box_x, box_y, player_pos_x)

                pygame.display.set_caption(game_title)
                # MiPi.RenderTest(player_pos_x, player_pos_y)
                MiPi.LoadPlayer(player_pos_x, player_pos_y)
                MiPi.LoadNPC(npc_pos_x, npc_pos_y)
                # MiPi.LoadEnemy(MiPiSettings.enemy_x, MiPiSettings.enemy_y)

                # The below is commented out, because UI is NOT being drawn to the game screen.
                # If you decide to add pygame_gui UI elements, then please use these!
                # mainframe.process_events(game)
                # mainframe.update(delta_time)

                sysclock.tick(mainFPS)
                pygame.display.flip()
                pygame.display.update()

        return MiPiSettings.player_img, MiPiSettings.sprite_path, \
               MiPiSettings.npc_img, MiPiSettings.npc_path, player_pos_x

    @classmethod
    def ShowPlayerPos(cls, x, y):
        print('player_x:', x, 'player_y:', y)

    @classmethod
    def RenderTest(cls, x, y):
        gamescreen.blit(Render.triangle, (x, y))

    @classmethod
    def DrawBoxCol(cls, x, y):
        enginescreen.blit(MiPiPhysics.Player.boxsurface, (x, y))

    @classmethod
    def CheckForCollision(cls, x, y, player_x):
        if player_x == box_x:
            print('collision has occured at:', box_x, 'x')

    @classmethod
    def LoadPlayer(cls, x, y):
        try:
            loadplayer = MiPiSettings.player_img
            gamescreen.blit(loadplayer, (x, y))
            if loadplayer is None:
                print(editor_error)
        except IOError as e:
            pass

    @classmethod
    def LoadNPC(cls, x, y):
        try:
            loadnpc = MiPiSettings.npc_img
            gamescreen.blit(loadnpc, (x, y))
            if loadnpc is None:
                print(editor_error)
        except IOError as e:
            pass

    @classmethod
    def LoadTilemap(cls, x, y):
        try:
            loadtilemap = MiPiSettings.tilemap_img
            gamescreen.blit(loadtilemap, (x, y))
            pygame.transform.scale(loadtilemap, (MiPiGUI.g_screen_x, MiPiGUI.g_screen_y))
            if loadtilemap is None:
                print(editor_error)
        except IOError as e:
            pass

    @classmethod
    def LoadEnemy(cls, x, y):
        try:
            # This is just for testing purposes: These test assets are just for TESTING my engine!
            # Remove any test assets before a serious beta or release build!!!
            MiPiSettings.enemy_image = pygame.image.load(
                os.path.join('D:/dev/assets/thirdparty/graphics/sprites', 'enemysprite.gif'))
            loadenemy = MiPiSettings.enemy_image
            gamescreen.blit(loadenemy, (x, y))
            if loadenemy is None:
                print(MiPiSettings.enemy_error)
        except IOError as e:
            pass

    @classmethod
    def EnemySpeed(cls):
        setspeed = input('Do you want a fast enemy or a slow enemy? Type either fast or slow: ')

        if setspeed == 'fast':
            MiPi.FastEnemy()
        elif setspeed == 'slow':
            MiPi.SlowEnemy()
        else:
            MiPi.FastEnemy()

    @classmethod
    def FastEnemy(cls):
        MiPiSettings.enemy_speed = 10

    @classmethod
    def SlowEnemy(cls):
        MiPiSettings.enemy_speed = 2

    @staticmethod
    def EngineInit():

        # This method is called upon starting the MiPi engine
        logging.basicConfig(filename='mipi.log', level=logging.INFO)
        print(current_date, ": ", MiPiSettings.current_version, " has been initialized")
        if platform.system() == MiPiSettings.Windows:
            print('Operating system: Windows detected - Engine running')
        elif platform.system() == MiPiSettings.Mac:
            print('Operating system: MacOS detected - Engine running')
        elif platform.system() == MiPiSettings.Linux:
            print('Operating system: Linux detected - Engine running')
        else:
            print('Operating system: unknown - Engine running (unexpected results may occur!)')
        logging.info(current_date)
        logging.info(MiPiSettings.log_msg)

    def UnderDev(self):
        msg = MiPiSettings.underdevelopment
        print(current_date, msg)

    @classmethod
    def EraseUI(cls):
        if not MiPiSettings.editablePlayerSprite:
            MiPiGUI.playerxlocbar.hide()
            MiPiGUI.playerylocbar.hide()
            MiPiGUI.updateplayer_button.hide()

        if not MiPiSettings.editableNPCSprite:
            MiPiGUI.npcxlocbar.hide()
            MiPiGUI.npcylocbar.hide()
            MiPiGUI.updatenpc_button.hide()

    @classmethod
    def EditSprite(cls):

        if MiPiSettings.editablePlayerSprite:
            enginescreen.blit(MiPiGUI.playerlocationlabel, MiPiGUI.playerborder)
            enginescreen.blit(MiPiGUI.playerxlabel, MiPiGUI.playerxborder)
            enginescreen.blit(MiPiGUI.playerylabel, MiPiGUI.playeryborder)

            playerxlabel = MiPiGUI.smallfont.render(MiPiGUI.textx, True, Render.WHITE, Render.DARKSHADE)
            playerxborder = playerxlabel.get_rect()
            playerxborder.center = (500, 185)
            enginescreen.blit(playerxlabel, playerxborder)

            playerylabel = MiPiGUI.smallfont.render(MiPiGUI.texty, True, Render.WHITE, Render.DARKSHADE)
            playeryborder = playerylabel.get_rect()
            playeryborder.center = (600, 185)
            enginescreen.blit(playerylabel, playeryborder)

            # UI Horizontal sliders
            MiPiGUI.playerxlocbar.show()
            MiPiGUI.playerylocbar.show()
            MiPiGUI.playerxlocbar.enable()
            MiPiGUI.playerylocbar.enable()

            # UI Sprite Update Button enabled
            MiPiGUI.updateplayer_button.show()
            MiPiGUI.updateplayer_button.enable()

            # Get current slider values
            getspritex = MiPiGUI.playerxlocbar.get_current_value()
            getspritey = MiPiGUI.playerylocbar.get_current_value()
            MiPiGUI.textx = str(getspritex)
            MiPiGUI.texty = str(getspritey)

        if MiPiSettings.editableNPCSprite:
            enginescreen.blit(MiPiGUI.npclocationlabel, MiPiGUI.npcborder)
            enginescreen.blit(MiPiGUI.npcxlabel, MiPiGUI.npcxborder)
            enginescreen.blit(MiPiGUI.npcylabel, MiPiGUI.npcyborder)

            # Get current slider values
            getnpcspritex = MiPiGUI.npcxlocbar.get_current_value()
            getnpcspritey = MiPiGUI.npcylocbar.get_current_value()
            MiPiGUI.npctextx = str(getnpcspritex)
            MiPiGUI.npctexty = str(getnpcspritey)

            npcxlabel = MiPiGUI.smallfont.render(MiPiGUI.npctextx, True, Render.WHITE, Render.DARKSHADE)
            npcxborder = npcxlabel.get_rect()
            npcxborder.center = (500, 370)
            enginescreen.blit(npcxlabel, npcxborder)

            npcylabel = MiPiGUI.smallfont.render(MiPiGUI.npctexty, True, Render.WHITE, Render.DARKSHADE)
            npcyborder = npcylabel.get_rect()
            npcyborder.center = (600, 370)
            enginescreen.blit(npcylabel, npcyborder)

            # UI Horizontal sliders
            MiPiGUI.npcxlocbar.show()
            MiPiGUI.npcylocbar.show()
            MiPiGUI.npcxlocbar.enable()
            MiPiGUI.npcylocbar.enable()

            # UI Sprite Update Button enabled
            MiPiGUI.updatenpc_button.show()
            MiPiGUI.updatenpc_button.enable()
