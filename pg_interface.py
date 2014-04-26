import pygame as pg
from pygame.locals import *
from config import *
import sys

class interface:
    def __init__(self,game):
        pg.init()
        self.screen = pg.display.set_mode((RES_X, RES_Y))
        pg.display.set_caption(GAME_NAME)
        #self.clock = pg.time.Clock()

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
        self.screen.fill((196,195,192))
