import pygame
from settings import *

class EventHandler:
    def __init__(self, game):
        self.game = game
        self.joysticks = self.get_joysticks()

    def get_joysticks(self):
        joysticks = []
        for joy in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(joy)
            joystick.init()
            joysticks.append(joystick)
        return joysticks

    def keys_pressed(self):
        return pygame.key.get_pressed()

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

    def get_switch_pro_controller_state(self, joy):
        ls_axes = (joy.get_axis(0), joy.get_axis(1))
        rs_axes = (joy.get_axis(2), joy.get_axis(3))
        lt_axis = (joy.get_axis(4) + 1) / 2
        rt_axis = (joy.get_axis(5) + 1) / 2

        return {
            **self.get_axis_state('LS', ls_axes),
            **self.get_axis_state('RS', rs_axes),
            'L Trigger': lt_axis if lt_axis > DEADZONE else 0,
            'R Trigger': rt_axis if rt_axis > DEADZONE else 0,
            'A': joy.get_button(0),
            'B': joy.get_button(1),
            'X': joy.get_button(2),
            'Y': joy.get_button(3)
        }

    def get_ps4_controller_state(self, joy):
        ls_axes = (joy.get_axis(0), joy.get_axis(1))
        rs_axes = (joy.get_axis(2), joy.get_axis(3))
        lt_axis = (joy.get_axis(4) + 1) / 2
        rt_axis = (joy.get_axis(5) + 1) / 2

        return {
            **self.get_axis_state('LS', ls_axes),
            **self.get_axis_state('RS', rs_axes),
            'L Trigger': lt_axis if lt_axis > DEADZONE else 0,
            'R Trigger': rt_axis if rt_axis > DEADZONE else 0,
            'Cross': joy.get_button(0),
            'Circle': joy.get_button(1),
            'Square': joy.get_button(2),
            'Triangle': joy.get_button(3)
        }

    def get_axis_state(self, stick, axes):
        x_axis, y_axis = axes
        return {
            f'{stick} Left': abs(x_axis) if x_axis < -DEADZONE else 0,
            f'{stick} Right': x_axis if x_axis > DEADZONE else 0,
            f'{stick} Up': abs(y_axis) if y_axis < -DEADZONE else 0,
            f'{stick} Down': y_axis if y_axis > DEADZONE else 0,
        }

    def get_controller_state(self, controller_name, joy):
        if controller_name == 'Nintendo Switch Pro Controller':
            return self.get_switch_pro_controller_state(joy)
        elif controller_name == 'PS4 Controller':
            return self.get_ps4_controller_state(joy)
        return {}

    def joystick_pressed(self):
        for joy in self.joysticks:
            name = joy.get_name()
            if name in CONTROLLERS:
                controller_state = self.get_controller_state(name, joy)
                CONTROLLERS[name].update(controller_state)


    
