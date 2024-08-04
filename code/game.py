import pygame, sys, os, time, json, cProfile
from pygame import mixer
from os import walk
from menu import PygameLogo
from settings import *

class Game:
    def __init__(self):
 
        mixer.init()
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(RES, pygame.FULLSCREEN|pygame.SCALED)
        self.font = pygame.font.Font(FONT, 10)
        self.big_font = pygame.font.Font(FONT, 10)
        self.block_input = False
        self.running = True
        
        # states
        self.stack = []
        self.pygame_logo = PygameLogo(self)
        self.stack.append(self.pygame_logo)

    def get_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if not self.block_input:
                    for action, value in KEY_MAP.items():
                        if value == event.key:
                            ACTIONS[action] = True

            if event.type == pygame.KEYUP:
                for action, value in KEY_MAP.items():
                    if value == event.key:
                        ACTIONS[action] = False

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def reset_keys(self):
        for action in ACTIONS:
            ACTIONS[action] = False

    def get_csv_layer(self, path):
        grid = []
        with open(path) as layout:
            layer = reader(layout, delimiter = ',')
            for row in layer:
                grid.append(list(row))
            return grid

    def get_images(self, path):
        images = []
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            img = pygame.image.load(full_path).convert_alpha()
            images.append(img)
        return images

    def get_animations(self, path):
        animations = {}
        for file_name in os.listdir(path):
            animations.update({file_name:[]})
            full_path = os.path.join(path, file_name)
        return animations

    def render_text(self, text, colour, font, pos, topleft=False):
        surf = font.render (str(text), False, colour)
        rect = surf.get_rect(topleft = pos) if topleft else surf.get_rect(center = pos)
        self.screen.blit(surf, rect)

    def update(self, dt):
        self.stack[-1].update(dt)
 
    def draw(self, screen):
        self.stack[-1].draw(screen)
        pygame.display.flip()

    def main_loop(self):
        dt = self.clock.tick(FPS)/1000
        self.get_events()
        self.update(dt)
        self.draw(self.screen)
        
if __name__ == "__main__":
    game = Game()
    while game.running:
        game.main_loop()
        #cProfile.run("game.main_loop()", sort="cumulative")

