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
freespaces = 0
# Player pieces Variable (To be outputted in the shell's board)
Player1 = 1
AIOne = 2
AITwo = 3
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
game_over = False

from pygame import mixer
mixer.init()
music = pygame.mixer.music.load("countersdrop.mp3")

# Intialises the board with zeros (empty posistions)
def intialise_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

# Creates the Board and makes it look orginal looking
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

# Dropping the counter
def droppiece(board, row, col, piece):
    board[row][col] = piece


# Checks if the move is valid
def isvalid(board, col):
    if board[ROWS - 1][col] == 0:
        return True

# gets the next row after a counter has been dropped
def nextrow(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r
# Checks if the top row is full
def isfull(board, freespace):
    for x in range(0,(COLUMNS)):
        if board[ROWS - 1][x] == 0:
            freespace = freespace + 1
    if freespace == 0:
        return True
# outptuts the board
def printboard(board):
    print(np.flip(board, 0))

# checks for any wins
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

    # Check negatively sloped diaganol
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

def setscores(window, piece):
    score = 0

    if window.count(piece) == 3 and window.count(0) == 1:
        score += 500
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 200

    if window.count(Player1) == 3 and window.count(0) == 1:
        score -= 400

    if window.count(AIOne) == 3 and window.count(0) == 1:
        score -= 400

    return score
# Function to get windows in order to pass it to setscores
def counter_window(board, piece):
    score = 0
    # Score center column
    center = [int(i) for i in list(board[:, COLUMNS // 2])]
    count = center.count(piece)
    score = count * 3

    # Score Horizontal
    for r in range(ROWS):
        rowarray = [int(i) for i in list(board[r, :])]
        for c in range(COLUMNS - 3):
            counters = rowarray[c:c + 4]
            score = setscores(counters, piece)

    # Score Vertical
    for c in range(COLUMNS):
        colarray = [int(i) for i in list(board[:, c])]
        for r in range(ROWS - 3):
            counters = colarray[r:r + 4]
            score = setscores(counters, piece)

    # Score positive sloped diagonal
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            counters = [board[r + i][c + i] for i in range(4)]
            score = setscores(counters, piece)
    # Score Negative sloped diagonals
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            counters = [board[r + 3 - i][c + i] for i in range(4)]
            score = setscores(counters, piece)

    return score


# Works out if any given state resulted in a win for any of the players/AI or if its full
def endnode(board):
    return winningpos(board, Player1) or winningpos(board, AIOne) or winningpos(board, AITwo) or \
           isfull(board,freespaces)

# Gets all available moves (used in minimax function)
def AvailablePos(board):
    Available = []
    for col in range(COLUMNS):
        if isvalid(board, col):
            Available.append(col)
    return Available

def minimaxone(board, depth, alpha, beta, playerturn):
    # Generates all valid moves stores them to array valid moves
    validmoves = AvailablePos(board)
    # will give terminal a boolean value based on the state of a board.
    terminal = endnode(board)
    # Checks if depth is 0 or terminal is True
    if depth == 0 or terminal:
        # Assigns heuristic values
        if terminal:
            if winningpos(board, AIOne):
                return (None, 1000)
            elif winningpos(board, Player1) or winningpos(board,AITwo):
                return (None,-1000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, counter_window(board, AI))

    # Player 1 Minimising tree creation
    if playerturn == 0:
        value = math.inf
        # Drops a counter in every valid location
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, 1)
            # Stops creation if player has won and makes sure depth is three
            #  further depths is unneeded and it ensures the player can win on their next turn not further turns
            if winningpos(new_board,1) and depth == 2:
                column = col
                value = -10000
                return column, value
            # Recursion
            newvalue = minimax(new_board, depth - 1, alpha, beta, 1)[1]
            if newvalue < value:
                value = newvalue
                column = col
                # Pruning redundant/unneeded states
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

    # Player 2 maximising tree creation
    elif playerturn == 1:
        value = -math.inf
        # Drops a counter in every valid locations
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, 2)
            # Stops creation if player has won and makes sure depth is two
            #  further depths is unneeded and it ensures the player can win on their next turn not further turns
            if winningpos(new_board,2) and depth == 4:
                column = col
                value = 10000
                return column, value
            # Recursion
            newvalue = minimax(new_board, depth - 1, alpha, beta, 2)[1]
            if newvalue < value:
                value = newvalue
                column = col
            # Pruning redundant/unneeded states
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

    # AI's minimising tree creation
    elif playerturn == 2:
        value = math.inf
        # Drops a counter in all valid locations
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, 3)
            # Stops creation if the AI can win on this turn
            if winningpos(new_board,AI) and depth == 3:
                column = col
                value = -10000
                return column, value
            # Recursion
            newvalue = minimax(new_board, depth - 1, alpha, beta, 0)[1]
            if newvalue > value:
                value = newvalue
                column = col
                # Pruning
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value


def minimaxtwo(board, depth, alpha, beta, playerturn):
    # Generates all valid moves stores them to array valid moves
    validmoves = AvailablePos(board)
    # will give terminal a boolean value based on the state of a board.
    terminal = endnode(board)
    # Checks if depth is 0 or terminal is True
    if depth == 0 or terminal:
        # Assigns heuristic values
        if terminal:
            if winningpos(board, AITwo):
                return (None, 1000)
            elif winningpos(board, Player1) or winningpos(board,AIOne):
                return (None,-1000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, counter_window(board, AI))

    # Player 1 Minimising tree creation
    if playerturn == 0:
        value = math.inf
        # Drops a counter in every valid location
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, 1)
            # Stops creation if player has won and makes sure depth is three
            #  further depths is unneeded and it ensures the player can win on their next turn not further turns
            if winningpos(new_board,1) and depth == 3:
                column = col
                value = -10000
                return column, value
            # Recursion
            newvalue = minimax(new_board, depth - 1, alpha, beta, 1)[1]
            if newvalue < value:
                value = newvalue
                column = col
                # Pruning redundant/unneeded states
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

    # Player 2 minimising tree creation
    elif playerturn == 1:
        value = math.inf
        # Drops a counter in every valid locations
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, 2)
            # Stops creation if player has won and makes sure depth is two
            #  further depths is unneeded and it ensures the player can win on their next turn not further turns
            if winningpos(new_board,2) and depth == 2:
                column = col
                value = -10000
                return column, value
            # Recursion
            newvalue = minimax(new_board, depth - 1, alpha, beta, 2)[1]
            if newvalue < value:
                value = newvalue
                column = col
            # Pruning redundant/unneeded states
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

    # AI's maximising tree creation
    elif playerturn == 2:
        value = -math.inf
        # Drops a counter in all valid locations
        for col in validmoves:
            row = nextrow(board, col)
            new_board = board.copy()
            droppiece(new_board, row, col, AI)
            # Stops creation if the AI can win on this turn
            if winningpos(new_board,AI) and depth == 4:
                column = col
                value = 10000
                return column, value
            # Recursion
            newvalue = minimax(new_board, depth - 1, alpha, beta, 0)[1]
            if newvalue > value:
                value = newvalue
                column = col
                # Pruning
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value



