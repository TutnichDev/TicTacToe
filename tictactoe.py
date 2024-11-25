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
    if terminal(board): return None
    accionesPosibles = actions(board)
    jugador = player(board)
    
    if jugador == X:
        utilidad = -10000
    else:
        utilidad = 10000
    iter = 0
    for accioni in accionesPosibles: # recorro las acciones posibles
        iter = iter+1
        boardAccionado = result(board,accioni) # tablero modificado por acción
        beneficio = benefit(boardAccionado) # beneficio de la acción i
        print(f'soy la iteracion ${iter}')
        print(accioni)
        print(beneficio)
        if jugador == X:
            if beneficio>utilidad:
                utilidad = beneficio
                mejorMovimiento = accioni # Para X, si el beneficio de la acción es la más alta, se guarda la accion en mejor movimiento
        else: 
            if beneficio<utilidad:
                utilidad = beneficio
                mejorMovimiento = accioni # Para O, si el beneficio de la acción es la más baja, se guarda la accion en mejor movimiento
    
    return mejorMovimiento 

def benefit(boardIncial):
    
    accionesPosibles = actions(boardIncial)
    
    if terminal(boardIncial): return utility(boardIncial)
    
    jugador = player(boardIncial)
    if jugador == X:
        utilidad = -1000
    else:
        utilidad = 1000
    
    if jugador == X:
        for accioni in accionesPosibles:
            boardMovido = result(boardIncial,accioni)
            if terminal(boardMovido):
                valorBoardMOvido = utility(boardMovido)
                if valorBoardMOvido > utilidad:
                    utilidad = valorBoardMOvido
                    mejorBeneficio = valorBoardMOvido
            else:
                valorBoardMOvido = benefit(boardMovido)
                if  valorBoardMOvido > utilidad:
                    utilidad = valorBoardMOvido
                    mejorBeneficio = valorBoardMOvido
        
    else: # si es el player == O
        for accioni in accionesPosibles:
            boardMovido = result(boardIncial,accioni)
            if terminal(boardMovido):
                valorBoardMOvido = utility(boardMovido)
                if valorBoardMOvido < utilidad:
                    utilidad = valorBoardMOvido
                    mejorBeneficio = valorBoardMOvido
            else:
                valorBoardMOvido = benefit(boardMovido)
                if  valorBoardMOvido < utilidad:
                    utilidad = valorBoardMOvido
                    mejorBeneficio = valorBoardMOvido
    return mejorBeneficio
