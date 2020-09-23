import pygame
from .rainbow import colours

class BodyPart(pygame.sprite.Sprite):
    def __init__(self, index, x, y, head=False):
        super().__init__()

        self.index = index
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.head = head

        self.image = pygame.Surface([self.width, self.height])
        if index % 2 == 0:
            self.image.fill(colours["SNAKEPINK"])
        else:
            self.image.fill(colours["PINK"])

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 50
        self.rect.y = self.y * 50

    def updateRectPos(self):
        self.rect.x = self.x * 50
        self.rect.y = self.y * 50
