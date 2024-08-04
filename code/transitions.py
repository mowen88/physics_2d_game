import pygame
from settings import *


class Fade:
	def __init__(self, game, colour=COLOURS['black']):

		self.game = game
		self.surface = pygame.Surface(RES)
		self.surface.fill(colour)
		self.alpha = 255
		self.fade_duration = 2000
		self.on_complete = None
		self.transitioning = False
		self.game.reset_keys()

	def update(self, dt):

		self.game.block_input = True if self.alpha > 0 else False
		self.transitioning = True if self.on_complete is not None else False

		if self.transitioning:
			self.alpha += self.fade_duration * dt
			if self.alpha >= 255: 
				self.alpha = 255
				[func() for func in self.on_complete]	
				self.on_complete = None
				self.transitioning = False
		else:
			self.alpha -= self.fade_duration * dt
			if self.alpha <= 0: 
				self.alpha = 0
		
	def draw(self, screen):
		screen.blit(self.surface, (0,0))
		self.surface.set_alpha(self.alpha)

class CirclesTransition:
	def __init__(self, game, colour=COLOURS['red']):

		self.game = game
		self.surface = pygame.Surface(RES)
		self.margin = 8
		self.cols = int(WIDTH/self.margin)
		self.rows = int(HEIGHT/self.margin)
		self.size = 16
		self.max_size = self.size
		self.fade_speed = 20
		self.on_complete = None
		self.transitioning = False
		self.game.reset_keys()

	def draw_shapes(self, screen):
		for x in range(self.rows):
			for y in range(self.cols):
				pos_x = y * self.margin * 2
				pos_y = x * self.margin * 2
				pygame.draw.circle(screen, COLOURS['black'], (pos_x, pos_y), int(self.size))

	def update(self, dt):

		self.game.block_input = True if self.size > 0 else False
		self.transitioning = True if self.on_complete is not None else False

		if self.transitioning:
			self.size += self.fade_speed * dt
			if self.size > self.max_size:
				[func() for func in self.on_complete]	
				self.on_complete = None
				self.transitioning = False
		else:
			self.size -= self.fade_speed * dt
			if self.size <= 0:
				self.size = 0

	def draw(self, screen):
		self.draw_shapes(screen)