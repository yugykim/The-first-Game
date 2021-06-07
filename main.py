import pygame
from pygame.locals import *
import random

class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/ghost.png").convert()
        self.block = pygame.transform.scale(self.block,(30, 30))
        self.enemy = pygame.image.load("resources/ghost copy.png").convert()
        self.enemy = pygame.transform.scale(self.enemy,(30, 30))
        self.x = 100
        self.y = 100
        self.enemy_x = random.randint(0, 450)
        self.enemy_y = random.randint(50, 150)
        self.size = 1


    def draw(self):
        self.parent_screen.fill((255, 255, 255))
        self.parent_screen.blit(self.block, (self.x, self.y))
        self.enemy_move()
        pygame.display.flip()

    def move_up(self):
        self.y -= 10
        self.draw()
    
    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def enemy_draw(self):
        self.parent_screen.blit(self.enemy, (self.enemy_x, self.enemy_y))
        pygame.display.flip()

    def enemy_move(self):
        if self.enemy_x >= 0:
            enemyX_change = 10
            self.enemy_x += enemyX_change
            self.enemy_draw()
        else:
            pass


            


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.snake.enemy_draw()
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        
                    if event.key == K_ESCAPE:
                        pygame.quit()
                elif event.type == QUIT:
                    pygame.quit()


        


if __name__ == '__main__':
    game = Game()
    game.run()





 

                
                
        