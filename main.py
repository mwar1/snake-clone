import pygame
pygame.init()

from Resources import rainbow, tile, snake, apple, score, collisions

#from Resources.rainbow import colours
#from Resources.tile import Tile
#from Resources.snake import BodyPart
#from Resources.apple import Apple
#from Resources.score import Score
#from Resources.collisions import bodyCollision, wallCollision

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
scores = pygame.sprite.Group()

## Create the initial apple
apples.add(apple.Apple())

## Creates a scoreboard object
scores.add(score.Score())

## Create the initial snake
snakeParts.add(snake.BodyPart(0, 3, 9))
snakeParts.add(snake.BodyPart(1, 2, 9))
snakeParts.add(snake.BodyPart(2, 1, 9))
snakeParts.add(snake.BodyPart(3, 0, 9))

## Starts the snake moving to the right
snakeDirection = (1,0)
snakeLength = 4
dead = False

deathFont = pygame.font.Font("Fonts/numberFont.ttf", 65)
font = font = pygame.font.Font("Fonts/numberFont.ttf", 45)
deathText = deathFont.render("You died!", False, rainbow.colours["BLACK"])
playAgainText = font.render("Press Enter to play again", False, rainbow.colours["BLACK"])

def resetGame():
    dead = False

    snakeParts.empty()
    snakeParts.add(snake.BodyPart(0, 3, 9))
    snakeParts.add(snake.BodyPart(1, 2, 9))
    snakeParts.add(snake.BodyPart(2, 1, 9))
    snakeParts.add(snake.BodyPart(3, 0, 9))

    snakeLength = 4
    snakeDirection = (1,0)

    apples.empty()
    apples.add(apple.Apple())

    scores.empty()
    scores.add(score.Score())

    return dead, snakeParts, snakeLength, snakeDirection, apples, scores

## Create a Group of Tile objects for the background
for i in range(19):
    for j in range(19):
        tiles.add(tile.Tile((i*19)+j))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snakeDirection != (-1, 0):
                snakeDirection = (1, 0)
            elif event.key == pygame.K_LEFT and snakeDirection != (1, 0):
                snakeDirection = (-1, 0)
            elif event.key == pygame.K_DOWN and snakeDirection != (0, -1):
                snakeDirection = (0, 1)
            elif event.key == pygame.K_UP and snakeDirection != (0, 1):
                snakeDirection = (0, -1)
            elif event.key == pygame.K_RETURN and dead:
                dead, snakeParts, snakeLength, snakeDirection, apples, scores = resetGame()

    ## Check if snake has eaten the apple
    if snakeParts.sprites()[0].x == apples.sprites()[0].x and snakeParts.sprites()[0].y == apples.sprites()[0].y:
        snakeLength += 1
        snakeParts.add(snake.BodyPart(snakeLength-1, snakeParts.sprites()[-1].x - snakeDirection[0], snakeParts.sprites()[-1].y - snakeDirection[1]))

        scores.sprites()[0].addScore() ## Adds one to the score counter
        apples.sprites()[0].newApple(snakeParts) ## Generates a new random apple

    ## Check if snake has collided with itself or the wall
    if collisions.bodyCollision(snakeParts) or collisions.wallCollision(snakeParts):
        dead = True

    if dead:
        screen.blit(deathText, (475 - (deathFont.size("You died!")[0]/2), 350))
        screen.blit(playAgainText, (475 - (font.size("Press Enter to play again")[0]/2), 450))
    else:
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
        scores.draw(screen)

    pygame.display.flip()
    clock.tick(7)

pygame.quit()
