
from state import State
from settings import *
from entities import Entity
from transitions import Fade, CirclesTransition
from scene import Scene

class PygameLogo(State):
	def __init__(self, game):
		State.__init__(self, game)

		self.timer = 0
		self.duration = 1.5
		self.transition = Fade(self.game)
		Entity([self.drawn_sprites], (WIDTH * 0.5, HEIGHT * 0.6), pygame.image.load('../assets/pygame_logo.png').convert_alpha(), 'background')

	def next_scene(self):
		Menu(self.game).enter_state()

	def update(self, dt):
		if self.timer >= self.duration:
			self.timer = 0
			self.transition.on_complete = [self.next_scene]
		else:
			self.timer += dt

		self.update_sprites.update(dt)
		self.transition.update(dt)

	def draw(self, screen):
		screen.fill(COLOURS['grey'])
		self.drawn_sprites.draw(screen)
		self.game.render_text('Made with', COLOURS['white'], self.game.font, (WIDTH * 0.5, HEIGHT * 0.2))
		self.transition.draw(screen)

class Menu(State):
	def __init__(self, game):
		State.__init__(self, game)

		self.bg_colour = COLOURS['red']
		self.transition = CirclesTransition(self.game)
		self.selection = None
		self.line_spacing = TILESIZE * 2
		self.options_list = ['Start Game', 'Audio', 'Controls', 'Quit']
		self.menu_objects = self.get_options()
		
	def get_options(self):
		offset = 0
		start_height = HEIGHT * 0.4
		for option in self.options_list:
			offset += self.line_spacing
			image = self.game.font.render(option, False, COLOURS['white'])
			pos = (WIDTH * 0.5, start_height + offset)
			menu_object = Entity([self.drawn_sprites], pos, image, 'player')

	def next_scene(self):
		Scene(self.game).enter_state()

	def update(self, dt):
		if ACTIONS['Pause']:
			self.transition.on_complete = [self.next_scene]

		self.update_sprites.update(dt)
		self.transition.update(dt)

	def draw(self, screen):
		screen.fill(self.bg_colour)
		self.drawn_sprites.draw(screen)
		self.game.render_text('First Menu !', COLOURS['white'], self.game.font, (WIDTH * 0.5, HEIGHT * 0.2))

		self.transition.draw(screen)

		self.debug([str('FPS: '+ str(round(self.game.clock.get_fps(), 2))),
					str(len(self.game.stack)),
					None])
