# Created by Anderson Greer in August of 2019
# This program is the game snake

import pygame
import random
import sys

def gameOver():

    font2 = pygame.font.SysFont(None, 100)
    gametext = font2.render("Game Over", True, (255, 255, 255))
    screen.blit(gametext, (240, 400))

def generateApplex():

    ax = random.randrange(0, width, snake_size)  # Generates the starting position of the apple

    if len(snake_coord) > 0:

        for item in snakeParts:
            # Makes sure the apple doesn't spawn in the apple
            if snake_coord[item][0] == ax:

                ax = random.randrange(0, width, snake_size)

    return ax

def generateAppley():

    ay = random.randrange(0, height, snake_size)

    if len(snake_coord) > 0:

        for item in snakeParts:
            # Makes sure the apple doesn't spawn in the apple
            if snake_coord[item][1] == ay:

                ay = random.randrange(0, height, snake_size)

    return ay

width = 800
height = 800

snake_size = 16
sx = 400  # Generates the starting position of the snake
sy = 400
direction = 'right'
snakeParts = []
partNum = 0

score = 0

snake_coord = [] # Array of coordinates for each pixel of the snake saved in tuples of (x, y)
coordindex = 0

BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
screen.fill((0,0,0))

gameover = False
firstLoop = True

ax = generateApplex()
ay = generateAppley()

clock = pygame.time.Clock()  # Creates the fps clock to slow the snake

while not gameover:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, BLUE, (sx, sy, snake_size, snake_size))
    pygame.draw.rect(screen, RED, (ax, ay, snake_size, snake_size))  # Creates the apple

    snake_coord.insert(0, (sx, sy))
    coordindex += 1

    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    scoretext = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(scoretext, (360, 0))

    if len(snake_coord) > 500:
        del snake_coord[500]

    for item in snakeParts:
        pygame.draw.rect(screen, BLUE, (snake_coord[item][0], snake_coord[item][1], snake_size, snake_size))

    # Detects if the arrow keys are pressed in order to move the snake
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and direction != 'left':
            direction = 'right'
        elif event.key == pygame.K_LEFT and direction != 'right':
            direction = 'left'
        elif event.key == pygame.K_UP and direction != 'down':
            direction = 'up'
        elif event.key == pygame.K_DOWN and direction != 'up':
            direction = 'down'

    # Moves the snake
    if direction == 'right':
        sx += snake_size
    elif direction == 'left':
        sx -= snake_size
    elif direction == 'down':
        sy += snake_size
    elif direction == 'up':
        sy -= snake_size

    # A collision between the snake and the apple
    if sx == ax and sy == ay:
        score += 10

        ax = random.randrange(0, width, snake_size)
        ay = random.randrange(0, height, snake_size)

        for i in range(0, 5):
            partNum += 1

            snakeParts.append(partNum)

            pygame.draw.rect(screen, BLUE, (snake_coord[partNum][0], snake_coord[partNum][1], snake_size, snake_size))

    clock.tick(15)

    # Checks if the snake head goes outside the frame
    if sx < -16:
        gameover = True
        gameOver()
    elif sx > width:
        gameover = True
        gameOver()
    elif sy < -16:
        gameover = True
        gameOver()
    elif sy > height:
        gameover = True
        gameOver()

    if len(snake_coord) > 0:

        for item in snakeParts:

            if snake_coord[item][0] == sx and snake_coord[item][1] == sy:
                for item in snakeParts:
                    pygame.draw.rect(screen, BLUE, (snake_coord[item][0], snake_coord[item][1], snake_size, snake_size))
                gameover = True
                gameOver()



    pygame.display.update()

pygame.time.wait(1000)
sys.exit()