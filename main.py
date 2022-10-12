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

def placeboat(board, x, y, horizontal, n, symbol):
    if horizontal:
        for i in range(0, n):
            if x + i > 9 or y > 9 or board[y * 10 + x + i] != " ":
                return False

        for i in range(0, n):
            board[y * 10 + x + i] = symbol
    else:
        for i in range(0, n):
            if x > 9 or y + i > 9 or board[(y + i) * 10 + x] != " ":
                return False

        for i in range(0, n):
            board[(y + i) * 10 + x] = symbol

    return True

def persistent_placement(board, n, symbol):
    while(not placeboat(board, random.randint(0, 9), random.randint(0, 9), random.randint(0, 1), n, symbol)):
        continue
def boardShipsCPU(board):
    persistent_placement(board, 5, "X")

    for i in range(0, 2):
        persistent_placement(board, 4, "X")

    for i in range(0, 3):
        persistent_placement(board, 3, "X")

    for i in range(0, 5):
        persistent_placement(board, 1, "X")

def boardShotsCPU(board):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        if board[y * 10 + x] != "C":
            board[y * 10 + x] = "C"
            break

def boardShipsHuman(board):
    print("Place 1 destructor: ")

    while(not placeboat(board, int(input("X? ")), int(input("Y?")), int(input("Horizontal?")), 5, "O")):
        print("El barco no está bien puesto")

    for i in range(0, 2):
        while (not placeboat(board, int(input("X? ")), int(input("Y?")), int(input("Horizontal?")), 4, "O")):
            print("El barco no está bien puesto")

    for i in range(0, 3):
        while (not placeboat(board, int(input("X? ")), int(input("Y?")), int(input("Horizontal?")), 3, "O")):
            print("El barco no está bien puesto")

    for i in range(0, 5):
        while (not placeboat(board, int(input("X? ")), int(input("Y?")), int(input("Horizontal?")), 1, "O")):
            print("El barco no está bien puesto")

def boardShotsHuman(board):
    x = int(input("X? "))
    y = int(input("Y? "))

    board[y * 10 + x] = "P"

def PrintBoardsBoat(board):
    for i in range(0, 10):
        for j in range(0, 10):
            print(f'[ {board[i * 3 + j]} ]', end = " ")
        print("")
def checkWinnerBoats(board):
    if not "X" in board:
        print("You Win!")
        return True

    if not "O" in board:
        print("I Win!")
        return True
    return False

def HundirlaFlota():
    board = [" "] * (10 * 10)

    func_list = [boardShotsCPU, boardShotsHuman]

    boardShipsCPU(board)
    PrintBoardsBoat(board)
    boardShipsHuman(board)

    while (not checkWinnerBoats(board)):
        PrintBoardsBoat(board)
        func_list[0](board)
        func_list.reverse()

def ToogleLight(board, x, y):
    if x < 8 and y < 8 or x < 0 and y < 0:
        board[y * 8 + x] = "*" if board[y * 8 + x] == " " else " "
def SwitchLights(board):
    user_input = input("Tu Turno. Introduce fila y columna: ")
    strings = user_input.split()
    inputs = []

    for i in strings:
        if i.isdigit():
            inputs.append(int(i))

    ToogleLight(board, inputs[0] - 1, inputs[1])
    ToogleLight(board, inputs[0], inputs[1] + 1)
    ToogleLight(board, inputs[0] + 1, inputs[1])
    ToogleLight(board, inputs[0], inputs[1] - 1)

def printLights(board):
    for i in range(0, 8):
        for j in range(0, 8):
            print(f'[ {board[i * 8 + j]} ]', end = " ")
        print("")
def SwitchOff():
    board = [" "] * (8 * 8)

    for i in range(0, 8 * 8):
        board[i] = "*" if random.randint(0, 1) == 1 else " "

    while "*" in board:
        printLights(board)
        SwitchLights(board)


#Call executing function
if __name__ == '__main__': SwitchOff()