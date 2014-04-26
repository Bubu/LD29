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
        self.game.newroots = []
        old_pos = self.pos
        if self.dir == DOWN:
            if old_pos[1] > 0 and self.game.grid[old_pos[0],old_pos[1]-1][0] in ACCESS:
                self.pos = (old_pos[0],old_pos[1]-1)
                self.dir = LEFT
                if old_pos[1] < RES_X//50 and self.game.grid[old_pos[0],old_pos[1]+1][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0],old_pos[1]+1),RIGHT))
                    return LEFT,RIGHT
                elif self.game.grid[old_pos[0]+1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]+1,old_pos[1]),DOWN))
                    return LEFT,DOWN
            elif old_pos[1] < RES_X//50 and self.game.grid[old_pos[0],old_pos[1]+1][0] in ACCESS:
                self.pos = (old_pos[0],old_pos[1]+1)
                self.dir = RIGHT
                if self.game.grid[old_pos[0]+1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]+1,old_pos[1]),DOWN))
                    return DOWN,RIGHT
            else:
                return self.check_down(),None

        elif self.dir == LEFT:
            if old_pos[1] > 0 and self.game.grid[old_pos[0],old_pos[1]-1][0] in ACCESS:
                self.pos = (old_pos[0],old_pos[1]-1)
                self.dir = LEFT
                if self.game.grid[old_pos[0]+1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]+1,old_pos[1]),DOWN))
                    return LEFT,DOWN
                elif self.game.grid[old_pos[0]-1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]-1,old_pos[1]),UP))
                    return UP,LEFT
            elif self.game.grid[old_pos[0]+1,old_pos[1]][0] in ACCESS:
                self.pos = (old_pos[0]+1,old_pos[1])
                self.dir = DOWN
                if self.game.grid[old_pos[0]-1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]-1,old_pos[1]),UP))
                    return UP,DOWN
            else:
                return self.check_up(), None

        elif self.dir == RIGHT:
            if old_pos[1] < RES_X//50 and self.game.grid[old_pos[0],old_pos[1]+1][0] in ACCESS:
                self.pos = (old_pos[0],old_pos[1]+1)
                self.dir = RIGHT
                if self.game.grid[old_pos[0]+1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]+1,old_pos[1]),DOWN))
                    return DOWN,RIGHT
                elif self.game.grid[old_pos[0]-1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]-1,old_pos[1]),UP))
                    return RIGHT,UP
            elif self.game.grid[old_pos[0]+1,old_pos[1]][0] in ACCESS:
                self.pos = (old_pos[0]+1,old_pos[1])
                self.dir = DOWN
                if self.game.grid[old_pos[0]-1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]-1,old_pos[1]),UP))
                    return DOWN,UP
            else:
                return self.check_up(),None

        elif self.dir == UP:
            if old_pos[1] > 0 and self.game.grid[old_pos[0],old_pos[1]-1][0] in ACCESS:
                self.pos = (old_pos[0],old_pos[1]-1)
                self.dir = LEFT
                if old_pos[1] < RES_X//50 and self.game.grid[old_pos[0],old_pos[1]+1][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0],old_pos[1]+1),RIGHT))
                    return LEFT,RIGHT
                elif self.game.grid[old_pos[0]-1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]-1,old_pos[1]),UP))
                    return UP,LEFT
            elif old_pos[1] < RES_X//50 and self.game.grid[old_pos[0],old_pos[1]+1][0] in ACCESS:
                self.pos = (old_pos[0],old_pos[1]+1)
                self.dir = RIGHT
                if self.game.grid[old_pos[0]-1,old_pos[1]][0] in ACCESS:
                    self.game.newroots.append(root(self.game,(old_pos[0]-1,old_pos[1]),UP))
                    return UP,RIGHT
            else:
                return self.check_up(),None
                                  
    def move_in_dir(self):
        if self.dir == DOWN:
            self.check_down()
        elif self.dir == LEFT:
            self.check_left()
        elif self.dir == RIGHT:
            self.check_right()
        elif self.dir == UP:
            self.check_up()
