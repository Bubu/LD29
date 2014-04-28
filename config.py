import os,sys

GAME_NAME = 'under the surface'
RES_X = 1650
RES_Y = 800

OFFSET_X = 0
OFFSET_Y = 0

ENERGY_MAX = 20

#TerrainGenerator
P_WATER = 0.01
P_URANIUM = 0.01
P_MINERAL = 0.005
#P_MINERAL2
#P_MINERAL3

#Game Constants. Don't change!
appdir = os.path.dirname(sys.argv[0])
PATH = os.path.join(appdir, "res") + os.sep

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

# ==Tile Constants==
GROUND = 0
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


STONE1 = 100
STONE2 = 104
STONE3 = 105
URANIUM = 101
WATER = 102
MINERAL = 103

PLANT = 1000

STONES = [STONE1,STONE2,STONE3]
ACCESS = [GROUND,WATER,URANIUM,MINERAL]
