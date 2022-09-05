import sys
import pygame

COLOR_BLACK = pygame.Color('black')
COLOR_WHITE = pygame.Color('white')
COLOR_RED = pygame.Color("red")
cells = {x: '-' for x in range(9)}
pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont('arial', 100)
font1 = pygame.font.SysFont('arial', 30)
textX = font.render("x", True, COLOR_WHITE)
textO = font.render("o", True, COLOR_WHITE)
text_win = font1.render('x win', True, COLOR_RED)
text_loose = font1.render('o win', True, COLOR_RED)
text_draw = font1.render('draw', True, COLOR_RED)
text_restart = font1.render('click to restart', True, COLOR_RED)
finished = False
mode = None

# computer turn algorythm

def minimax(depth):

    if checkWinner() == 'x':
        return -1
    if checkWinner() == 'o':
        return 1
    else:
        if list(cells.values()).count('-') == 0:
            return 0

    if depth % 2 == 1:
        score = -1000000
        for x in range(9):
            if '-' in cells[x]:
                cells[x] = "o"
                score = max(score, minimax(depth+1))
                cells[x] = '-'
    else:
        score = 10000000
        for x in range(9):
            if '-' in cells[x]:
                cells[x] = "x"
                score = min(score, minimax(depth+1))
                cells[x] = '-'
    return score

# looking for a winner

def checkWinner():
    deck = list(cells.values())
    if set(deck[0:3]) == {'x'} or set(deck[3:6]) == {"x"} or set(deck[6:9]) == {"x"} or set(deck[0:7:3]) == {"x"} or set(deck[1:8:3]) == {"x"} or set(deck[2:9:3]) == {'x'}  or set(deck[::4]) == {"x"} or set(deck[2:7:2]) == {"x"}:
        return "x"
    if set(deck[0:3]) == {"o"} or set(deck[3:6]) == {"o"} or set(deck[6:9]) == {"o"} or set(deck[0:7:3]) == {"o"} or set(deck[1:8:3]) == {"o"} or set(deck[2:9:3]) == {"o"}  or set(deck[::4]) == {"o"} or set(deck[2:7:2]) == {"o"}:
        return "o"
    return None

# getting computer turn

def getStep():
    if "-" in cells.values():
        score = -100000
        pos = None
        for x in range(9):
            if '-' in cells[x]:
                cells[x] = "o"
                if minimax(0) > score:
                    score = minimax(0)
                    pos = x
                cells[x] = '-'
        cells[pos] = 'o'
        screen.blit(textO, (pos % 3 * 200 + 70, pos // 3 * 200 + 30))

while True:
    # start menu
    if mode == None:
        textStart = font1.render('play with bot?   y/n', True, COLOR_WHITE)
        screen.fill(COLOR_BLACK)
        screen.blit(textStart, (200, 200))
        pygame.display.update()
    # drawing a field
    if not finished and mode:
        textStart = font1.render("play with bot?   y/n", COLOR_BLACK, True)
        screen.blit(textStart, (200, 200))
        for x in range(1, 3):
            pygame.draw.line(screen, COLOR_WHITE, (x * 200, 0), (x * 200, 600), 5)
            pygame.draw.line(screen, COLOR_WHITE, (0, x * 200), (600, x * 200), 5)
        pygame.display.update()
    # end menu
    elif mode:
        if checkWinner() == 'x':
            screen.blit(text_win, (270, 350))
        elif checkWinner():
            screen.blit(text_loose, (270, 350))
        else:
            screen.blit(text_draw, (275, 350))
        screen.blit(text_restart, (225, 400))
        pygame.display.update()
    # processing turns
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                mode = "bot"
            if event.key == pygame.K_n:
                mode = "player"
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordX, coordY = pygame.mouse.get_pos()
            if cells[(coordX // 200) + ((coordY // 200) * 3)] == '-':
                if mode == 'player':
                    if list(cells.values()).count('-') % 2 == 1:
                        cells[(coordX // 200) + ((coordY // 200) * 3)] = "x"
                        screen.blit(textX, (coordX // 200 * 200 + 80, coordY // 200 * 200 + 30))
                    else:
                        cells[(coordX // 200) + ((coordY // 200) * 3)] = "o"
                        screen.blit(textO, (coordX // 200 * 200 + 80, coordY // 200 * 200 + 30))
                if mode == 'bot':
                    cells[(coordX // 200) + ((coordY // 200) * 3)] = "x"
                    screen.blit(textX, (coordX//200*200+80, coordY//200*200+30))
                print(checkWinner())
                if mode == 'bot':
                    getStep()

            if finished == True:
                cells = {x: '-' for x in range(9)}
                pygame.display.update()
                finished = False
                mode = None

            if checkWinner() or "-" not in cells.values():
                finished = True