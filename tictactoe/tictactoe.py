"""
Tic Tac Toe Player
"""

import math
import copy 

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
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
    if o < x:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append((i,j))
    if action:
        return action
    else:
        return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    modBoard = copy.deepcopy(board)
    availActions = actions(modBoard)
    currentPlayer = player(modBoard)
    if not terminal(board):
        modBoard[action[0]][action[1]] = currentPlayer
    else:
        raise ValueError("Invalid Move")
    return modBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    results = winner(board)
    if results == None:
        return 0
    elif results == X:
        return 1
    else:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == "X":
        v = -2
        for action in actions(board):
            c = max(v,minValue(result(board,action)))
            if c == 1:
                return action
            if v != c:
                bestAction = action
                v = c
    else:
        v = 2
        for action in actions(board):
            c = min(v,maxValue(result(board,action)))
            if c == -1:
                return action
            if v != c:
                bestAction = action
                v = c
    return bestAction
        

def minValue(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v,maxValue(result(board,action)))
        if v == -1:
            return -1
    return v

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v,minValue(result(board,action)))
        if v == 1:
            return 1
    return v