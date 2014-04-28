import pygame as pg
from pygame.locals import *
from itertools import product
import sys

from config import *


class interface:
    def __init__(self,game):
        self.game = game
        pg.init()
        self.screen = pg.display.set_mode((RES_X, RES_Y+50))
        pg.display.set_caption(GAME_NAME)
        self.updateRects = []
        self.initSprites()

        self.manual()
        self.refresh_depthscore()

        self.basicFont = pg.font.Font(PATH + 'EBGaramond08-Regular.ttf', 17)

    def manual(self):
        maFont = pg.font.Font(PATH + 'EBGaramond08-Regular.ttf', 17)
        mainpanel = pg.Surface((600,50))
        left = maFont.render('Arrow Left - Move Left',True, (255,255,255), (0,0,0))
        down = maFont.render('Arrow Down - Move Down',True, (255,255,255), (0,0,0))
        right = maFont.render('Arrow Left - Move Right',True, (255,255,255), (0,0,0))
        split = maFont.render('Space Bar - Split the Roots',True, (255,255,255), (0,0,0))
        restart = maFont.render('(r)estart Game',True, (255,255,255), (0,0,0))
        q_uit = maFont.render('(q)uit Game',True, (255,255,255), (0,0,0))
        mainpanel.blit(left, (0, 10))
        mainpanel.blit(down, (200, 10))
        mainpanel.blit(right, (400, 10))
        mainpanel.blit(split, (0, 30))
        mainpanel.blit(restart, (200, 30))
        mainpanel.blit(q_uit, (400, 30))
        self.updateRects.append(self.screen.blit(mainpanel, (0, RES_Y)))


    def score(self):
        scFont = pg.font.Font(PATH + 'EBGaramond08-Regular.ttf', 17)
        mainlabel = pg.Surface((150,50))
        energy = scFont.render('Energy: '+str(self.game.energy),True, (255,255,255), (0,0,0))
        level = scFont.render('Depthlevel: '+str(self.game.level),True, (255,255,255), (0,0,0))
        mainlabel.blit(energy, (0, 10))
        mainlabel.blit(level, (0, 30))
        self.updateRects.append(self.screen.blit(mainlabel,(RES_X-150, RES_Y)))

    def refresh_depthscore(self):
        dsFont = pg.font.Font(PATH + 'EBGaramond08-Regular.ttf', 17)
        mainlabel = pg.Surface((300,50))
        no_highscore = dsFont.render('The Highscore is a lie.',True, (255,255,255), (0,0,0))
        depthscore = dsFont.render('Actually your Depthscore is '+str(self.game.depthscore)+'.',True, (255,255,255), (0,0,0))
        mainlabel.blit(no_highscore, (0, 10))
        mainlabel.blit(depthscore, (0, 30))
        self.updateRects.append(self.screen.blit(mainlabel, (RES_X-450, RES_Y)))
        
    def initSprites(self):
        self.sprites = {AIR:pg.Surface((50,50)),
                        GROUND:pg.Surface((50,50)),
                        STONE1:pg.image.load(PATH+'stone1.png').convert_alpha(),
                        STONE2:pg.image.load(PATH+'stone2.png').convert_alpha(),
                        STONE3:pg.image.load(PATH+'stone3.png').convert_alpha(),
                        WATER:pg.image.load(PATH+'water.png').convert_alpha(),
                        URANIUM:pg.Surface((50,50)),
                        MINERAL:pg.image.load(PATH+'mineral1.png').convert_alpha(),
                        SUP:pg.image.load(PATH+'up.png').convert_alpha(),
                        SDOWN:pg.image.load(PATH+'down.png').convert_alpha(),
                        SLEFT:pg.image.load(PATH+'left.png').convert_alpha(),
                        SRIGHT:pg.image.load(PATH+'right.png').convert_alpha(),
                        UPDOWN:pg.image.load(PATH+'updown.png').convert_alpha(),
                        DOWNUP:pg.image.load(PATH+'downup.png').convert_alpha(),
                        LEFTRIGHT:pg.image.load(PATH+'leftright.png').convert_alpha(),
                        RIGHTLEFT:pg.image.load(PATH+'rightleft.png').convert_alpha(),
                        UPLEFT:pg.image.load(PATH+'upleft.png').convert_alpha(),
                        UPRIGHT:pg.image.load(PATH+'upright.png').convert_alpha(),
                        DOWNLEFT:pg.image.load(PATH+'downleft.png').convert_alpha(),
                        DOWNRIGHT:pg.image.load(PATH+'downright.png').convert_alpha(),
                        LEFTUP:pg.image.load(PATH+'leftup.png').convert_alpha(),
                        LEFTDOWN:pg.image.load(PATH+'leftdown.png').convert_alpha(),
                        RIGHTUP:pg.image.load(PATH+'rightup.png').convert_alpha(),
                        RIGHTDOWN:pg.image.load(PATH+'rightdown.png').convert_alpha(),                        
                        DOWNRIGHTLEFT:pg.image.load(PATH+'downrightleft.png').convert_alpha(),
                        DOWNUPLEFT:pg.image.load(PATH+'downupleft.png').convert_alpha(),
                        DOWNRIGHTUP:pg.image.load(PATH+'downrightup.png').convert_alpha(),
                        UPLEFTRIGHT:pg.image.load(PATH+'upleftright.png').convert_alpha(),
                        UPLEFTDOWN:pg.image.load(PATH+'upleftdown.png').convert_alpha(),
                        UPDOWNRIGHT:pg.image.load(PATH+'updownright.png').convert_alpha(),
                        LEFTDOWNUP:pg.image.load(PATH+'leftdownup.png').convert_alpha(),
                        LEFTDOWNRIGHT:pg.image.load(PATH+'leftdownright.png').convert_alpha(),
                        LEFTRIGHTUP:pg.image.load(PATH+'leftrightup.png').convert_alpha(),
                        RIGHTUPDOWN:pg.image.load(PATH+'rightupdown.png').convert_alpha(),
                        RIGHTUPLEFT:pg.image.load(PATH+'rightupleft.png').convert_alpha(),
                        RIGHTLEFTDOWN:pg.image.load(PATH+'rightleftdown.png').convert_alpha()
                        }
        self.sprites[AIR].fill((50,50,200))
        self.sprites[GROUND].fill((139,69,19))
        #self.sprites[WATER].fill((0,0,255))
        self.sprites[URANIUM].fill((255,0,0))
        #self.sprites[MINERAL].fill((255,255,255))
        self.grounds = {}
        self.grounds[0] = (self.sprites[GROUND])
        self.grounds[1] = (self.sprites[GROUND])
        self.grounds[2] = (self.sprites[GROUND])

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
            if evt.type == KEYUP and evt.key == K_q:
                return
            else:
                if not self.game.game_over:
                    if evt.type == KEYUP and evt.key == K_DOWN:
                        self.game.move(DOWN)
                    elif evt.type == KEYUP and evt.key == K_RIGHT:
                        self.game.move(RIGHT)
                    elif evt.type == KEYUP and evt.key == K_LEFT:
                        self.game.move(LEFT)
                    elif evt.type == KEYUP and evt.key == K_SPACE:
                        self.game.triggerSplit()
                    elif evt.type == KEYUP and evt.key == K_d:
                        import pdb
                        import numpy as np
                        np.set_printoptions(linewidth=200)
                        pdb.set_trace()

                if evt.type == KEYUP and evt.key == K_r:
                    self.game.reset()
                self.game.check_energy()
                pg.display.update(self.updateRects)
                self.updateRects = []
                

    def update(self,coord_list):
        for coord in coord_list:
            self.screen.blit(self.grounds[self.game.level-RES_Y//50+coord[0]],self.getScreenPos(coord))
            if self.game.grid[coord][0] != GROUND:
                self.screen.blit(self.sprites[self.game.grid[coord][0]],self.getScreenPos(coord))
            self.updateRects.append(self.getRect(coord))
            
    def getRect(self,coord):
        return pg.Rect(self.getScreenPos(coord),(50,50))

    def redrawGrid(self):
        self.drawGrid()
        self.updateRects.append(self.screen.get_rect())

    def setup(self):
        self.drawGrid()

    def drawGrid(self):
        for coord in product(range(RES_Y//50),range(RES_X//50)):
            self.screen.blit(self.grounds[self.game.level-RES_Y//50+coord[0]],self.getScreenPos(coord))
            if self.game.grid[coord][0] != GROUND:
                self.screen.blit(self.sprites[self.game.grid[coord][0]],self.getScreenPos(coord))
            #pg.draw.circle(self.screen,(0,0,0),(self.getScreenPos(coord)[0]+25,self.getScreenPos(coord)[1]+25),10,1)

    def getScreenPos(self,coord):
        y = coord[0] * 50 + OFFSET_Y
        x = coord[1] * 50 + OFFSET_X
        return x,y

    def genground(self,level):
        self.grounds[level] = self.sprites[GROUND].copy()
        self.grounds[level].fill((max(40,180-level),max(10,90-level//2),max(4,20-level//90)))

    def game_over(self):
        game_over = pg.Surface((300,100))
        goFont = pg.font.Font(PATH + 'EBGaramond08-Regular.ttf', 48)
        reFont = pg.font.Font(PATH + 'EBGaramond08-Regular.ttf', 21)
        text = goFont.render('Game Over',True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.x = game_over.get_rect().centerx-text.get_width()//2
        textRect.y = game_over.get_rect().centery-2*text.get_height()//3
        re_text = reFont.render('(r)estart or (q)uit',True, (255,255,255), (0,0,0))
        re_textRect = re_text.get_rect()
        re_textRect.x = game_over.get_rect().centerx-re_text.get_width()//2
        re_textRect.y = game_over.get_rect().centery+re_text.get_height()
        game_over.blit(text, textRect)
        game_over.blit(re_text, re_textRect)
        self.updateRects.append(self.screen.blit(game_over,(RES_X//2-game_over.get_width()//2, RES_Y//2-game_over.get_height()//2)))
