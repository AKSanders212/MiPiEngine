# MiPi Engine alpha v1.0 - © Aaron Keith Sanders - All Rights Reserved
import pygame
from pygame import *
import Render
from Render import *

pygame.init()

# Mipi variables
current_version = "MiPi Engine alpha v1.3"
log_msg = (current_version, " has been initialized")
reminders_one = ''' 
Remove lines of code for npcsprite = False @ 161 and playersprite = False @ 192. 
These were bandaid fixes. You added them, so as to remove duplicate sprites, 
but one sprite is actually the npc and the other is the player. 
You want multiple sprites on the screen, so do not let duplicates confuse you! 
'''
size = 0, 0
editor_has_content = False
player_img = None
npc_img = pygame.Surface(size)
enemy_image = None
sprite_path = None
npc_path = None
editablePlayerSprite = False
editableNPCSprite = False
import_player_sprite = None
import_npc_sprite = None
sliderxmoved = False
sliderymoved = False
playerx_to_editor = 0
playery_to_editor = 0
npcx_to_editor = 0
npcy_to_editor = 0
offset_x = 96
offset_y = 260.2941176470588
isEnemy = False
enemy_x = 0
enemy_y = 0
enemy_speed = 0
enemy_error = 'The enemy test sprite could not be loaded!'
platform_error = 'Your OS could not be detected!'
Windows = 'Windows'
Linux = 'Linux'
Mac = 'Darwin'
underdevelopment = 'This feature is still in development'
playersprite = False
npcsprite = False
npc_removeduplicates = 0
player_removeduplicates = 0
tilemap_chosen = False
tilemap_img = None
tile_path = None
import_tilemap = None
tilemap_ready = False
tilemap_available = False
playersprite_available = False


class Settings:

    def __init__(self):
        pass


class Errors:
    font = pygame.font.Font('freesansbold.ttf', 32)

    def __init__(self, msg, text, size, x, y):
        self.msg = ''
        self.x = 0
        self.y = 0
        self.size = (x, y)
        self.text = ''

    @staticmethod
    def NotAvailableBox():
        x = 500
        y = 500
        size = (x, y)
        text = Errors.font.render('Uh oh, youre either missing a resource or youre importing in the wrong order!', True,
                           Render.RED, Render.BLACK)
        # window screen
        error1_screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Error01: [Resource Not Available] ')
        text_rect = text.get_rect()
        text_rect.center = (x // 2, y // 2)
        error1_screen.fill(Render.LIGHTCOLOR)
        error1_screen.blit(text, text_rect)

        pygame.display.update()
