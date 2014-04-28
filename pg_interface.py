import pygame as pg
from pygame.locals import *
from itertools import product
import sys

from config import *


class interface:
    def __init__(self,game):
        self.game = game
        pg.mixer.pre_init(44100,-16,2, 1024)
        pg.init()
        self.screen = pg.display.set_mode((RES_X, RES_Y+50))
        pg.display.set_caption(GAME_NAME)
        self.updateRects = []
        self.initSprites()
        self.initSounds()
        self.mute = False
        self.manual()
        self.icon_description()
        self.separator()
        self.refresh_depthscore()

    def manual(self):
        maFont = pg.font.Font(PATH + FONT2, 16)
        mainpanel = pg.Surface((300,50))
        arrows = maFont.render('arrows - move',True, (255,255,255), (0,0,0))
        split = maFont.render('space - rootsplit',True, (255,255,255), (0,0,0))
        restart = maFont.render('(r)estart',True, (255,255,255), (0,0,0))
        q_uit = maFont.render('(q)uit',True, (255,255,255), (0,0,0))
        mute = maFont.render('(m)ute',True, (255,255,255), (0,0,0)) 
        mainpanel.blit(arrows, (0, 5))
        mainpanel.blit(split, (0, 25))
        mainpanel.blit(restart, (150, 5))
        mainpanel.blit(q_uit, (150, 25))
        mainpanel.blit(mute, (250, 5))
        self.updateRects.append(self.screen.blit(mainpanel, (10, RES_Y)))

    def separator(self):
        separator = pg.Surface((3, 40))
        separator.fill((255,255,255))
        self.updateRects.append(self.screen.blit(separator, (320, RES_Y+5)))
        self.updateRects.append(self.screen.blit(separator, (RES_X-363, RES_Y+5)))

    def icon_description(self):
        maFont = pg.font.Font(PATH + FONT2, 16)
        mainpanel = pg.Surface((600,50))
        water = maFont.render('+'+str(VAL_WATER)+(' energy'),True, (255,255,255), (0,0,0))
        uranium = maFont.render('-'+str(VAL_URANIUM)+' energy',True, (255,255,255), (0,0,0))
        mineral1 = maFont.render('root gets +'+str(VAL_MINERAL)+' stone crusher',True, (255,255,255), (0,0,0))
        mineral2 = maFont.render('+'+str(VAL_MINERAL2)+' energy',True, (255,255,255), (0,0,0))
        mineral3 = maFont.render('all roots get +'+str(VAL_MINERAL3)+' stone crusher',True, (255,255,255), (0,0,0))
        mainpanel.blit(self.sprites[WATER_ICON], (0, 5))
        mainpanel.blit(water, (35, 5))
        mainpanel.blit(self.sprites[MINERAL2_ICON], (0, 25))
        mainpanel.blit(mineral2, (35, 25))
        mainpanel.blit(self.sprites[URANIUM_ICON], (165, 5))
        mainpanel.blit(uranium, (200, 5))
        mainpanel.blit(self.sprites[MINERAL1_ICON], (335, 5))
        mainpanel.blit(mineral1, (370, 5))
        mainpanel.blit(self.sprites[MINERAL3_ICON], (335, 25))
        mainpanel.blit(mineral3, (370, 25))
        
        
        self.updateRects.append(self.screen.blit(mainpanel, (RES_X//2-mainpanel.get_width()//2, RES_Y)))

    def score(self):
        scFont = pg.font.Font(PATH + FONT2, 16)
        mainlabel = pg.Surface((120,50))
        energy = scFont.render('energy: '+str(self.game.energy),True, (255,255,255), (0,0,0))
        level = scFont.render('depthlevel: '+str(self.game.level),True, (255,255,255), (0,0,0))
        mainlabel.blit(energy, (0, 5))
        mainlabel.blit(level, (0, 25))
        self.updateRects.append(self.screen.blit(mainlabel,(RES_X-130, RES_Y)))

    def refresh_depthscore(self):
        dsFont = pg.font.Font(PATH + FONT2, 16)
        mainlabel = pg.Surface((220,50))
        no_highscore = dsFont.render('The highscore is a lie.',True, (255,255,255), (0,0,0))
        depthscore = dsFont.render('Your depthscore is '+str(self.game.depthscore)+'.',True, (255,255,255), (0,0,0))
        mainlabel.blit(no_highscore, (0, 5))
        mainlabel.blit(depthscore, (0, 25))
        self.updateRects.append(self.screen.blit(mainlabel, (RES_X-350, RES_Y)))

    def initSounds(self):
        self.sounds = {GAME_OVER:pg.mixer.Sound(PATH+'game_over2.ogg'),
                       S_MINERAL1:pg.mixer.Sound(PATH+'mineral1.wav'),
                       S_MINERAL2:pg.mixer.Sound(PATH+'mineral2.wav'),
                       S_MINERAL3:pg.mixer.Sound(PATH+'mineral3.wav'),
                       S_WATER:pg.mixer.Sound(PATH+'water.wav'),
                       S_STONE_CRUSH:pg.mixer.Sound(PATH+'stone_crush.wav'),
                       S_URANIUM:pg.mixer.Sound(PATH+'uranium.wav')}
        pg.mixer.music.load(PATH + MUSICFILE)
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.set_endevent(MUSIC_END)
        
    def initSprites(self):
        self.sprites = {AIR:pg.Surface((50,50)),
                        GROUND:pg.Surface((50,50)),
                        RED:pg.Surface((50,50)),
                        STONE1:pg.image.load(PATH+'stone4.png').convert_alpha(),
                        STONE2:pg.image.load(PATH+'stone5.png').convert_alpha(),
                        STONE3:pg.image.load(PATH+'stone6.png').convert_alpha(),
                        WATER:pg.image.load(PATH+'water.png').convert_alpha(),
                        URANIUM:pg.image.load(PATH+'uranium.png').convert_alpha(),
                        MINERAL:pg.image.load(PATH+'mineral1.png').convert_alpha(),
                        MINERAL2:pg.image.load(PATH+'mineral2.png').convert_alpha(),
                        MINERAL3:pg.image.load(PATH+'mineral3.png').convert_alpha(),
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
                        RIGHTLEFTDOWN:pg.image.load(PATH+'rightleftdown.png').convert_alpha(),
                        CLOUD1:pg.image.load(PATH+'cloud1.png').convert_alpha(),
                        CLOUD2:pg.image.load(PATH+'cloud2.png').convert_alpha(),
                        CLOUD3:pg.image.load(PATH+'cloud3.png').convert_alpha(),
                        CLOUD4:pg.image.load(PATH+'cloud4.png').convert_alpha(),
                        PLANT:pg.image.load(PATH+'plant.png').convert_alpha(),
                        GROUNDTEX:pg.image.load(PATH+'groundtex.png').convert_alpha(),
                        WATER_ICON:pg.image.load(PATH+'water_icon.png').convert_alpha(),
                        URANIUM_ICON:pg.image.load(PATH+'uranium_icon.png').convert_alpha(),
                        MINERAL1_ICON:pg.image.load(PATH+'mineral1_icon.png').convert_alpha(),
                        MINERAL2_ICON:pg.image.load(PATH+'mineral2_icon.png').convert_alpha(),
                        MINERAL3_ICON:pg.image.load(PATH+'mineral3_icon.png').convert_alpha()}
        self.sprites[AIR].fill((50,50,200))
        self.sprites[GROUND].fill((139,69,19))
        self.sprites[RED].fill((255,30,25))
        self.sprites[SUPRED] = self.sprites[SUP].copy()
        self.sprites[SDOWNRED] = self.sprites[SDOWN].copy()
        self.sprites[SLEFTRED] = self.sprites[SLEFT].copy()
        self.sprites[SRIGHTRED] = self.sprites[SRIGHT].copy()
        self.sprites[SUPRED].blit(self.sprites[RED],(0,0),special_flags=BLEND_RGB_MULT)
        self.sprites[SDOWNRED].blit(self.sprites[RED],(0,0),special_flags=BLEND_RGB_MULT)
        self.sprites[SLEFTRED].blit(self.sprites[RED],(0,0),special_flags=BLEND_RGB_MULT)
        self.sprites[SRIGHTRED].blit(self.sprites[RED],(0,0),special_flags=BLEND_RGB_MULT)     
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
            if evt.type == MUSIC_END:
                self.handlemusic()
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
                if evt.type == KEYUP and evt.key == K_m:
                    if self.mute == False:
                        self.mute = True
                        self.stop_sounds()
                    elif self.mute == True:
                        self.mute = False
                elif evt.type == KEYUP and evt.key == K_r:
                    self.game.reset()
                self.game.check_energy()
                pg.display.update(self.updateRects)
                self.updateRects = []
                

    def update(self,coord_list):
        crusherCoords = self.game.getCrusherCoords()
        for coord in coord_list:
            self.screen.blit(self.grounds[self.game.level-RES_Y//50+coord[0]],self.getScreenPos(coord))
            if self.game.grid[coord][0] != GROUND and coord not in crusherCoords:
                self.screen.blit(self.sprites[self.game.grid[coord][0]],self.getScreenPos(coord))
            if coord in crusherCoords:
                self.screen.blit(self.sprites[-self.game.grid[coord][0]],self.getScreenPos(coord))
            self.updateRects.append(self.getRect(coord))
            
    def getRect(self,coord):
        return pg.Rect(self.getScreenPos(coord),(50,50))

    def redrawGrid(self):
        self.drawGrid()
        self.updateRects.append(self.screen.get_rect())

    def setup(self):
        self.drawGrid()

    def drawGrid(self):
        crusherCoords = self.game.getCrusherCoords()
        for coord in product(range(RES_Y//50),range(RES_X//50)):
            self.screen.blit(self.grounds[self.game.level-RES_Y//50+coord[0]],self.getScreenPos(coord))
            if self.game.grid[coord][0] != GROUND and coord not in crusherCoords:
                self.screen.blit(self.sprites[self.game.grid[coord][0]],self.getScreenPos(coord))
            if coord in crusherCoords:
                self.screen.blit(self.sprites[-self.game.grid[coord][0]],self.getScreenPos(coord))
        for d in self.game.decals:
            self.screen.blit(self.sprites[d.type],(d.x,d.y))
                                 
    def getScreenPos(self,coord):
        y = coord[0] * 50 + OFFSET_Y
        x = coord[1] * 50 + OFFSET_X
        return x,y

    def genground(self,level):
        self.grounds[level] = self.sprites[GROUND].copy()
        self.grounds[level].fill((max(40,180-level),max(10,90-level//2),max(4,20-level//90)))
        self.grounds[level].blit(self.sprites[GROUNDTEX],(0,0),special_flags=0)

    def game_over(self):
        game_over = pg.Surface((300,100))
        goFont = pg.font.Font(PATH + FONT2, 48)
        reFont = pg.font.Font(PATH + FONT2, 21)
        text = goFont.render('Game Over',True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.x = game_over.get_rect().centerx-text.get_width()//2
        textRect.y = game_over.get_rect().centery-2*text.get_height()//3
        re_text = reFont.render('(r)estart or (q)uit',True, (255,255,255), (0,0,0))
        re_textRect = re_text.get_rect()
        re_textRect.x = game_over.get_rect().centerx-re_text.get_width()//2
        re_textRect.y = game_over.get_rect().centery+re_text.get_height()//2
        game_over.blit(text, textRect)
        game_over.blit(re_text, re_textRect)
        self.updateRects.append(self.screen.blit(game_over,(RES_X//2-game_over.get_width()//2, RES_Y//2-game_over.get_height()//2)))

    def play_sound(self,sound):
        if not self.mute:
            self.sounds[sound].play()
            
    def handlemusic(self):
        pg.mixer.music.play()
    
    def stop_sounds(self):
        for s in self.sounds.values():
            s.stop()
    def stopMusic(self):
        pg.mixer.music.stop()
