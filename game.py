import config as cfg
import pg_interface as _if
import numpy as np

class game:
    def __init__(self):
        self._if = _if.interface(self)
        self.grid = np.zeros((cfg.RES_Y/50,cfg.RES_X/50))
        self.grid[0:3] = cfg.AIR

        #print the self.grid with its methods
        #print(self.grid)
        #self.scroll_up()
        #print('cut first line' ,+self.grid)
        #self.self_grid_update()
        #print('add last line with zeros',+self.grid)

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        self.grid = np.delete(self.grid, 0, 0)

    def grid_update(self):
        self.grid = np.vstack([self.grid, np.zeros(cfg.RES_X/50)])

    def moveDown(self):
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
