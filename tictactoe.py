"""
Tic Tac Toe Player
"""

import copy
import math

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
    cant_X = 0
    cant_O = 0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                cant_X = cant_X + 1
            if board[i][j] == O:
                cant_O = cant_O + 1
    return X if cant_X == cant_O else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    posibleAction = set()
    
    return {(i,j) for i in range(len(board)) for j in range(len(board)) if board[i][j] is EMPTY}
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move: Position already taken.")
    resultBoard = copy.deepcopy(board)
    jugador = player(resultBoard)
    resultBoard[action[0]][action[1]] = jugador
    return resultBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range (len(board)):
            
            if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] is not EMPTY:
                return board[i][0]
            if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] is not EMPTY:
                return board[0][j]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] is not EMPTY:
        return board[1][1]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_completo = True
    if winner(board) is not None:
        return True
    
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] is EMPTY:
                    is_completo = False
    return is_completo
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None 
    
    jugador = player(board)
    acciones = actions(board)
    utilidad_X_base = -100
    utilidad_O_base = 100
    mejorMovimiento = None
    
    if jugador == X:
        for accion in acciones:
            boardAccionado = result(board,accion)
            if terminal(boardAccionado):
                utilidadAccionado = utility(boardAccionado)
                if utilidadAccionado > utilidad_X_base:
                    utilidad_X_base = utilidadAccionado
                    mejorMovimiento = accion
            else:
                reaccionOtroPlayer = minimax(boardAccionado)
                boardReaccionado = result(boardAccionado,reaccionOtroPlayer)
                utilidadReaccionado = utility(boardReaccionado)
                if utilidadReaccionado > utilidad_X_base:
                    utilidad_X_base = utilidadReaccionado
                    mejorMovimiento = accion
                    
    if jugador == O:
        for accion in acciones:
            boardAccionado = result(board,accion)
            if terminal(boardAccionado):
                utilidadAccionado = utility(boardAccionado)
                if utilidadAccionado < utilidad_O_base:
                    utilidad_O_base = utilidadAccionado
                    mejorMovimiento = accion
                    
            else:
                reaccionOtroPlayer = minimax(boardAccionado)
                boardReaccionado = result(boardAccionado,reaccionOtroPlayer)
                utilidadReaccionado = utility(boardReaccionado)
                if utilidadReaccionado < utilidad_O_base:
                    utilidad_O_base = utilidadReaccionado
                    mejorMovimiento = accion
                    
    return mejorMovimiento


