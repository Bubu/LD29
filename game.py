from config import *

import pg_interface as _if
import root
import numpy as np

class game:
    def __init__(self):
        self._if = _if.interface(self)
        self.grid = np.zeros((RES_Y//50,RES_X//50),dtype=(int,3))
        self.grid[:3,:,0] = AIR
        self.grid[3,RES_X//100][0] = SUP
        self.roots = []
        self.roots.append(root.root(self,(3,RES_X//100),DOWN))

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        self.grid = np.roll(self.grid,-1,0)
        for r in self.roots:
            r.pos = (r.pos[0]-1,r.pos[1])
            if r.pos[0] < 0:
                roots.remove(r)

    def grid_update(self):
        self.grid[-1,:,0] = GROUND #TODO: Generate new, random tiles

    def move(self,check_dir):
        self.lowest_ypos = 0
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
        self.checkScroll()

    def triggerSplit(self):
        for r in self.roots:
            dir1 = None
            dir2 = None
            oldpos = r.pos
            olddir = r.dir
            t = r.check_split()
            print(t)
            try:
                dir1,dir2 = t
            except TypeError:
                print("ERROR: ", oldpos,olddir,dir1,dir2)
            if dir1 is not None:
                if dir2 is not None:
                    newpos1,newpos2 = self.getnewpos(oldpos,dir1,dir2)
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
                else:
                    self.updateSingleTile(r,dir1,olddir,oldpos)
        self.roots += self.newroots

    def updateSingleTile(self,root,dir,olddir,oldpos):
        newpos = root.pos
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
            self.grid_update()
            self._if.redrawGrid()
            
    def getnewpos(self,oldpos,dir1,dir2):
        d = {DOWN:(1,0),UP:(-1,0),LEFT:(0,-1),RIGHT:(0,1)}
        newpos1 = oldpos[0] + d[dir1][0],oldpos[1] + d[dir1][1]
        newpos2 = oldpos[0] + d[dir2][0],oldpos[1] + d[dir2][1]
        #print(newpos1,newpos2)
        return newpos1,newpos2
    
myGame = game()
myGame.run()
myGame.close()
