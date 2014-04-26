import pygame as pg
from pygame.locals import *
from itertools import product
import sys

from config import *


class interface:
    def __init__(self,game):
        self.game = game
        pg.init()
        self.screen = pg.display.set_mode((RES_X, RES_Y))
        pg.display.set_caption(GAME_NAME)
        self.initSprites()
        
    def initSprites(self):
        self.sprites = {AIR:pg.Surface((50,50)),
                        GROUND:pg.Surface((50,50))
                        }
        self.sprites[AIR].fill((50,50,200))
        self.sprites[GROUND].fill((139,69,19))

    def close(self):
        pg.quit()

    def run(self):
        self.setup()
        pg.display.update()
        while True:
            evt = pg.event.wait()
            if evt.type == QUIT:
                return
            if evt.type == KEYUP and evt.key == K_F4 and bool(evt.mod & KMOD_ALT):
                return
            else:
                pass

    def setup(self):
        #self.screen.fill((196,195,192))
        self.drawGrid()
        self.screen.blit(self.sprites[AIR],(50,50))
        self.screen.blit(self.sprites[GROUND],(50,100))

    def drawGrid(self):
        for coord in product(range(RES_X//50),range(RES_Y//50)):
            self.screen.blit(self.sprites[self.game.grid[coord]],self.getScreenPos(coord))

    def getScreenPos(self,coord):
        x = ccord[0] * 50 + OFFSET_X
        y = ccord[1] * 50 + OFFSET_Y
        return x,y
