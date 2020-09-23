def bodyCollision(snake):
    head = snake.sprites()[0]

    for part in snake.sprites():
        if part.x == head.x and part.y == head.y and snake.sprites().index(part) != 0:
            return True
    return False

def wallCollision(snake):
    head = snake.sprites()[0]

    return head.x < 0 or head.x > 18 or head.y < 0 or head.y > 18
