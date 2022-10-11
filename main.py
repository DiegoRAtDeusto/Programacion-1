#
#	TresEnRaya.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 11/10/22
#	Copyright � 2022 Deusto. All Rights reserved
#
import random

def printBoard(board):
    for i in range(0, 3):
        for j in range(0, 3):
            print(f'[ {board[i * 3 + j]} ]', end = " ")
        print("")

def selectCellCPU(board):
    print("Mi turno:")
    i = random.randint(0, 8)

    while board[i] != ' ':
        i = random.randint(0, 8)

    board[i] = 'X'

def selectCellHuman(board):
    user_input = input("Tu Turno. Introduce fila y columna: ")
    strings = user_input.split()
    inputs = []

    for i in strings:
        if i.isdigit():
            inputs.append(int(i))

    board[inputs[0] * 3 + inputs[1]] = 'O'

def checkWinner(board):
    representations = ["O", "X"]

    for c in representations:
        for j in range(0, 3):
            if all(board[j * 3 + i] == c for i in range(0, 3)):
                return True

    for c in representations:
        for j in range(0, 3):
            if all(board[j + i * 3] == c for i in range(0, 3)):
                return True

    for c in representations:
        if (board[0] == c and board[4] == c and board[8] == c) or (board[7] == c and board[4] == c and board[2] == c):
                return True

    return False

def TresEnRaya():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']

    func_list = [selectCellCPU, selectCellHuman]

    while(not checkWinner(board)):
        func_list[0](board)
        printBoard(board)
        func_list.reverse()

def boardShipsCPU():

def boardShotsCPU():

def boardShipsHuman():

def boardShotsHuman():

def PrintBoardsHuman():

def checkWinnerBoats():

def HundirlaFlota():

#Call executing function
if __name__ == '__main__': TresEnRaya()