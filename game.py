from config import *

import pg_interface as _if
import root
import numpy as np

class game:
    def __init__(self):
        self._if = _if.interface(self)
        self.grid = np.zeros((RES_Y//50,RES_X//50))
        self.grid[0:3] = AIR
        self.grid[3,RES_X//100] = STUB
        #self.grid[4][RES_X//100] = AIR
        self.roots = []
        self.roots.append(root.root(self,(3,RES_X//100),DOWN))
        #self.roots[0].check_down()

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        self.grid = np.delete(self.grid, 0, 0)

    def grid_update(self):
        self.grid = np.vstack([self.grid, np.zeros(RES_X//50)])

    def moveDown(self):
        self.roots[0].check_down()
        self.scroll_up()
        self.grid_update()
        self._if.redrawGrid()

    def moveRight(self):
        pass
    
    def moveLeft(self):
        pass

    def triggerSplit(self):
        pass
        
myGame = game()
myGame.run()
myGame.close()
