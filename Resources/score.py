import pygame, random
pygame.init()
from .rainbow import colours

font = pygame.font.Font("Fonts/numberFont.ttf", 22)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.image = pygame.Surface([900, 50])
        self.image.fill(colours["WHITE"])
        self.image.set_colorkey(colours["WHITE"])
        scoreText = font.render("SCORE : " + str(self.score), False, colours["BLACK"])
        self.image.blit(scoreText, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def addScore(self):
        self.score += 1

        scoreText = font.render("SCORE : " + str(self.score), False, colours["BLACK"])
        self.image.fill(colours["WHITE"])
        self.image.blit(scoreText, (0,0))
