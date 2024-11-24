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
    return [[O, X, O],
            [EMPTY, X, EMPTY],
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
    
    jugador = player(board)
    frontier = [] #inicializo un frontier, quiero agregar acá el camino que hace el algoritmo para luego obtener utilidad
    bestAction = "no devuelve nada minimax"
    if jugador == X :
        utilidadInicial = -100
    else:
        utilidadInicial = +100
        
        for accion in actions(board):
            newBoard = result(board,accion)
            if terminal(newBoard): #hay ganador o empate, me quedo con el de mas valor
                utilidadAccion = utility(newBoard)
            
            else: #si no, necesito ir a buscar el valor esperado del nodo
                for accionNew in actions(newBoard):
                    utilidadAccion = blablabla #guardo valor esperado del nodo
                
            if utilidadAccion > utilidadInicial: #Si la utilidad de este juego es la mejor, la guardo.
                utilidadInicial = utilidadAccion
                bestAction = accion
    
    return bestAction #devuelvo al mejor opcion
             


def utilidadFrontier(boardIncial):
    accionBest = "no hay mejor accion"
    jugador = player(boardIncial)
    
    if jugador == X :
        bestUtilidad = -100
    else:
        bestUtilidad = +100
    
    if terminal(boardIncial):
        return(utility(boardIncial))
    
    for action in boardIncial:
        newBoard = result(boardIncial,action)
        if terminal(newBoard):
            utilidadNewBoard = utility(newBoard)
            if jugador == X:
                if bestUtilidad < utilidadNewBoard:
                    accionBest = action
                    bestUtilidad = utilidadNewBoard
            if jugador == O:
                if bestUtilidad > utilidadNewBoard:
                    accionBest = action
                    bestUtilidad = utilidadNewBoard
        else: 
            boardIncial = newBoard
            utilidadNewBoard = utilidadFrontier(newBoard)
            if jugador == X:
                if bestUtilidad < utilidadNewBoard:
                    bestUtilidad = utilidadNewBoard
            if jugador == O:
                if bestUtilidad > utilidadNewBoard:
                    bestUtilidad = utilidadNewBoard
    print(accionBest)
    return utilidadNewBoard

ver = utilidadFrontier(initial_state())
print(ver)
