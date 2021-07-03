import pygame
from pygame.locals import *


pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('first game')

# define  game variables
tile_size = 50

 
#image
bg_img = pygame.image.load('resources/sky.jpg')

def draw_grid():
    for line in range(0, 16):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('resources/ghost.png')
        self.image = pygame.transform.scale(img, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.x = x + 50
        self.rect.y = y + 50
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        dx = 0
        dy = 0
        downY = 0
        downX = 0
        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 1
            downX -= 1
        if key[pygame.K_RIGHT]:
            dx += 1
        if key[pygame.K_UP]:
            dy -= 1
            downY -= 1
        if key[pygame.K_DOWN]:
            dy += 1
        
        #check for collision
        for tile in world.tile_list:
            #check for collision in y direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                if downY < 0:
                    dy = tile[1].bottom - self.rect.top 
                if dy > 0:
                    dy = tile[1].top - self.rect.bottom 
                if downX < 0:
                    dx = tile[1].right - self.rect.left
                if dx > 0:
                    dx = tile[1].left - self.rect.right
            #collision for edges of the screen



        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy    
        # draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

#calculate new player position and check collison new position adjust player position. 

class World():
    def __init__(self, data):
        self.tile_list = []


        #load images
        dirt_img = pygame.image.load('resources/wall.png')
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile) # store useful tile information
                col_count += 1
            row_count += 1 

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])  
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2) 


#rectangle 
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
[1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
[1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]


player = Player(0, tile_size)
world = World(world_data)

running = True

while running:

    screen.blit(bg_img, (0,  0))

    draw_grid()

    print(world.tile_list)
    world.draw()
    player.update()        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    running = False
            
        pygame.display.update()

    



