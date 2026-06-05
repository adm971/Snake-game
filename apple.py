import pygame, random

class Apple : 
    def __init__(self) :
        self.pos_x = random.randrange(0 + 40, 800 - 40)
        self.pos_y = random.randrange(0 + 40, 600 - 40)
        self.size = 20
    