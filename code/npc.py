import pygame
from support import *
from settings import *
from entities import AnimatedEntity

class NPC(AnimatedEntity):
    def __init__(self, groups, pos, path, z='background'):
        super().__init__(groups, pos, path)

        self.import_images(path)
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.25, -self.rect.height*0.25)

    def movement(self, dt):
        self.hitbox.centerx += self.direction.x * self.speed * dt
        self.hitbox.centery += self.direction.y * self.speed * dt

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize() 

        self.rect.center = self.hitbox.center

    def update(self, dt):
        self.animate('idle', 6 * dt)
        self.movement(dt)



