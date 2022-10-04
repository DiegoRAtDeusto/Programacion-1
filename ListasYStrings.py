#
#	ListasYStrings.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 26/09/22
#	Copyright � 2022 Deusto. All Rights reserved
#

import random
import string

def Consonantes():
    phrase = input("Frase: ")
    vowels = "AEIOUaeiou ."

    for letter in vowels:
        phrase = phrase.replace(letter, '')

    print(f'Consonantes: {len(phrase)}')

###########################################################
#   Siglas
#
#   Solicita una frase y muestra el acrónimo
#   (siglas) correspondiente:
###########################################################
def Siglas():
    phrase = input("Frase: ")
    last_idx = 0
    string = phrase[last_idx]

    while(last_idx >= 0):
        last_idx = phrase.find(' ', last_idx + 1)
        string += phrase[last_idx + 1]

    string = string[:-1]
    print(string.upper())

###########################################################
#   Busca
#
#   Genera 100 números aleatorios entre 1 y 1000
#   y guárdalos en una lista. Busca el número 37
#   dentro de él e indica en qué posición está (si no
#   está, indícalo):
###########################################################
def Busca():
    numbers = []

    for i in range(1, 1001):
        numbers.append(random.randint(1, 1000))

    try:
        idx = numbers.index(37)
        print(f'El número está en la posición {idx}')
    except ValueError:
        print("El número no está en la lista")

###########################################################
#   Menor
#
#   Genera 100 números aleatorios entre 1 y 1000
#   y guárdalos en una lista. Busca y muestra el
#   menor de todos ellos e indica en qué posición
#   está:
###########################################################
def Menor():
    numbers = []

    for i in range(1, 1001):
        numbers.append(random.randint(1, 1000))

    minimun = min(numbers)

    print(f'El menor número es {minimun} y está en la posición'
          f' {numbers.index(minimun)}')

###########################################################
#   Rango
#
#   Genera 100 números aleatorios entre 1 y 1000
#   y guárdalos en una lista. Calcula el rango de
#   amplitud que tienen los números de la
#   lista(mayor-menor):
###########################################################
def Rango():
    numbers = []

    for i in range(1, 1001):
        numbers.append(random.randint(1, 1000))

    minimun = min(numbers)
    maximun = max(numbers)
    print(f'{maximun - minimun} ({minimun} - {maximun}) ')

###########################################################
#   Generador de claves numéricas
#
#   Recibe una longitud por teclado y genera una
#   contraseña numérica de esa longitud.
###########################################################
def Claves():
    length = int(input("Longitud: "))
    print(f'Contraseña: {random.randint(10 ** (length - 1),10 ** length - 1)}')

###########################################################
#   Generador de claves alfanuméricas
#
#   Recibe una longitud por teclado y genera una
#   contraseña alfabética de esa longitud.
###########################################################
def ClavesB():
    length = int(input("Longitud: "))
    result = ""

    for i in range(0, length):
        result += (random.choice(string.ascii_letters))

    print(f'Contraseña: {result}')

###########################################################
#   Palíndromo
#
#   Recibe una palabra (o frase) y di si es un
#   palíndromo (capicúa)
###########################################################
def Palindromo():
    phrase = input("¿Palabra? ")
    length = len(phrase)

    for i in range(0, int(length / 2)):
        if phrase[i] != phrase[length - i - 1]:
            print(f'{phrase} NO es un palíndromo')
            return

    print(f'{phrase} es un palíndromo')

###########################################################
#   Diccionario
#
#   Recibe dos palabras y di cuál de ellas está
#   antes en un diccionario
###########################################################
def Diccionario():
    first_word = input("¿Primera palabra?")
    second_word = input("¿Segunda palabra?")
    minor_length = min(len(first_word), len(second_word))

    for i in range(0, minor_length):
        if  first_word[i] > second_word[i]:
            break;
        elif first_word[i] < second_word[i]:
            temp = first_word
            first_word = second_word
            second_word = first_word
            break;

    print(f'{second_word} está antes que {first_word} en un diccionario')

###########################################################
#   Array Ordenado
#
#   Crea una lista. Solicita un entero por teclado, y almacénalo en
#   la lista solo si es >= que el anterior número almacenado (para
#   el primer número, que sea >=0). Repite el anterior paso hasta
#   rellenar la lista con 10 enteros. Muestra el contenido de la lista.
###########################################################
def ArrayOrdenado():
    array = []
    for i in range(0, 10):
        array.append(int(input(f'Dime un número (>= {0 if len(array) == 0 else array[-1]}): ')))

    print("El contenido del array es:")

    for i in range(0, 9):
        print(i, end=', ')
    print(array[-1])

