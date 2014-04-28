import os,sys
import pygame as pg
from pygame.locals import *

appdir = os.path.dirname(sys.argv[0])
PATH = os.path.join(appdir, "res") + os.sep

p = os.path.join(appdir, '..')
p = os.path.join(p, 'settings.txt')
f = open(p)

GAME_NAME = 'Game of Roots'
RES_X = 1300
RES_Y = 800

OFFSET_X = 0
OFFSET_Y = 0

ENERGY_MAX = 200

#TerrainGenerator
P_STONE = 0.001
P_WATER = 0.01
VAL_WATER = 10
P_URANIUM = 0.01
VAL_URANIUM = 50
P_MINERAL = 0.005
VAL_MINERAL = 3
P_MINERAL2 = 0.002
VAL_MINERAL2 = 100
P_MINERAL3 = 0.002
VAL_MINERAL3 = 10

for line in f:
    exec(line)
f.close()

#Game Constants. Don't change!

FONT = 'DISTRO.ttf'
FONT2 = 'DISTROB.ttf'
MUSICFILE = 'roots.ogg'
MUSIC_END = pg.USEREVENT + 1
SOUND = ['','','','','','']

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

# ==Tile Constants==
GROUND = 0
GROUNDTEX = -1
SUPRED = -10
SDOWNRED = -11
SLEFTRED = -12
SRIGHTRED = -13
RED = -6
AIR = 1
#Stubs
SUP = 10
SDOWN = 11
SLEFT = 12
SRIGHT = 13
#Straight
UPDOWN = 14
DOWNUP = 15
LEFTRIGHT = 16
RIGHTLEFT = 17
#Corners
UPLEFT = 18
UPRIGHT = 19
DOWNLEFT = 20
DOWNRIGHT = 21
LEFTUP = 22
LEFTDOWN = 23
RIGHTUP = 24
RIGHTDOWN = 25
#Junctions
DOWNRIGHTLEFT = 26
DOWNUPLEFT = 27
DOWNRIGHTUP = 28
UPLEFTRIGHT = 29
UPLEFTDOWN = 30
UPDOWNRIGHT = 31
LEFTDOWNUP = 32
LEFTDOWNRIGHT = 33
LEFTRIGHTUP = 34
RIGHTUPDOWN = 35
RIGHTUPLEFT = 36
RIGHTLEFTDOWN = 37
WATER_ICON = 38
URANIUM_ICON = 39
MINERAL1_ICON = 40
MINERAL2_ICON = 41
MINERAL3_ICON = 42


STONE1 = 100
STONE2 = 104
STONE3 = 105
URANIUM = 101
WATER = 102
MINERAL = 103
MINERAL2 = 106
MINERAL3 = 107

PLANT = 1000
CLOUD1 = 1001
CLOUD2 = 1002
CLOUD3 = 1003
CLOUD4 = 1004

#Sounds
GAME_OVER = 1
S_MINERAL1 = 2
S_MINERAL2 = 3
S_MINERAL3 = 4
S_WATER = 5
S_URANIUM = 6
S_STONE_CRUSH = 7

STONES = [STONE1,STONE2,STONE3]
ACCESS = [GROUND,WATER,URANIUM,MINERAL,MINERAL2,MINERAL3]
