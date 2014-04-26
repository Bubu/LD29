import config as cfg
import pg_interface as _if
import numpy as np

class game:
    def __init__(self):
        self._if = _if.interface(self)
        #values in self.grid indicate, which tile is stored at the moment
        self.grid = np.zeros((3,3))
        #self.grid = np.zeros((cfg.RES_Y/50,cfg.RES_X/50))
        print(self.grid)
        self.scroll_up()
        print(self.grid)
        self.self_grid_update()
        print(self.grid)

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

    def scroll_up(self):
        self.grid = np.delete(self.grid, 0, 0)

    def self_grid_update(self):
        pass
        #self.grid = np.append(self.grid,np.zeros((1,3)))

myGame = game()
myGame.run()
myGame.close()
