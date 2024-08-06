import pygame, math
from support import *
from settings import *

class Entity(pygame.sprite.Sprite):
	def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE)), z= 'background'):
		super().__init__(groups)

		self.image = surf
		self.rect = self.image.get_rect(center=pos)
		self.z = z

class AnimatedEntity(pygame.sprite.Sprite):
    def __init__(self, groups, pos, path, z='background'):
        super().__init__(groups)

        self.import_images(path)
        self.frame_index = 0
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy().inflate(0,0)

    def import_images(self, path):
        path = f'../assets/{path}/'
        self.animations = get_animations(path)
        for animation in self.animations.keys():
            full_path = path + animation
            self.animations[animation] = get_images(full_path)

        self.image = next(iter(self.animations.values()))[0].convert_alpha()

    def animate(self, state, speed, loop=True):
        self.frame_index += speed
        if self.frame_index >= len(self.animations[state]):
            self.frame_index = 0 if loop else len(self.animations[state]) - 1

        self.image = self.animations[state][int(self.frame_index)]
        
    def update(self, dt):
        self.animate('idle', 6 * dt)
        self.hitbox.center = self.rect.center
