import pygame
from state import State
from settings import *
from entities import Entity, AnimatedEntity
from characters.player import Player
from transitions import Fade, CirclesTransition

class Scene(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.bg_colour = COLOURS['green']
        self.transition = CirclesTransition(self.game)

        self.update_sprites = pygame.sprite.Group()
        self.drawn_sprites = pygame.sprite.Group()

        self.player = Player([self.update_sprites, self.drawn_sprites], (HALF_WIDTH, HALF_HEIGHT), 'characters/player', 'player')
  
    def next_scene(self):
        self.exit_state()

    def create_scene(self):
        pass

    def update(self, dt):

    	if ACTIONS['Pause'] >= 0.2:
    		self.transition.on_complete = [self.next_scene]

    	self.update_sprites.update(dt)
    	self.transition.update(dt)

    def show_buttons(self, controller):
        return list(CONTROLLERS[controller].values())

    def draw(self, screen):

        screen.fill(self.bg_colour)
        self.drawn_sprites.draw(screen)
        pygame.draw.rect(screen, COLOURS['white'], self.player.hitbox, 2)

        self.game.render_text('Made with', COLOURS['green'], self.game.font, (WIDTH * 0.5, HEIGHT * 0.2))
        self.transition.draw(screen)

        self.debug([str('FPS: '+ str(round(self.game.clock.get_fps(), 2))),
                    str('Stack: ' + str(len(self.game.stack))),
                    str(self.show_buttons('Nintendo Switch Pro Controller')),
                    None])
