import pygame
from pygame.math import Vector2 as vec
from support import *
from settings import *
from npc import NPC

class Player(NPC):
    def __init__(self, groups, pos, path, z='background'):
        super().__init__(groups, pos, path)

        self.import_images(path)
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.25, -self.rect.height*0.25)

        self.direction = vec() 
        self.speed = 250

    def input(self):
        if CONTROLLERS['PS4 Controller']['LS Right']: 
            self.direction.x = CONTROLLERS['PS4 Controller']['LS Right']
        elif CONTROLLERS['PS4 Controller']['LS Left']:
            self.direction.x = -CONTROLLERS['PS4 Controller']['LS Left']
        else:
            self.direction.x = 0

        if CONTROLLERS['PS4 Controller']['LS Down']: 
            self.direction.y = CONTROLLERS['PS4 Controller']['LS Down']
        elif CONTROLLERS['PS4 Controller']['LS Up']:
            self.direction.y = -CONTROLLERS['PS4 Controller']['LS Up']
        else:
            self.direction.y = 0

    def update(self, dt):
        self.animate('idle', 6 * dt)
        self.input()
        self.movement(dt)
        