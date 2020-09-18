"""
Tic Tac Toe Player
Works with minimax and alpha-beta pruning
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player = 0 
    for rows in board:
        for cell in rows:
            if cell is O:
                player-=1
            elif cell is X:
                player+=1
    if(player):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is None:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    sign = player(board)
    newBoard = deepcopy(board)
    if(board[action[0]][action[1]] is None):
        newBoard[action[0]][action[1]] = sign
        return newBoard
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if(all(cell == board[i][0] for cell in board[i])):
            return board[i][0]
        if(all(board[j][i] == board[0][i] for j in range(len(board)))):
            return board[0][i]
    if(all(board[j][j] == board[0][0] for j in range(len(board)))):
        return board[0][0]
    if(all(board[len(board)-1-j][j] == board[len(board)-1][0] for j in range(len(board)))):
        return board[len(board)-1][0]
    return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) is not None):
        return True

    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if(win == X):
        return 2
    elif(win == O):
        return -2
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    Action = ()
    if player(board) == X:
        maximum = -1
        for action in actions(board):
            value = Min(result(board,action))
            if(maximum < value):
                Action = action
                maximum = value
    else:
        minimum = 1
        for action in actions(board):
            value = Max(result(board, action))
            if(minimum > value):
                Action = action
                minimum = value
    return Action

def Max(board):
    if(terminal(board)):
        return utility(board)
    maximum = -1
    for action in actions(board):
        maximum = max(maximum,Min(result(board,action)))
    return maximum

def Min(board):
    if(terminal(board)):
        return utility(board)
    minimum = 1
    for action in actions(board):
        minimum = min(minimum, Max(result(board, action)))
    return minimum
