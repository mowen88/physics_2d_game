
from state import State
from settings import *
from entities import Entity, AnimatedEntity
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
		self.max_items_per_column = 5
		self.options_list = ['Start Game', 'Audio', 'Controls', 'Quit', 'Opt 5', 'Option 6', 'Option 7777777']
		self.menu_objects = self.get_options()

		self.index = 0
		self.cursor = AnimatedEntity([self.update_sprites, self.drawn_sprites], self.menu_objects[self.index].rect.midleft, '../assets/particles/menu_cursor_left', 'player')

	def navigate(self):
		if ACTIONS['Down']:
			self.index = (self.index + 1) % len(self.menu_objects)
			print(self.index)
			ACTIONS['Down'] = False

		elif ACTIONS['Up']:
			self.index = (self.index - 1) % len(self.menu_objects)
			print(self.index)
			ACTIONS['Up'] = False

		if ACTIONS['Left'] or ACTIONS['Right']:
			if self.index < self.max_items_per_column:
				self.index = min(self.index + self.max_items_per_column, len(self.options_list)-1)
			else:
				self.index -= self.max_items_per_column
			ACTIONS['Right'] = False
			ACTIONS['Left'] = False

		self.cursor.rect.midright = self.menu_objects[self.index].rect.midleft

	def get_options(self, centred=False):
	    obj_list = []
	    offset = 0
	    start_x = WIDTH * 0.2
	    start_height = HEIGHT * 0.4

	    for index, option in enumerate(self.options_list):
	        if index % self.max_items_per_column == 0 and index != 0:
	            start_x += WIDTH * 0.3
	            offset = 0

	        offset += self.line_spacing
	        image = self.game.font.render(option, False, COLOURS['white'])
	        adjusted_start_x = start_x
	        if centred:
	        	adjusted_start_x = start_x + image.get_size()[0]
	        pos = (adjusted_start_x, start_height + offset)
	        menu_obj = Entity([self.drawn_sprites], pos, image, 'player', 'topleft')
	        obj_list.append(menu_obj)

	    return obj_list


	def next_scene(self):
		Scene(self.game).enter_state()

	def update(self, dt):
		if ACTIONS['Pause']:
			self.transition.on_complete = [self.next_scene]

		self.navigate()

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
