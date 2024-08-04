import pygame
import pymunk
from state import State
from settings import *
from entities import Entity, PhysicsEntity, PhysicsLine
from player import Player
from transitions import Fade, CirclesTransition

class Scene(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.bg_colour = COLOURS['green']
        self.transition = CirclesTransition(self.game)

        self.space = pymunk.Space()
        self.space.gravity = (0.0, -100.0)
        self.space.sleep_time_threshold = 0.3

        self.drawn_sprites = pygame.sprite.LayeredUpdates()
        self.update_sprites = pygame.sprite.Group()

        self.box = PhysicsEntity(self.space, [self.drawn_sprites, self.update_sprites], 'player', (40,40), 30, COLOURS['black'])
        self.floor = PhysicsLine(self.space, (100,200),(200,200))
        self.floor2 = PhysicsLine(self.space, (10,100),(100,200))
        self.floor3 = PhysicsLine(self.space, (200,200),(400,100))

    def next_scene(self):
        self.exit_state()

    def update(self, dt):
        if ACTIONS['Pause']:
            self.transition.on_complete = [self.next_scene]

        self.update_sprites.update(dt)

        self.transition.update(dt)
        self.space.step(1/FPS)

    def draw(self, screen):
        screen.fill(self.bg_colour)
        self.drawn_sprites.draw(screen)
        self.floor.draw(screen)
        self.floor2.draw(screen)
        self.floor3.draw(screen)

        self.game.render_text('Made with', COLOURS['green'], self.game.font, (WIDTH * 0.5, HEIGHT * 0.2))
        self.transition.draw(screen)

        self.debug([str('FPS: '+ str(round(self.game.clock.get_fps(), 2))),
                    str(len(self.game.stack)),
                    None])
