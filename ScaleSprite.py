import pygame

class ScaleSprite(pygame.sprite.Sprite):
    def __init__(self, center, image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center = center)
        self.mode = 1
        self.grow = 0

    def update(self):
        if self.grow > 100:
            self.mode = -1
        if self.grow < 1:
            self.mode = 1
        self.grow += 1 * self.mode 

        orig_x, orig_y = self.original_image.get_size()
        size_x = orig_x + round(self.grow)
        size_y = orig_y + round(self.grow)
        self.image = pygame.transform.scale(self.original_image, (size_x, size_y))
        self.rect = self.image.get_rect(center = self.rect.center)


