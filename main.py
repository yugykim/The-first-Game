import pygame
from pygame.locals import *

def draw_block():
    surface.fill((110,110,5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500))   #size of the screen
    surface.fill((255,255,255))   #color

    block = pygame.image.load("resources/Red_button.jpg").convert()
    block = pygame.transform.scale(block, (50, 100))
    block_x = 100
    block_y = 100

    running = True

    while running:
        draw_block()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    pass
            elif event.type == QUIT:
                running == False
