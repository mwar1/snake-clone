# snake-clone

A basic clone of the classic arcade game 'Snake' made with Python and Pygame.

## apple.py
Contains the code for generating and replacing an Apple object which the player eats to increase the length of the snake.

## tile.py
Creates the background for the game, using an array of Tile objects. Possibly unnecessary to put into its own class but it is what it is.

## score.py
Contains the code to display and update a score in the top-left corner of the screen.

## snake.py
Contains the code for creating a BodyPart object, which can be added to the snake to make it longer. Also is used to update the position of each BodyPart every game tick.

## collisions.py
### bodyCollision(snake)
Used to check if the snake has crashed into itself.
### wallCollision(snake)
Used to check if the snake has crashed into the wall.

## rainbow.py
Contains a dictionary of colours and their matching RGB values.

## main.py
Links all these functions and classes together, along with the main game loop and global variables to run the game and process events.
