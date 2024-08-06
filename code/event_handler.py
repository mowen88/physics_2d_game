import pygame
from settings import *

class EventHandler:
	def __init__(self, game):

		self.game = game
		self.joysticks = []
		self.joysticks = self.get_joysticks()

	def get_joysticks(self):
		joysticks = []
		for joy in range(pygame.joystick.get_count()):
			joystick = pygame.joystick.Joystick(joy)
			joystick.init()
			joysticks.append(joystick)
		return joysticks

	def key_events(self):
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				self.game.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.game.quit()
				if not self.game.block_input:
					for action, value in KEY_MAP.items():
						if value == event.key:
							ACTIONS[action] = True
			if event.type == pygame.KEYUP:
				for action, value in KEY_MAP.items():
					if value == event.key:
						ACTIONS[action] = False

	def joystick_events(self):
		for joy in self.joysticks:
			name = joy.get_name()
			joy.get_axis(0)
			
			if name == 'Nintendo Switch Pro Controller':
				ls_x_axis = joy.get_axis(0)
				ls_y_axis = joy.get_axis(1)
				rs_x_axis = joy.get_axis(2)
				rs_y_axis = joy.get_axis(3)
				# change weird trigger values so it ranges from 0 to 1 instead of -1 to 1
				lt_axis = joy.get_axis(4)
				rt_axis = joy.get_axis(5)
				adjusted_lt_axis = (lt_axis + 1)/2
				adjusted_rt_axis = (rt_axis + 1)/2

				# joysticks
				if abs(ls_x_axis) > DEADZONE:
					if ls_x_axis < 0:
						CONTROLLERS[name]['LS Left'] = abs(ls_x_axis)
						CONTROLLERS[name]['LS Right'] = 0
					else:
						CONTROLLERS[name]['LS Right'] = ls_x_axis
						CONTROLLERS[name]['LS Left'] = 0
				else:
					CONTROLLERS[name]['LS Left'] = 0
					CONTROLLERS[name]['LS Right'] = 0

				if abs(ls_y_axis) > DEADZONE:
					if ls_y_axis < 0:
						CONTROLLERS[name]['LS Up'] = abs(ls_y_axis)
						CONTROLLERS[name]['LS Down'] = 0
					else:
						CONTROLLERS[name]['LS Down'] = ls_y_axis
						CONTROLLERS[name]['LS Up'] = 0
				else:
					CONTROLLERS[name]['LS Up'] = 0
					CONTROLLERS[name]['LS Down'] = 0

				if abs(rs_x_axis) > DEADZONE:
					if rs_x_axis < 0:
						CONTROLLERS[name]['RS Left'] = abs(rs_x_axis)
						CONTROLLERS[name]['RS Right'] = 0
					else:
						CONTROLLERS[name]['RS Right'] = rs_x_axis
						CONTROLLERS[name]['RS Left'] = 0
				else:
					CONTROLLERS[name]['RS Left'] = 0
					CONTROLLERS[name]['RS Right'] = 0

				if abs(rs_y_axis) > DEADZONE:
					if rs_y_axis < 0:
						CONTROLLERS[name]['RS Up'] = abs(rs_y_axis)
						CONTROLLERS[name]['RS Down'] = 0
					else:
						CONTROLLERS[name]['RS Down'] = rs_y_axis
						CONTROLLERS[name]['RS Up'] = 0
				else:
					CONTROLLERS[name]['RS Up'] = 0
					CONTROLLERS[name]['RS Down'] = 0

				# triggers
				if abs(lt_axis) > DEADZONE:
					CONTROLLERS[name]['L Trigger'] = adjusted_lt_axis
				else:
					CONTROLLERS[name]['L Trigger'] = 0

				if abs(rt_axis) > DEADZONE:
					CONTROLLERS[name]['R Trigger'] = adjusted_rt_axis
				else:
					CONTROLLERS[name]['R Trigger'] = 0
				
				# buttons
				CONTROLLERS[name]['A'] = joy.get_button(0)
				CONTROLLERS[name]['B'] = joy.get_button(1)
				CONTROLLERS[name]['X'] = joy.get_button(2)
				CONTROLLERS[name]['Y'] = joy.get_button(3)

				print(joy.get_axis(4))

			if name == 'PS4 Controller':
				ls_x_axis = joy.get_axis(0)
				ls_y_axis = joy.get_axis(1)
				rs_x_axis = joy.get_axis(2)
				rs_y_axis = joy.get_axis(3)
				lt_axis = (joy.get_axis(4)+1)/2
				rt_axis = (joy.get_axis(5)+1)/2

				# joysticks
				if abs(ls_x_axis) > DEADZONE:
					if ls_x_axis < 0:
						CONTROLLERS[name]['LS Left'] = abs(ls_x_axis)
						CONTROLLERS[name]['LS Right'] = 0
					else:
						CONTROLLERS[name]['LS Right'] = ls_x_axis
						CONTROLLERS[name]['LS Left'] = 0
				else:
					CONTROLLERS[name]['LS Left'] = 0
					CONTROLLERS[name]['LS Right'] = 0

				if abs(ls_y_axis) > DEADZONE:
					if ls_y_axis < 0:
						CONTROLLERS[name]['LS Up'] = abs(ls_y_axis)
						CONTROLLERS[name]['LS Down'] = 0
					else:
						CONTROLLERS[name]['LS Down'] = ls_y_axis
						CONTROLLERS[name]['LS Up'] = 0
				else:
					CONTROLLERS[name]['LS Up'] = 0
					CONTROLLERS[name]['LS Down'] = 0

				if abs(rs_x_axis) > DEADZONE:
					if rs_x_axis < 0:
						CONTROLLERS[name]['RS Left'] = abs(rs_x_axis)
						CONTROLLERS[name]['RS Right'] = 0
					else:
						CONTROLLERS[name]['RS Right'] = rs_x_axis
						CONTROLLERS[name]['RS Left'] = 0
				else:
					CONTROLLERS[name]['RS Left'] = 0
					CONTROLLERS[name]['RS Right'] = 0

				if abs(rs_y_axis) > DEADZONE:
					if rs_y_axis < 0:
						CONTROLLERS[name]['RS Up'] = abs(rs_y_axis)
						CONTROLLERS[name]['RS Down'] = 0
					else:
						CONTROLLERS[name]['RS Down'] = rs_y_axis
						CONTROLLERS[name]['RS Up'] = 0
				else:
					CONTROLLERS[name]['RS Up'] = 0
					CONTROLLERS[name]['RS Down'] = 0

				# triggers
				if lt_axis > DEADZONE:
					CONTROLLERS[name]['L Trigger'] = lt_axis
				else:
					CONTROLLERS[name]['L Trigger'] = 0

				if rt_axis > DEADZONE:
					CONTROLLERS[name]['R Trigger'] = rt_axis
				else:
					CONTROLLERS[name]['R Trigger'] = 0

				# BUTTONS
				CONTROLLERS[name]['Cross'] = joy.get_button(0)
				CONTROLLERS[name]['Circle'] = joy.get_button(1)
				CONTROLLERS[name]['Square'] = joy.get_button(2)
				CONTROLLERS[name]['Triangle'] = joy.get_button(3)








	






		

