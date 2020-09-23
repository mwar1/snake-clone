import pygame, random
from .rainbow import colours

class Tile(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()

        self.index = index
        self.width = 50
        self.height = 50
        self.apple = False

        self.image = pygame.Surface([self.width, self.height])
        if self.index % 2 == 0:
            self.image.fill(colours["LIME"])
        else:
            self.image.fill(colours["GREEN"])

        self.rect = self.image.get_rect()
        self.rect.x = (self.index % 19) * self.width
        self.rect.y = (self.index // 19) * self.height
