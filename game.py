from config import *

import pg_interface as _if
import root
import numpy as np

class game:
    def __init__(self):
        self._if = _if.interface(self)
        self.grid = np.zeros((RES_Y//50,RES_X//50))
        self.grid[0:3] = AIR
        self.grid[3,RES_X//100] = STUBd
        self.roots = []
        self.roots.append(root.root(self,(3,RES_X//100),DOWN))

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        self.grid = np.delete(self.grid, 0, 0)
        for r in roots:
            r.pos = (r.pos[0]-1,r.pos[1])
            if r.pos[0] < 0:
                roots.remove(r)

    def grid_update(self):
        self.grid = np.vstack([self.grid, np.zeros(RES_X//50)])

    def move(self,check_dir):
        lowest_ypos = 0
        for root in self.roots:
            oldpos = root.pos
            old_dir = root.dir
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
                    self.grid[newpos] = STUBd
                    if olddir == DOWN:
                        self.grid[oldpos] = ROOTv
                    elif olddir == RIGHT:
                        self.grid[oldpos] = LANGLEd
                    elif olddir == LEFT:
                        self.grid[oldpos] = RANGLEd
                elif dir == UP:
                    self.grid[newpos] = STUBu
                    if olddir == UP:
                        self.grid[oldpos] = ROOTv
                    elif olddir == LEFT:
                        self.grid[oldpos] = RANGLEu
                    elif olddir == RIGHT:
                        self.grid[oldpos] = LANGLEu
                elif dir == RIGHT:
                    self.grid[newpos] = STUBr
                    if olddir == UP:
                        self.grid[oldpos] = RANGLEd
                    elif olddir == DOWN:
                        self.grid[oldpos] = RANGLEu
                    elif olddir == RIGHT:
                        self.grid[oldpos] = ROOTh
                elif dir == LEFT:
                    self.grid[newpos] = STUBl
                    if olddir == UP:
                        self.grid[oldpos] = LANGLEd
                    elif olddir == LEFT:
                        self.grid[oldpos] = ROOTh
                    elif olddir == DOWN:
                        self.grid[oldpos] = LANGLEu
                self._if.update([oldpos,newpos])
        if lowest_ypos >= (RES_Y//50-10):
            self.scroll_up()
            self.grid_update()
            self._if.redrawGrid()
            
    def triggerSplit(self):
        pass
        
myGame = game()
myGame.run()
myGame.close()