###########################################################
#   Burbuja
#
#   Crea una lista con 10 números enteros desordenada y ordénala
#   por el método de la burbuja
###########################################################
def Burbuja():
    array = []

    for i in range(0, 10):
        array.append(random.randint(0, 30))

    print("Lista inicial:", end=" ")

    for i in range(0, 9):
        print(array[i], end=", ")
    print(array[-1])

    swapped = False
    for n in range(9, 0, -1):
        for i in range(n):
            if array[i] > array[i + 1]:
                swapped = True
                array[i], array[i + 1] = array[i + 1], array[i]
        if not swapped:
            break

    print("Lista final:", end=" ")

    for i in range(0, 9):
        print(array[i], end=", ")
    print(array[-1])

###########################################################
#   Cifrado Cesar
#
#   Recibe una frase y un desplazamiento y cifra la
#   frase con el algoritmo del Cesar (desplazar n
#   posiciones cada letra)
###########################################################
def Cesar():
    phrase = input("¿Texto? ")
    offset = int(input("¿Desplazamiento? "))
    result = ""

    for i in range(len(phrase)):
        char = phrase[i]
        result += chr((ord(char) + 4))

    print(f"Cifrado: {result}")

###########################################################
#   Vigenere
###########################################################
def Vigenere():
    text = input("Texto? ")
    clave = input("Clave? ")
    result = ""
    for i in range(0,len(text)):
        desp = ord(clave[i % len(clave)])
        result += chr((ord(text[i]) + desp))
    print(result)

###########################################################
#   Euromillones
#
#   Muestra una posible jugada en el Euromillones
#   (5 números del 1 al 50 no repetidos y 2
#   números del 1 al 11 no repetidos)
###########################################################
def Euromillones():
    numbers = list(range(1, 51))
    stars = list(range(1, 12))
    combination_numbers = []
    combination_stars = []

    for i in range(0, 5):
        random_idx = random.randint(0, 49 - i)
        combination_numbers.append(numbers[random_idx])
        numbers.pop(random_idx)

    for i in range(0, 2):
        random_idx = random.randint(0, 10 - i)
        combination_stars.append(stars[random_idx])
        stars.pop(random_idx)

    print(f"Prueba suerte con esta combinación: {combination_numbers}, estrellas: {combination_stars}")

###########################################################
#   Reverse!
#
#   Juego en el que se empieza con un conjunto de números
#   del 1 al 9 desordenados y se solicita una posición hasta la
#   que revertir el orden del conjunto de números. El objetivo
#   es lograr ordenar todos los números.
###########################################################
def Reverse():
    numbers = list(range(1, 10))
    random.shuffle(numbers)

    while(not all(numbers[i] <= numbers[i+1] for i in range(len(numbers) - 1))):
        print(f"Números: {numbers}")
        position = int(input("¿Posición? "))

        for i in range(0, int(position/2)):
            numbers[i], numbers[position-i - 1] = numbers[position-i - 1], numbers[i]

###########################################################
#   7 y media
#
#   Define y narray con las 40 cartas de la baraja española
#   y permite jufar a las 7 y media
###########################################################

###########################################################
#   Mastermind
#
#   Juego en el que el ordenador inventa una combinación de 4 números del 1
#   al 6 y da 10 intentos para adivinarlo. Tras cada intento indicará cuántos
#   números son parte del secreto y cuántos están en su posición correcta:
###########################################################
def Mastermind():
    number = str(random.randint(1000, 9999))

    for i in range(1, 11):
        in_number = input(f'Intento {i}? ')
        pertaining_numbers = 0
        correct_numbers = 0

        if number == in_number:
            print(f'Correcto! La combinación secreta era {number}')
            break

        for i in in_number:
            pertaining_numbers += number.count(i)

        for i in range(0, len(number)):
            if number[i] == in_number[i]:
                correct_numbers += 1

        print(f'{pertaining_numbers} números pertenecen al secreto.')
        print(f'{correct_numbers} estám correctamente situados.')

#Call executing function
if __name__ == '__main__': Mastermind()