def AIMoveOne(board):
    # Gets all valid moves for the next turn
    validmoves = AvailablePos(board)
    # This checks if the AI can win on their next turn
    for col in validmoves:
        row = nextrow(board, col)
        new_board = board.copy()
        droppiece(new_board, row, col, AIOne)
        if winningpos(new_board,AIOne):
            # Returns the winning move
            column = col
            return column
    # Checks if Red can win on their next turn
    for col in validmoves:
        row = nextrow(board, col)
        new_board = board.copy()
        droppiece(new_board, row, col, AITwo)
        if winningpos(new_board,AITwo):
            # Returns column to block Red
            column = col
            return column
    # Checks if yellow can win
    for col in validmoves:
        row = nextrow(board, col)
        new_board = board.copy()
        droppiece(new_board, row, col, Player1)
        if winningpos(new_board,Player1):
            # Returns column to block yellow
            column = col
            return column

    # Drops a counter in all valid locations and finds the highest scoring state
    bestscore = 0
    bestcol = random.choice(validmoves)
    for col in validmoves:
        board_copy=board.copy()
        row = nextrow(board_copy,col)
        droppiece(board_copy,row,col,AIOne)
        score = counter_window(board_copy,AIOne)
        if score > bestscore:
            bestscore = score
            bestcol = col

    return bestcol

