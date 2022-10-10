#
#	Modular.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 30/09/22
#	Copyright � 2022 Deusto. All Rights reserved
#

def check_if_list_of_integers(op):
    return isinstance(op, list) and all(isinstance(i, int) for i in op)

###########################################################
#   Dos Y Cuatro
#
#   Programa una función que reciba una lista de enteros y
#   devuelva True si contiene un 2 o un 4, pero no ambos:
###########################################################
def DosYCuatro(numbers):
    if check_if_list_of_integers(numbers):
        result = False

        for i in [2, 4]:
            if i in numbers:
                result = not result

        return result
    else:
        raise ValueError("given argument is not a list of integer numbers")

###########################################################
#  Mayor Array
#
#   Programa una función que reciba dos listas de enteros del
#   del mismo tamaño y devuelva True si cada elemento de la 1a
#   lista es mayor que el correspondiente elemento en la 2a lista
###########################################################
def Mayor(op1, op2):
    if check_if_list_of_integers(op1) and check_if_list_of_integers(op2):
        length = min(len(op1), len(op2))

        for i in range(0, length - 1):
            if op1[i] < op2[i]:
                return False
        return True
    else:
        raise ValueError("given argument is not a list of integer numbers")

###########################################################
#  Terminar Igual
#
#   Programa una función que reciba dos listas de enteros y un entero n.
#   Devolverá True si la 1a lista termina igual que la 2a lista en los n
#   últimos elementos
###########################################################
def TerminarIgual(op1, op2, n):
    #if they are the incorrect type, throw an exception
    if check_if_list_of_integers(op1) and check_if_list_of_integers(op2) and isinstance(n, int):
        length = len(op1)

        #Check that they are the same length
        if length != len(op2):
            raise ValueError("Both lists are not of the same size")

        #check in all of the desired range that the numbers are the same
        for i in range(n, length - 1):
            if op1[i] != op2[i]:
                return False
        return True
    else:
        raise ValueError("Given argument is not a list of integer numbers")

###########################################################
#  DosJuntoADos
#
#   Programa una función que reciba una lista de enteros y
#   devuelva True si hay un 2 junto a otro 2, o false en caso
#   contrario
###########################################################
def DosJuntoADos(op):
    assert check_if_list_of_integers(op)
    op.sort()

    if op.count(2) > 1:
        return True
    return False

###########################################################
#  Mayor Diferencia
#
#   Programa una función que reciba una lista de enteros y
#   devuelva la diferencia entre el número más alto y el
#   número más bajo
###########################################################
def mayorDiferencia(op):
    assert check_if_list_of_integers(op)
    return max(op) - min(op)

###########################################################
#   Rima
#
#   Programa una función que reciba dos strins y un entero
#   y diga si riman, es decir, si son iguales los n últimos
#   caracteres
###########################################################
def Rima(str1, str2, n):
    assert isinstance(str1, str) and isinstance(str2, str) and isinstance(n, int)

    if n > len(str1) or n > len(str2):
        raise ValueError("N is larger than the length of the strings")

    # check in all of the desired range that the numbers are the same
    for i in range(-1, -n - 1, -1):
        if str1[i] != str2[i]:
            return False
    return True

#Call executing function
if __name__ == '__main__': print(Rima("carcasa", "pisa", 3))