import pygame, random
from rainbow import colours

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 15
        self.y = 9

        self.image = pygame.Surface([50,50])
        self.image.fill(colours["YELLOW"])

        self.rect = self.image.get_rect()
        self.rect.x = self.x * 50
        self.rect.y = self.y * 50

    def newApple(self, snakeParts):
        clear = False

        self.x = random.randint(0, 18)
        self.y = random.randint(0, 18)

        while not clear:
            self.x = random.randint(0, 18)
            self.y = random.randint(0, 18)
            for part in snakeParts.sprites():
                if part.x == self.x and part.y == self.y:
                    self.x = random.randint(0, 18)
                    self.y = random.randint(0, 18)
                    break
            else:
                clear = True

        self.rect.x = self.x * 50
        self.rect.y = self.y * 50
