import pygame as pg
import math

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
            
    def draw(self,win):
        pg.draw.circle(win, self.COLOR,(self.x,self.y),self.size)
        pg.draw.circle(win, self.SECOND_COLOR,(self.x,self.y),self.size * 0.8)
        pg.draw.circle(win, self.COLOR,(self.x,self.y),self.size * 0.6)
        pg.draw.circle(win, self.SECOND_COLOR,(self.x,self.y),self.size * 0.4)
        
    def collide(self,x,y):
        dis = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        return dis <= self.size