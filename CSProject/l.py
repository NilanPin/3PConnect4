# Libaries needed
import numpy as np
import pygame
import math
import sys
import random
#Declaring RGB values needed
BLUE = (0, 100, 255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
Highlight = (218,165,32)
# Row and Column variables
ROWS = 8
COLUMNS = 9
# freespace variable for isfull()
freespaces = 0
# define our screen size
Screensize = 100
# sets game over to false so the game can be played. It will turn to true once someone has won or if the board is full
game_over = False
# Randomly picks a player to start
turn = random.randint(0,2)
# define width and height of board
width = COLUMNS * Screensize
height = (ROWS + 1) * Screensize
size = (width, height)
# intialises the size of the counter
Counter_Size = int(Screensize/ 2 - 5 )

# Intialises the board with zeros (empty posistions)
def intialise_board():
    board = np.zeros((ROWS, COLUMNS))
    return board
board = intialise_board()

def createboard(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c * Screensize, r * Screensize + Screensize, Screensize,Screensize ))
            pygame.draw.circle(screen, BLACK, (
                int(c * Screensize + Screensize / 2), int(r * Screensize + Screensize + Screensize / 2)), Counter_Size)
    # Creates the counters which then can be dropped
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * Screensize + Screensize / 2), height - int(r * Screensize + Screensize / 2)), Counter_Size)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * Screensize + Screensize / 2), height - int(r * Screensize + Screensize / 2)), Counter_Size)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, GREEN, (
                    int(c * Screensize + Screensize / 2), height - int(r * Screensize + Screensize / 2)), Counter_Size)
            elif board[r][c] == 4:
                pygame.draw.circle(screen, Highlight, (
                    int(c * Screensize + Screensize / 2), height - int(r * Screensize + Screensize / 2)), Counter_Size)
    pygame.display.update()

screen = pygame.display.set_mode(size)

# Dropping the counter
def droppiece(board, row, col, piece):
    board[row][col] = piece

# gets the next row before a counter has been dropped
def nextrow(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

# Checks if the move is valid
def isvalid(board, col):
    if board[ROWS - 1][col] == 0:
        return True

# outptuts the board
def printboard(board):
    print(np.flip(board, 0))
printboard(board)

# Checks if the top row is full
def isfull(board):
    for x in range(0, COLUMNS):
        if board[ROWS - 1][x] == 0:
            return False
    return True


# checks for any wins
def winingpos(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                board[r][c] = 4
                board[r][c+1] = 4
                board[r][c+2] = 4
                board[r][c+3] = 4
                return True

    # Check vertical locations for win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                board[r][c] = 4
                board[r + 1][c] = 4
                board[r + 2][c] = 4
                board[r + 3][c] = 4
                return True

    # Check positively sloped diagonal
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                board[r][c] = 4
                board[r + 1][c + 1] = 4
                board[r + 2][c + 2] = 4
                board[r + 3][c + 3] = 4
                return True

    # Check negatively sloped diaganol
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                board[r][c] = 4
                board[r - 1][c + 1] = 4
                board[r - 2][c + 2] = 4
                board[r - 3][c + 3] = 4
                return True


# initalize pygame
pygame.init()
# Calling function create board again
createboard(board)
from pygame import mixer
mixer.init()
music = pygame.mixer.music.load("countersdrop.mp3")

myfont = pygame.font.SysFont("monospace", 80)







# Allows the game to be played until game_over is true
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Allows the correct coloured counter to be dropped according to the turn order
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(Screensize/ 2)), Counter_Size)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(Screensize / 2)), Counter_Size)
            elif turn == 2:
                pygame.draw.circle(screen, GREEN, (posx, int(Screensize / 2)), Counter_Size)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / Screensize))

                if isvalid(board, col):
                    row = nextrow(board, col)
                    droppiece(board, row, col, 1)
                    # Plays counter drop sound
                    pygame.mixer.music.play(1)

                    if winingpos(board, 1):
                        pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
                        label = myfont.render(  "Player 1 Wins!!!"  , True, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        if isfull(board) == True:
                            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
                            label = myfont.render("   IT IS A DRAW   ",True, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True
                        else:
                            turn = 1


            # Ask for Player 2 Input
            elif turn == 1:
                posx = event.pos[0]
                col = int(math.floor(posx / Screensize))

                if isvalid(board, col):
                    row = nextrow(board, col)
                    droppiece(board, row, col, 2)
                    pygame.mixer.music.play(1)

                    if winingpos(board, 2):
                        pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
                        label = myfont.render( "Player 2 Wins!!!",True, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        if isfull(board) == True:
                            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
                            label = myfont.render("   IT IS A DRAW   ", True, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True
                        else:
                            turn = 2

            # Ask for player 3 output
            elif turn == 2:
                posx = event.pos[0]
                col = int(math.floor(posx / Screensize))

                if isvalid(board, col):
                    row = nextrow(board, col)
                    droppiece(board, row, col, 3)
                    pygame.mixer.music.play(1)

                    if winingpos(board, 3):
                        pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
                        label = myfont.render("Player 3 Wins!!!", True, GREEN)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        if isfull(board) == True:
                            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
                            label = myfont.render("   IT IS A DRAW   ", True, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True
                        else:
                            turn = 0

            printboard(board)
            createboard(board)

            if not game_over:
                continue
            pygame.time.wait(10000)










