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
        #self.roots[0].check_down()

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        #self.grid = np.delete(self.grid, 0, 0)
        self.grid = np.roll(self.grid,-1,0)
        for r in self.roots:
            r.pos = (r.pos[0]-1,r.pos[1])
            if r.pos[0] < 0:
                roots.remove(r)

    def grid_update(self):
        #self.grid = np.vstack([self.grid, np.zeros(RES_X//50,dtype=(int,2))])
        self.grid[-1,:,0] = GROUND #TODO: Generate new, random tiles

    def move(self,check_dir):
        lowest_ypos = 0
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
                newpos = root.pos
                if newpos[0] > lowest_ypos:
                    lowest_ypos = newpos[0]
                if dir == DOWN:
                    self.grid[newpos][0] = SUP
                    if olddir == DOWN:
                        self.grid[oldpos][0] = UPDOWN
                    elif olddir == RIGHT:
                        self.grid[oldpos][0] = LANGLEd
                    elif olddir == LEFT:
                        self.grid[oldpos][0] = RANGLEd
                elif dir == UP:
                    self.grid[newpos][0] = SDOWN
                    if olddir == UP:
                        self.grid[oldpos][0] = DOWNUP
                    elif olddir == LEFT:
                        self.grid[oldpos][0] = RANGLEu
                    elif olddir == RIGHT:
                        self.grid[oldpos][0] = LANGLEu
                elif dir == RIGHT:
                    self.grid[newpos][0] = SLEFT
                    if olddir == UP:
                        self.grid[oldpos][0] = RANGLEd
                    elif olddir == DOWN:
                        self.grid[oldpos][0] = RANGLEu
                    elif olddir == RIGHT:
                        self.grid[oldpos][0] = LEFTRIGHT
                elif dir == LEFT:
                    self.grid[newpos][0] = SRIGHT
                    if olddir == UP:
                        self.grid[oldpos][0] = LANGLEd
                    elif olddir == LEFT:
                        self.grid[oldpos][0] = RIGHTLEFT
                    elif olddir == DOWN:
                        self.grid[oldpos][0] = LANGLEu
                self._if.update([oldpos,newpos])
        if lowest_ypos >= (RES_Y//50-5):
            self.scroll_up()
            self.grid_update()
            self._if.redrawGrid()

    def triggerSplit(self):
        for r in self.roots:
            oldpos = root.pos
            olddir = root.dir
            dir1,dir2 = r.check_split()
            if dir1 is not None and dir2 is not None:
                pass
                #self.grid[oldpos][0] = TILE[]
        self._if.update([oldpos,newpos1,newpos2])
        self.roots += self.newroots
        
myGame = game()
myGame.run()
myGame.close()
