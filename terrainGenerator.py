from config import *
import numpy as np
from random import random, choice

class terrainGenerator:
    def __init__(self):
        self.path = [RES_X//100]
        self.p_stone = 0.6
        self.p_connected = 2
        self.p_bonus = 0.05
        self.p_malus = 0.04

    def getLine(self):
        line = np.zeros((1,RES_X//50),dtype=(int,3))
        for i in range(RES_X//50):
            r = random()
            if r < self.p_stone:
                line[0,i,0] = STONE1
        self.checkPath(line)
        return line

    def checkPath(self,line):
        havePath = False
        for x in self.path:
            if line[0,x,0] in ACCESS:
                havePath = True
        if not havePath:
            line[0,choice(self.path),0] = GROUND #ACCESS
        newpath = []
        for x in self.path:
            if line[0,x,0] in ACCESS:
                newpath.append(x)
                i = x+1
                while i < RES_X//50 and line[0,i,0] in ACCESS:
                    newpath.append(i)
                    i += 1
                i = x-1
                while i > 0 and line[0,i,0] in ACCESS:
                    newpath.append(i)
                    i -= 1
        self.path = list(set(newpath))
