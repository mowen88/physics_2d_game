import pygame, math
from support import *
from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE)), z='background', centred='center'):
        super().__init__(groups)

        self.image = surf
        self.rect = self.get_pos(pos, centred)
        self.z = z

    def get_pos(self, pos, centred):
        rect_methods = {
            'topleft': self.image.get_rect(topleft=pos),
            'topright': self.image.get_rect(topright=pos),
            'bottomleft': self.image.get_rect(bottomleft=pos),
            'bottomright': self.image.get_rect(bottomright=pos),
            'center': self.image.get_rect(center=pos)
        }
        return rect_methods.get(centred, self.image.get_rect(center=pos))


class AnimatedEntity(pygame.sprite.Sprite):
    def __init__(self, groups, pos, path, z='background'):
        super().__init__(groups)

        self.frame_index = 0
        self.frames = get_images(path)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy().inflate(0,0)

    def animate(self, state, speed, loop=True):
        self.frame_index += speed
        self.frame_index = self.frame_index % len(self.frames)
        self.image = self.frames[int(self.frame_index)]
        
    def update(self, dt):
        self.animate('idle', 6 * dt)
        self.hitbox.center = self.rect.center
