import pygame, tile
from rainbow import colours
pygame.init()

SCREENWIDTH = 950
SCREENHEIGHT = 950
size = (SCREENWIDTH, SCREENHEIGHT)
clock = pygame.time.Clock()

carryOn = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

tiles = pygame.sprite.Group()
for i in range(19):
    for j in range(19):
        tiles.add(tile.Tile((i*19)+j))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False


    ## Drawing the background
    screen.fill(colours["WHITE"])

    tiles.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
