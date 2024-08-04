import pygame

TILESIZE = 8
FPS = 60

RES = WIDTH, HEIGHT = pygame.math.Vector2(512, 288)
HALF_WIDTH, HALF_HEIGHT = RES/2
ASPECT_RATIO = (WIDTH/HEIGHT)

LAYERS = ['background',
		  'objects',
		  'player',
		  'particles',
		  'blocks',
		  'foreground']

#FONT = '../assets/EndlessBossBattleRegular.ttf'
FONT = '../assets/PixelFont.ttf'
#FONT = '../assets/homespun.ttf'

COLOURS = {'black':(0,0,0), 'white':(255,255,255),'red':(255,0,0), 'green':(0,255,0), 'pale_yellow':(201,204,161),'yellow':(202,160,90),'orange':(174,106,71), 'red':(139,64,73), 'burgundy':(84,51,68), 'grey':(81,82,98),'green':(99,120,125),'pale_green':(142,160,145)}

ACTIONS = {'Left':False, 'Right':False, 'Up':False, 'Down':False, 'Jump':False, 'Attack':False, 'Dash':False, 'Focus':False, 'Inventory':False, 'Pause':False}

KEY_MAP = {'Left':pygame.K_LEFT, 'Right':pygame.K_RIGHT, 'Up':pygame.K_UP, 'Down':pygame.K_DOWN, 'Jump':pygame.K_z,
			'Attack':pygame.K_x, 'Dash':pygame.K_c, 'Focus':pygame.K_r, 'Inventory':pygame.K_j, 'Pause':pygame.K_SPACE}
DEFAULT_KEY_MAP = {'Left':pygame.K_LEFT, 'Right':pygame.K_RIGHT, 'Up':pygame.K_UP, 'Down':pygame.K_DOWN, 'Jump':pygame.K_z,
			'Attack':pygame.K_x, 'Dash':pygame.K_c, 'Focus':pygame.K_r, 'Inventory':pygame.K_i, 'Pause':pygame.K_SPACE}