def AIMoveTwo(board):
    # Gets all valid moves for the next turn
    validmoves = AvailablePos(board)
    # This checks if the AI can win on their next turn
    for col in validmoves:
        row = nextrow(board, col)
        new_board = board.copy()
        droppiece(new_board, row, col, AITwo)
        if winningpos(new_board,AITwo):
            # Returns the winning move
            column = col
            return column
    # Checks if Red can win on their next turn
    for col in validmoves:
        row = nextrow(board, col)
        new_board = board.copy()
        droppiece(new_board, row, col, Player1)
        if winningpos(new_board,Player1):
            # Returns column to block Red
            column = col
            return column
    # Checks if yellow can win
    for col in validmoves:
        row = nextrow(board, col)
        new_board = board.copy()
        droppiece(new_board, row, col, AIOne)
        if winningpos(new_board,AIOne):
            # Returns column to block yellow
            column = col
            return column

    # Drops a counter in all valid locations and finds the highest scoring state
    bestscore = 0
    bestcol = random.choice(validmoves)
    for col in validmoves:
        board_copy=board.copy()
        row = nextrow(board_copy,col)
        droppiece(board_copy,row,col,AITwo)
        score = counter_window(board_copy,AITwo)
        if score > bestscore:
            bestscore = score
            bestcol = col

    return bestcol



board = intialise_board()
printboard(board)
# initalize pygame
pygame.init()
screen = pygame.display.set_mode(size)
# Calling function create board again
createboard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 80)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(Screensize / 2)), Counter_Size)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, WHITE, (0, 0, width, Screensize))

            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / Screensize))

                if isvalid(board, col):
                    row = nextrow(board, col)
                    droppiece(board, row, col, 1)
                    pygame.mixer.music.play(1)

                    if winningpos(board, 1):
                        label = myfont.render(   "Player 1 Wins!!!"  , 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        if isfull(board, freespaces) == True:
                            label = myfont.render(   "IT IS A DRAW"   , 1, BLUE)
                            screen.blit(label, (40, 10))
                            game_over = True
                        else:
                            turn = 1
                printboard(board)
                createboard(board)

    if turn == 1 and not game_over:
        col, minimax_score = minimaxone(board, 4, -math.inf, math.inf, 2)
        row = nextrow(board, col)
        pygame.time.wait(500)
        if isvalid(board, col):
            row = nextrow(board, col)
            droppiece(board, row, col, 2)
            pygame.mixer.music.play(1)

            if winningpos(board, 2):
                label = myfont.render("   AI One wins!!!   ", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True
            else:
                if isfull(board, freespaces) == True:
                    label = myfont.render("IT IS A DRAW!!!" , 1, BLUE)
                    screen.blit(label, (40, 10))
                    game_over = True
                else:
                    turn = 2
            printboard(board)
            createboard(board)

    if turn == 2 and not game_over:
        col, minimax_score = minimaxtwo(board, 4, -math.inf, math.inf, 3)
        row = nextrow(board, col)
        pygame.time.wait(500)
        droppiece(board, row, col, 3)
        pygame.mixer.music.play(1)

        if winningpos(board, 3):
            label = myfont.render(   "AI Two wins!!!"  , 1, GREEN)
            screen.blit(label, (40, 10))
            game_over = True
        else:
            if isfull(board, freespaces) == True:
                label = myfont.render("IT IS A DRAW!!!", 1, BLUE)
                screen.blit(label, (40, 10))
                Game_over = True
            else:
                turn = 0
        printboard(board)
        createboard(board)


    if not game_over:
        continue
    pygame.time.wait(9000)