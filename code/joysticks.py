import pygame
from settings import *

class JoystickEvents:
	def __init__(self, game):

		self.game = game
		self.joysticks = []
		self.button_states = []

		for joy in range(pygame.joystick.get_count()):
			joystick = pygame.joystick.Joystick(joy)
			joystick.init()
			self.joysticks.append(joystick)
			self.button_states.append([0] * joystick.get_numbuttons())

		

