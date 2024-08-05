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

ACTIONS = {'Left':0, 'Right':0, 'Up':0, 'Down':0, 'Attack':0, 'Dash':0, 'Inventory':0, 'Pause':0}

KEY_MAP = {'Left':pygame.K_LEFT, 'Right':pygame.K_RIGHT, 'Up':pygame.K_UP, 'Down':pygame.K_DOWN,
			'Attack':pygame.K_x, 'Dash':pygame.K_c, 'Inventory':pygame.K_j, 'Pause':pygame.K_SPACE}
DEFAULT_KEY_MAP = {'Left':pygame.K_LEFT, 'Right':pygame.K_RIGHT, 'Up':pygame.K_UP, 'Down':pygame.K_DOWN,
			'Attack':pygame.K_x, 'Dash':pygame.K_c,'Inventory':pygame.K_i, 'Pause':pygame.K_SPACE}

DEADZONE = 0.2
TRIGGER_TO_BUTTON_DEADZONE = 0.3
CONTROLLERS = {
			'Nintendo Switch Pro Controller':
			{'LS Left':0, 'LS Right':0, 'LS Up':0, 'LS Down':0, 'RS Left':0, 'RS Right':0, 'RS Up':0, 'RS Down':0,
			'L Trigger':0, 'R Trigger':0, 'A':0, 'B':0, 'X':0, 'Y':0},
			'PS4 Controller':
			{'LS Left':0, 'LS Right':0, 'LS Up':0, 'LS Down':0, 'RS Left':0, 'RS Right':0, 'RS Up':0, 'RS Down':0,
			'L Trigger':0, 'R Trigger':0, 'Cross':0, 'Circle':0, 'Square':0, 'Triangle':0},
}