import pygame, pymunk, math
from support import *
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE)), z= 'background'):
		super().__init__(groups)

		self.name = 'player'
		self.import_images()
		self.frame_index = 0
		self.image = self.animations['idle'][self.frame_index].convert_alpha()
		self.rect = self.image.get_frect(center=pos)
		self.hitbox = self.rect.inflate(-self.rect.width/2, -self.rect.height/2)
		self.z = z

	def import_images(self):
		path = f'../assets/characters/{self.name}/'

		self.animations = get_animations(path)

		for animation in self.animations.keys():
			full_path = path + animation
			self.animations[animation] = get_images(full_path)

	def animate(self, state, loop=True):

		self.frame_index += 0.2
		if self.frame_index >= len(self.animations[state]):
			if loop: 
				self.frame_index = 0
			else:
				self.frame_index = len(self.animations[state]) -1			
		self.image = pygame.transform.flip(self.animations[state][int(self.frame_index)], self.facing, False)
