from config import *

import pg_interface as _if
import terrainGenerator
import root
import numpy as np

class game:
    def __init__(self):
        self.energy = ENERGY_MAX
        self.depthscore = 15
        self._if = _if.interface(self)
        self.setup()

    def setup(self):
        self.game_over = False
        self.energy = ENERGY_MAX
        self.level = 3       
        self.generator = terrainGenerator.terrainGenerator()
        self.initialTerrain()
        
        self.decals = []
        self.decals.append(decal(PLANT,0,(RES_X//100)*50-18,150,100))
        self.decals.append(decal(CLOUD1,5,15,90,199))
        self.decals.append(decal(CLOUD2,7,870,87,201))
        self.decals.append(decal(CLOUD3,4,400,58,104))
        self.decals.append(decal(CLOUD4,10,1200,50,82))
        self.roots = []
        self.roots.append(root.root(self,(3,RES_X//100),DOWN))
        
        self._if.score()
        
    def initialTerrain(self):
        self.grid = np.zeros((RES_Y//50,RES_X//50),dtype=(int,2))
        self.grid[:3,:,0] = AIR
        for i in range(3,RES_Y//50):
            self.grid[i,:,:] = self.generator.getLine()
            self._if.genground(self.level)
            self.level += 1
        self.grid[3,RES_X//100][0] = SUP

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        self.grid = np.roll(self.grid,-1,0)
        remove = []
        for r in self.roots:
            r.pos = (r.pos[0]-1,r.pos[1])
            if r.pos[0] < 0:
                remove.append(r)
        for rem in remove:
            self.roots.remove(rem)
        remove = []
        for d in self.decals:
            d.scrollUp()
            if d.isDead():
                remove.append(d)
        for rem in remove:
            self.decals.remove(rem)
        self.grid_update()

    def grid_update(self):
        self.grid[-1,:,:] = self.generator.getLine()
        self._if.genground(self.level)
        self.level += 1

    def move(self,check_dir):
        self.lowest_ypos = 0
        stuck_counter = 0
        for root in self.roots:
            oldpos = root.pos
            olddir = root.dir
            if check_dir == DOWN:
                dir = root.check_down()
            elif check_dir == RIGHT:
                dir = root.check_right()
            elif check_dir == LEFT:
                dir = root.check_left()
            if dir is not None:
                self.updateSingleTile(root,dir,olddir,oldpos)
                self.energy -= 1
                self._if.score()
            if oldpos == root.pos:
               stuck_counter += 1
        if stuck_counter == len(self.roots):
            self.init_game_over()
        self.checkScroll()
        

    def triggerSplit(self):
        self.newroots = []
        self.lowest_ypos = 0
        for r in self.roots:
            dir1 = None
            dir2 = None
            oldpos = r.pos
            olddir = r.dir
            dir1,dir2 = r.check_split()
            if dir1 is not None:
                if dir2 is not None:
                    newpos1,newpos2 = self.getnewpos(oldpos,dir1,dir2)
                    self.doAction(self.grid[newpos1][0],r)
                    self.doAction(self.grid[newpos2][0],r)
                    self.lowest_ypos = max(self.lowest_ypos,newpos1[0],newpos2[0])
                    if olddir == UP:
                        if dir1 == RIGHT:
                            if dir2 == LEFT:
                                newtile = DOWNRIGHTLEFT
                                newtile1 = SLEFT
                                newtile2 = SRIGHT
                            elif dir2 == UP:
                                newtile = DOWNRIGHTUP
                                newtile1 = SLEFT
                                newtile2 = SDOWN
                        elif dir1 == UP:
                            if dir2 == LEFT:
                                newtile = DOWNUPLEFT
                                newtile1 = SDOWN
                                newtile2 = SRIGHT
                    elif olddir == DOWN:
                        if dir1 == LEFT:
                            if dir2 == RIGHT:
                                newtile = UPLEFTRIGHT
                                newtile1 = SRIGHT
                                newtile2 = SLEFT
                            elif dir2 == DOWN:
                                newtile = UPLEFTDOWN
                                newtile1 = SRIGHT
                                newtile2 = SUP
                        elif dir1 == DOWN:
                            if dir2 == RIGHT:
                                newtile = UPDOWNRIGHT
                                newtile1 = SUP
                                newtile2 = SLEFT
                    elif olddir == RIGHT:
                        if dir1 == DOWN:
                            if dir2 == UP:
                                newtile = LEFTDOWNUP
                                newtile1 = SUP
                                newtile2 = SDOWN
                            elif dir2 == RIGHT:
                                newtile = LEFTDOWNRIGHT
                                newtile1 = SUP
                                newtile2 = SLEFT
                        elif dir1 == RIGHT:
                            if dir2 == UP:
                                newtile = LEFTRIGHTUP
                                newtile1 = SLEFT
                                newtile2 = SDOWN
                    elif olddir == LEFT:
                        if dir1 == UP:
                            if dir2 == DOWN:
                                newtile = RIGHTUPDOWN
                                newtile1 = SDOWN
                                newtile2 = SUP
                            elif dir2 == LEFT:
                                newtile = RIGHTUPLEFT
                                newtile1 = SDOWN
                                newtile2 = SRIGHT
                        elif dir1 == LEFT:
                            if dir2 == DOWN:
                                newtile = RIGHTLEFTDOWN
                                newtile1 = SRIGHT
                                newtile2 = SUP
                    self.grid[oldpos][0] = newtile
                    self.grid[newpos1][0] = newtile1
                    self.grid[newpos2][0] = newtile2
                    self._if.update([oldpos,newpos1,newpos2])
                    self.energy -= 2
                    self._if.score()             
                else:
                    self.updateSingleTile(r,dir1,olddir,oldpos)
                    self.energy -= 1
                    self._if.score()
        self.roots += self.newroots
        self.checkScroll()

    def updateSingleTile(self,root,dir,olddir,oldpos):
        newpos = root.pos
        if newpos[0] < 0 or newpos[1] < 0:
            raise ValueError("<0: Old: ", olddir," New: ", dir)
        self.doAction(self.grid[newpos][0],root)
        if newpos[0] > self.lowest_ypos:
            self.lowest_ypos = newpos[0]
        if dir == DOWN:
            self.grid[newpos][0] = SUP
            if olddir == DOWN:
                self.grid[oldpos][0] = UPDOWN
            elif olddir == RIGHT:
                self.grid[oldpos][0] = LEFTDOWN
            elif olddir == LEFT:
                self.grid[oldpos][0] = RIGHTDOWN
        elif dir == UP:
            self.grid[newpos][0] = SDOWN
            if olddir == UP:
                self.grid[oldpos][0] = DOWNUP
            elif olddir == LEFT:
                self.grid[oldpos][0] = RIGHTUP
            elif olddir == RIGHT:
                self.grid[oldpos][0] = LEFTUP
        elif dir == RIGHT:
            self.grid[newpos][0] = SLEFT
            if olddir == UP:
                self.grid[oldpos][0] = DOWNRIGHT
            elif olddir == DOWN:
                self.grid[oldpos][0] = UPRIGHT
            elif olddir == RIGHT:
                self.grid[oldpos][0] = LEFTRIGHT
        elif dir == LEFT:
            self.grid[newpos][0] = SRIGHT
            if olddir == UP:
                self.grid[oldpos][0] = DOWNLEFT
            elif olddir == LEFT:
                self.grid[oldpos][0] = RIGHTLEFT
            elif olddir == DOWN:
                self.grid[oldpos][0] = UPLEFT
        self._if.update([oldpos,newpos])

    def checkScroll(self):
        if self.lowest_ypos >= (RES_Y//50-5):
            self.scroll_up()
            self._if.redrawGrid()
            
    def getnewpos(self,oldpos,dir1,dir2):
        d = {DOWN:(1,0),UP:(-1,0),LEFT:(0,-1),RIGHT:(0,1)}
        newpos1 = oldpos[0] + d[dir1][0],oldpos[1] + d[dir1][1]
        newpos2 = oldpos[0] + d[dir2][0],oldpos[1] + d[dir2][1]
        if newpos1[0] < 0 or newpos1[1] < 0:
            raise ValueError("<0: New: ", dir1,dir2, newpos1)
        if newpos2[0] < 0 or newpos2[1] < 0:
            raise ValueError("<0: New: ", dir1,dir2, newpos2)
        return newpos1,newpos2

    def reset(self):
        self.setup()
        self._if.stop_sounds()
        self._if.redrawGrid()

    def check_energy(self):
        if self.energy <= 0:
            self.init_game_over()

    def init_game_over(self):
        if self.game_over == False:
            self._if.play_sound(GAME_OVER)
        self.game_over = True
        if self.level > self.depthscore:
            self.depthscore = self.level
        self._if.refresh_depthscore()
        self._if.game_over()
            
    def doAction(self,type,root):
        if type == WATER:
            self.energy += VAL_WATER
        if type == URANIUM:
            self.energy -= VAL_URANIUM
        if type == MINERAL:
            root.setStoneCrusher()
        if type in STONES:
            root.eatStone()

    def getCrusherCoords(self):
        return [r.pos for r in self.roots if r.stoner_rock > 0]

class decal:
    def __init__(self,type,y,x,sizey,sizex):
        self.type = type
        self.y = y
        self.x = x
        self.sizey = sizey
        self.sizex = sizex
        
    def scrollUp(self):
        self.y -= 50
        
    def isDead(self):
        return self.y + self.sizey <= 0
        
myGame = game()
myGame.run()
myGame.close()
