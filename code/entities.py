import pygame, pymunk, math
from support import *
from settings import *

class Entity(pygame.sprite.Sprite):
	def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE)), z= 'background'):
		super().__init__(groups)

		self.image = surf
		self.rect = self.image.get_rect(center=pos)
		self.z = z

class PhysicsLine:
    def __init__(self, space, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.color = COLOURS['black']

        # create a segment - a static line that physics objects collide with:
        # don't forget to invert the y values, since pymunk has an inverted y axis:
        line = pymunk.Segment(space.static_body, (point_1[0], -point_1[1]), (point_2[0], -point_2[1]), 1.0)
        line.friction = 1.0
        # add the line to the physics space so it interacts with other objects in the physics space:
        space.add(line)

    # drawing the line unto the screen:
    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.point_1, self.point_2)

class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, space, groups, name, pos, size, color):
        super().__init__(groups)
        self.size = size
        self.color = color
        self.x, self.y = pos

        self.name = name
        self.angle_index = 16
        self.import_images()
        self.frame_index = 0
        self.image_cache = {}
        self.precompute_rotated_images()
        self.image = self.animations['idle'][self.frame_index].convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.25, -self.rect.height*0.25)

        # if poly
        half_width, half_height = round(size / 2), round(size / 2)
        points = [(-half_width, -half_height), (-half_width, half_height), (half_width, half_height), (half_width, -half_height)]

        # If circle
        radius = 16

        mass = 1.0
        moment = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC)
        body.position = (self.x, -self.y)
        self.body = body
        self.angle = self.body.angle
        shape = pymunk.Circle(body, radius)
        shape.friction = 1
        space.add(body, shape)

    def import_images(self):
        path = f'../assets/characters/{self.name}/'
        self.animations = get_animations(path)
        for animation in self.animations.keys():
            full_path = path + animation
            self.animations[animation] = get_images(full_path)

    def precompute_rotated_images(self):
        for state in self.animations.keys():
            self.image_cache[state] = []
            for image in self.animations[state]:
                image_cache_state = []
                for angle in range(0, 360, self.angle_index):
                    rotated_image = pygame.transform.rotate(image, angle)
                    image_cache_state.append(rotated_image)
                self.image_cache[state].append(image_cache_state)

    def animate(self, state, speed, loop=True):
        self.frame_index += speed
        if self.frame_index >= len(self.animations[state]):
            if loop:
                self.frame_index = 0
            else:
                self.frame_index = len(self.animations[state]) - 1

        angle = math.degrees(self.body.angle) % 360
        angle_index = int(angle / self.angle_index)
        self.image = self.image_cache[state][int(self.frame_index)][angle_index]
        
        # Update the rect and hitbox
        self.rect = self.image.get_rect(center=self.rect.center)
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.25, -self.rect.height * 0.25)

    def update(self, dt):
        self.animate('run', 6 * dt)
        self.rect.center = (self.body.position.x, -self.body.position.y)
        self.hitbox.center = self.rect.center
        self.angle = math.degrees(self.body.angle)
        print(self.angle)
