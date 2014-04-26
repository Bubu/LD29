from config import *

class root:
    def __init__(self, game, pos, dir):
        self.game = game
        self.pos = pos
        self.dir = dir

    def check_down(self):
        if self.dir == UP:
            return self.check_up()
        if self.game.grid[self.pos[0]+1][self.pos[1]][0] in ACCESS:
            self.pos = (self.pos[0]+1,self.pos[1])
            self.dir = DOWN
            return DOWN
        elif self.pos[1] < RES_X//100:
            if self.pos[1] > 0 and self.game.grid[self.pos[0]][self.pos[1]-1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]-1)
                self.dir = LEFT
                return LEFT
            elif self.game.grid[self.pos[0]][self.pos[1]+1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]+1)
                self.dir = RIGHT
                return RIGHT
            else:
                return None
        elif self.pos[1] >= RES_X//100:
            if self.pos[1] < RES_X//50 and self.game.grid[self.pos[0]][self.pos[1]+1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]+1)
                self.dir = RIGHT
                return RIGHT
            elif self.game.grid[self.pos[0]][self.pos[1]-1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]-1)
                self.dir = LEFT
                return LEFT
            else:
                return None

    def check_right(self):
        if self.dir == LEFT:
            return self.check_left()
        if self.pos[1] < RES_X//100:
            if self.game.grid[self.pos[0]][self.pos[1]+1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]+1)
                self.dir = RIGHT
                return RIGHT
            elif self.game.grid[self.pos[0]+1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]+1,self.pos[1])
                self.dir = DOWN
                return DOWN
            elif self.game.grid[self.pos[0]-1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]-1,self.pos[1])
                self.dir = UP
                return UP 
            else:
                return None
        elif self.pos[1] >= RES_X//100:
            if self.pos[1] < RES_X//50 and self.game.grid[self.pos[0]][self.pos[1]+1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]+1)
                self.dir = RIGHT
                return RIGHT
            elif self.game.grid[self.pos[0]+1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]+1,self.pos[1])
                self.dir = DOWN
                return DOWN
            elif self.game.grid[self.pos[0]-1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]-1,self.pos[1])
                self.dir = UP
                return UP 
            else:
                return None

    def check_left(self):
        if self.dir == RIGHT:
            return self.check_right()
        if self.pos[1] < RES_X//100:
            if self.pos[1] > 0 and self.game.grid[self.pos[0]][self.pos[1]-1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]-1)
                self.dir = LEFT
                return LEFT
            elif self.game.grid[self.pos[0]+1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]+1,self.pos[1])
                self.dir = DOWN
                return DOWN
            elif self.game.grid[self.pos[0]-1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]-1,self.pos[1])
                self.dir = UP
                return UP 
            else:
                return None
        elif self.pos[1] >= RES_X//100:
            if self.game.grid[self.pos[0]][self.pos[1]-1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]-1)
                self.dir = LEFT
                return LEFT
            elif self.game.grid[self.pos[0]+1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]+1,self.pos[1])
                self.dir = DOWN
                return DOWN
            elif self.game.grid[self.pos[0]-1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]-1,self.pos[1])
                self.dir = UP
                return UP 
            else:
                return None

    def check_up(self):
        if self.pos[1] < RES_X//100:
            if self.pos[1] > 0 and self.game.grid[self.pos[0]][self.pos[1]-1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]-1)
                self.dir = LEFT
                return LEFT
            elif self.game.grid[self.pos[0]][self.pos[1]+1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]+1)
                self.dir = RIGHT
                return RIGHT
            elif self.game.grid[self.pos[0]-1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]-1,self.pos[1])
                self.dir = UP
                return UP 
            else:
                return None
        elif self.pos[1] >= RES_X//100:
            if self.pos[1] < RES_X//50 and self.game.grid[self.pos[0]][self.pos[1]+1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]+1)
                self.dir = RIGHT
                return RIGHT
            elif self.game.grid[self.pos[0]][self.pos[1]-1][0] in ACCESS:
                self.pos = (self.pos[0],self.pos[1]-1)
                self.dir = LEFT
                return LEFT
            elif self.game.grid[self.pos[0]-1][self.pos[1]][0] in ACCESS:
                self.pos = (self.pos[0]-1,self.pos[1])
                self.dir = UP
                return UP 
            else:
                return None             
        
    def check_split(self):
        pass
        
