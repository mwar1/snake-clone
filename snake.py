import pygame
from rainbow import colours

class BodyPart(pygame.sprite.Sprite):
    def __init__(self, index, head=False):
        super().__init__()

        self.index = index
        self.head = head
        self.width = 50
        self.height = 50

        self.image = pygame.Surface([self.width, self.height])
        if self.index % 2 == 0:
            self.image.fill(colours["BLUE"])
        else:
            self.image.fill(colours["PURPLE"])

        self.rect = self.image.get_rect()
