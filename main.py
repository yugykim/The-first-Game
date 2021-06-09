import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((550, 550))
        self.block = pygame.image.load("resources/ghost.png").convert()
        self.block = pygame.transform.scale(self.block,(30, 30))
        self.back = pygame.image.load("resources/sky.jpg").convert()
        self.back = pygame.transform.scale(self.back,(550, 550))
        self.wall = pygame.image.load("resources/wall.png").convert()
        self.wall = pygame.transform.scale(self.wall,(150, 30))
        self.over = pygame.image.load("resources/game-over.png").convert()
        self.over = pygame.transform.scale(self.over,(550, 550))
        self.block_over = pygame.image.load("resources/brickwall.png").convert()
        self.block_over = pygame.transform.scale(self.block_over,(30, 30))
        self.x = 0
        self.y = 0
        self.x_lo = [0, 50, 200, 400, 400]
        self.y_lo = [100, 130, 250, 280, 300, 350, 400]
    
    def draw(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change
        self.x += self.x_change
        self.y += self.y_change
        self.surface.blit(self.block, (self.x, self.y))
        pygame.display.update()

    
    def wall_im(self):
        self.surface.blit(self.wall, (0, 100))
        self.surface.blit(self.wall, (400, 200))
        self.surface.blit(self.wall, (200, 130))
        self.surface.blit(self.wall, (0, 250))
        self.surface.blit(self.wall, (400, 280))
        self.surface.blit(self.wall, (50, 300))
        self.surface.blit(self.wall, (300, 350))
        self.surface.blit(self.wall, (200, 400))

    def run(self):
        running = True
        while running:
            self.surface.fill((0,0,0))
            self.surface.blit(self.back, (0, 0))
            self.surface.blit(self.block, (self.x, self.y))
            self.surface.blit(self.block_over, (510, 510))
            self.wall_im()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.draw(0, -10)
                    elif event.key == K_DOWN:
                        self.draw(0, 10)
                    elif event.key == K_LEFT:
                        self.draw(-10, 0)
                    elif event.key == K_RIGHT:
                        self.draw(10, 0)             
                    elif event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    game.run()
