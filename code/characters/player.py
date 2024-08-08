import pygame
from pygame.math import Vector2 as vec2
from settings import *
from support import *
from characters.npc import NPC

class Player(NPC):
    def __init__(self, groups, pos, path, z='background'):
        super().__init__(groups, pos, path)

        self.import_images(path)
        self.rect = self.image.get_frect(center=pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.25, -self.rect.height*0.25)

        self.direction = vec2() 
        self.speed = 180

    def input(self, controller):
        if ACTIONS['Right'] or ACTIONS['Left'] or ACTIONS['Down'] or ACTIONS['Up']:
            if ACTIONS['Right']: 
                self.direction.x = 1
            elif ACTIONS['Left']:
                self.direction.x = -1
            else:
                self.direction.x = 0

            if ACTIONS['Down']: 
                self.direction.y = 1
            elif ACTIONS['Up']:
                self.direction.y = -1
            else:
                self.direction.y = 0

        else:
            if CONTROLLERS[controller]['LS Right']: 
                self.direction.x = CONTROLLERS[controller]['LS Right']
            elif CONTROLLERS[controller]['LS Left']:
                self.direction.x = -CONTROLLERS[controller]['LS Left']
            else:
                self.direction.x = 0

            if CONTROLLERS[controller]['LS Down']: 
                self.direction.y = CONTROLLERS[controller]['LS Down']
            elif CONTROLLERS[controller]['LS Up']:
                self.direction.y = -CONTROLLERS[controller]['LS Up']
            else:
                self.direction.y = 0

    def update(self, dt):
        self.animate('idle', 6 * dt)
        self.input('Nintendo Switch Pro Controller')
        self.movement(dt)
        