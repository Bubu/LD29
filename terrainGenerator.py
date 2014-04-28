from config import *
import numpy as np
from random import random, choice

class terrainGenerator:
    def __init__(self):
        self.counter = 0
        self.path = [RES_X//100]
        self.p_stone = P_STONE
        self.mineral_counter = 3
        #self.p_connected = 2
        self.p_variations = [P_MINERAL,P_WATER,P_URANIUM,P_MINERAL2,P_MINERAL3]

    def getLine(self):
        line = np.zeros((1,RES_X//50),dtype=(int,2))
        for i in range(RES_X//50):
            r = random()
            if r < self.p_stone:
                line[0,i,0] = STONE1
        self.checkPath(line)
        self.refresh_ground(line)
        self.refresh_stones(line)
        self.p_stone = min(0.8,self.p_stone +0.001)
        #DEBUGGING
        #if self.counter == 1:
        #    line[0,RES_X//100,0]= STONE1            
        #    line[0,RES_X//100+1,0]= GROUND            
        #    line[0,RES_X//100+2,0]= STONE1
        #if self.counter == 2:
        #    line[0,RES_X//100,0]= STONE1            
        #    line[0,RES_X//100+1,0]= STONE1            
        #    line[0,RES_X//100+2,0]= STONE1
        self.counter += 1
        if self.counter > 100:
            self.mineral_counter = 4
        if self.counter > 200:
            self.mineral_counter = 5
        return line

    def checkPath(self,line):
        havePath = False
        for x in self.path:
            if line[0,x,0] in ACCESS:
                havePath = True
        if not havePath:
            line[0,choice(self.path),0] = GROUND
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

    def refresh_ground(self,line):       
        for i in range(RES_X//50):
            for j in range(self.mineral_counter):
                if line[0,i,0] == GROUND:
                    r = random()
                    if r < self.p_variations[j]:
                        line[0,i,0] = ACCESS[j+1]

    def refresh_stones(self,line):       
        for i in range(RES_X//50):
            if line[0,i,0] == STONE1:
                line[0,i,0] = choice(STONES)


