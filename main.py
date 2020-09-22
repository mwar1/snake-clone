import pygame, tile, snake, apple
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
snakeParts = pygame.sprite.Group()
apples = pygame.sprite.Group()

## Create the initial apple
apples.add(apple.Apple())

## Create the initial snake
snakeParts.add(snake.BodyPart(0, 7, 9))
snakeParts.add(snake.BodyPart(1, 6, 9))
snakeParts.add(snake.BodyPart(2, 5, 9))
snakeParts.add(snake.BodyPart(3, 4, 9))

## Starts the snake moving to the right
snakeDirection = (0,-1)
snakeLength = 4

## Create a Group of Tile objects for the background
for i in range(19):
    for j in range(19):
        tiles.add(tile.Tile((i*19)+j))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeDirection = (1, 0)
            elif event.key == pygame.K_LEFT:
                snakeDirection = (-1, 0)
            elif event.key == pygame.K_DOWN:
                snakeDirection = (0, 1)
            elif event.key == pygame.K_UP:
                snakeDirection = (0, -1)

    ## Drawing the background
    screen.fill(colours["WHITE"])

    ## Check if snake has eaten the apple
    if snakeParts.sprites()[0].x == apples.sprites()[0].x and snakeParts.sprites()[0].y == apples.sprites()[0].y:
        snakeLength += 1
        snakeParts.add(snake.BodyPart(snakeLength-1, snakeParts.sprites()[-1].x - snakeDirection[0], snakeParts.sprites()[-1].y - snakeDirection[1]))
        apples.sprites()[0].newApple()

    ## Refreshing and updating
    for i in range(len(snakeParts.sprites())-1, 0, -1):
        snakeParts.sprites()[i].x = snakeParts.sprites()[i-1].x
        snakeParts.sprites()[i].y = snakeParts.sprites()[i-1].y
        snakeParts.sprites()[i].updateRectPos()

    snakeParts.sprites()[0].x += snakeDirection[0]
    snakeParts.sprites()[0].y += snakeDirection[1]
    snakeParts.sprites()[0].updateRectPos()

    ## Drawing sprites
    tiles.draw(screen)
    apples.draw(screen)
    snakeParts.draw(screen)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
