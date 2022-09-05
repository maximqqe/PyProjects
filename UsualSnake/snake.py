import sys
import pygame
from random import randrange

COLOR_BLACK = pygame.Color('black')
COLOR_GREEN = pygame.Color('green')
COLOR_RED = pygame.Color('red')

len = 1
x, y = randrange(0, 500, 50), randrange(0, 500, 50)
apple = randrange(0, 500, 50), randrange(0, 500, 50)

player = [(x, y)]
dx, dy = 0, 0
speed = 7

run = True

pygame.init()
screen = pygame.display.set_mode((500, 500))

#спавн яблока

def spawnApple(bool):
    if bool:
        global apple
        apple = randrange(0, 500, 50), randrange(0, 500, 50)
        if apple not in player:
            pygame.draw.rect(screen, COLOR_RED, (apple[0], apple[1], 50, 50))
        else:
            spawnApple(True)
    else:
        pygame.draw.rect(screen, COLOR_RED, (apple[0], apple[1], 50, 50))

#механика игры

while run:

    screen.fill(COLOR_BLACK)

    for i,j in player:
        pygame.draw.rect(screen, COLOR_GREEN, (i, j, 48, 48))
    spawnApple(False)
    x += dx*50
    y += dy*50

    if x > 500:
        x = 0
    elif x < 0:
        x = 500
    if y > 500:
        y = 0
    elif y < 0:
        y = 500

    player.append((x,y))
    player = player[-len:]
    pygame.display.flip()
    pygame.time.Clock().tick(speed)

    if player[-1] == apple:
        spawnApple(True)
        len += 1
        speed += 0.2


#рестарт при столкновении

    for cell in player:
        if player.count(cell) > 1:
            dx,dy = 0,0
            len = 1
            speed = 7
            apple = randrange(0, 500, 50), randrange(0, 500, 50)
            player = [(randrange(0, 500, 50), randrange(0, 500, 50))]
        if cell[0] > 500:
            print(cell)
        if cell[0] < 0:
            print(cell)
        if cell[1] > 500:
            print(cell)
        if cell[1] < 0:
            print(cell)
#выход

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#управление

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_d]:
        dx, dy = 1, 0

