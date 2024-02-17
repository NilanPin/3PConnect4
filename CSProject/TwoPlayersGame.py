# Libaries Needed
import numpy as np
import pygame
import math
import sys
import random
# RGB Values
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
Highlight = (218,165,32)
# Row and Column Variables
ROWS = 8
COLUMNS = 9
# Freespace variable for is full
freespace = 0
# Player pieces Variable (To be outputted in the shell's board)
Player1 = 1
Player2 = 2
AI = 3
# Screen Size for our game
Screensize = 100
# Makes  our pygame window size
width = COLUMNS * Screensize
height = (ROWS + 1) * Screensize
size = (width, height)
# defines our counter size
Counter_Size = int(Screensize / 2 - 5)
# Turn variable to decide who go first
turn = random.randint(0, 2)

# Inialises the board with 0's
def intialise_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

# Creates the board and counters
def createboard(board):
    # Creates the connect 4 board makes it look orginal
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c * Screensize, r * Screensize + Screensize, Screensize, Screensize))
            pygame.draw.circle(screen, BLACK, (
                int(c * Screensize + Screensize / 2), int(r * Screensize + Screensize + Screensize / 2)), Counter_Size)
    # Creates Red,Yellow,Green and Gold counters
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

def printboard(board):
    print(np.flip(board, 0))


# Drops a piece in the board shell so the one in pygame can be updated
def droppiece(board, row, col, piece):
    board[row][col] = piece

def isvalid(board, col):
    return board[ROWS - 1][col] == 0


def nextrow(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def winningpos(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                piece = 4
                board[r][c] = piece
                board[r][c+1] = piece
                board[r][c+2] = piece
                board[r][c+3] = piece
                return True

    # Check vertical locations for win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                piece = 4
                board[r][c] = piece
                board[r + 1][c] = piece
                board[r + 2][c] = piece
                board[r + 3][c] = piece
                return True

    # Check positively sloped diagonal
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                piece = 4
                board[r][c] = piece
                board[r + 1][c + 1] = piece
                board[r + 2][c + 2] = piece
                board[r + 3][c + 3] = piece
                return True

    # Check negatively sloped diagonal
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                piece = 4
                board[r][c] = piece
                board[r - 1][c + 1] = piece
                board[r - 2][c + 2] = piece
                board[r - 3][c + 3] = piece
                return True


def isfull(board, freespace):
    for x in range(0, (COLUMNS)):
        if board[ROWS - 1][x] == 0:
            freespace = freespace + 1
    if freespace == 0:
        return True


def setscores(window, piece):
    score = 0
    playagainst = random.randint(1, 2)
    opp_piece = playagainst
    if piece == Player1 or piece == Player2:
        opp_piece = AI

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score


def boardscores(board, piece):
    score = 0

    # Score center column
    center = [int(i) for i in list(board[:, COLUMNS // 2])]
    count = center.count(piece)
    score += count * 3

    # Score Horizontal
    for r in range(ROWS):
        rowarray = [int(i) for i in list(board[r, :])]
        for c in range(COLUMNS - 3):
            window = rowarray[c:c + 4]
            score += setscores(window, piece)

    # Score Vertical
    for c in range(COLUMNS):
        colarray = [int(i) for i in list(board[:, c])]
        for r in range(ROWS - 3):
            window = colarray[r:r + 4]
            score += setscores(window, piece)

    # Score positive sloped diagonal
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += setscores(window, piece)
    # Score Negative sloped diagonals
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            window = [board[r + 3 - i][c + i] for i in range(4)]
            score += setscores(window, piece)

    return score


# Works out if any given state resulted in a win for any of the players/AI or if its full
def endnode(board):
    return winningpos(board, Player1) or winningpos(board, Player2) or winningpos(board, AI) or \
           isfull(board,freespace) == True



def AvailablePos(board):
    Available = []
    for col in range(COLUMNS):
        if isvalid(board, col):
            Available.append(col)
    return Available


def minimax(board, depth, alpha, beta, maximizingPlayer):
    validmoves = AvailablePos(board)
    terminal = endnode(board)
    if depth == 0 or terminal:
        if terminal:
            if winningpos(board, AI):
                return (None, 1000)
            elif winningpos(board, Player1) or winningpos(board, Player2):
                return (None,-1000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, boardscores(board, AI))
    if maximizingPlayer:
        value = -math.inf
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, AI)
            newvalue = minimax(new_board, depth - 1, alpha, beta, False)[1]
            if newvalue > value:
                value = newvalue
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        playagainst = random.randint(1, 2)
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, playagainst)
            newvalue = minimax(new_board, depth - 1, alpha, beta, True)[1]
            if newvalue < value:
                value = newvalue
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


board = intialise_board()
printboard(board)
game_over = False

pygame.init()

screen = pygame.display.set_mode(size)
createboard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(Screensize / 2)), Counter_Size)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(Screensize / 2)), Counter_Size)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))

            # Ask for Player 1 Input
            if turn == 0 and not game_over:
                posx = event.pos[0]
                col = int(math.floor(posx / Screensize))

                if isvalid(board, col):
                    row = nextrow(board, col)
                    droppiece(board, row, col, 1)

                    if winningpos(board, 1):
                        label = myfont.render("  Player 1 wins!!   ", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        if isfull(board, freespace) == True:
                            label = myfont.render("   IT IS A DRAW  ", 1, BLUE)
                            game_over = True
                        else:
                            turn = 1
                    printboard(board)
                    createboard(board)

            # # Ask for Player 2 Input
            elif turn == 1 and not game_over:

                posx = event.pos[0]
                col = int(math.floor(posx / Screensize))

                if isvalid(board, col):
                    row = nextrow(board, col)
                    droppiece(board, row, col, 2)

                    if winningpos(board, 2):
                        label = myfont.render("  Player 2 wins!!   ", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        if isfull(board, freespace) == True:
                            label = myfont.render("     IT IS A DRAW!!!     ", 1, BLUE)
                            game_over = True
                        else:
                            turn = 2
                    printboard(board)
                    createboard(board)

    if turn == 2 and not game_over:
        col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)

        if isvalid(board, col):
            row = nextrow(board, col)
            timedelay = random.randint(100,1000)
            pygame.time.wait(timedelay)
            droppiece(board, row, col, 3)

            if winningpos(board, 3):
                label = myfont.render("     AI wins!!       ", 1, GREEN)
                screen.blit(label, (40, 10))
                game_over = True
            else:
                if isfull(board, freespace) == True:
                    label = myfont.render("     IT IS A DRAW!!!     ", 1, BLUE)
                    game_over = True
                else:
                    turn = 0
            printboard(board)
            createboard(board)

    if not game_over:
        continue
    pygame.time.wait(10000)
