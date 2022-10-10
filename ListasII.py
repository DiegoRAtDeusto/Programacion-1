#
#	ListasII.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 30/09/22
#	Copyright � 2022 Deusto. All Rights reserved
#

import random

###########################################################
#   Divisibles
#
#   Prepara una lista de todos los números entre 1
#   y 100 que sean divisibles entre 2, 3 y 5 o 7.
###########################################################
def Divisibles():
    numbers = []

    for i in range(1, 101):
        if i % 2 or 3 or 5 or 7 == 0:
            numbers.append(i)

    print(numbers)

###########################################################
#   Sin repetir
#
#   Prepara una lista con 100 números aleatorios
#   de 1 a 50 y saca por pantalla otra lista que
#   contenga esos números pero sin repeticiones
############################################################
def SinRepetir():
    numbers = []
    without_repetition = []

    for i in range(0, 101):
        numbers.append(random.randint(0, 50))

    numbers.sort()
    i = 0

    while i < 100:
        num = numbers[i]
        without_repetition.append(num)
        i += 1

        while num == numbers[i] and i < 100: i += 1

    print(without_repetition)

###########################################################
#   Más Larga
#
#   Recibe un texto por teclado y muestra por
#   pantalla la palabra más larga de ese texto.
############################################################
def MasLarga():
    phrase = input("Texto: ")
    largerword = ""

    for word in phrase.split():
        if len(word) > len(largerword):
            largerword = word

    print(f'Palabra más larga: {largerword}')

###########################################################
#   Calificaciones
#
#   Prepara una lista con los nombres de tus
#   asignaturas para este curso y pide por teclado
#   las calificaciones de cada una. Finalmente,
#   muestra por pantalla la calificación media.
############################################################
def Calificaciones():
    keywords = ["Programación", "Álgebra", "Electrónica", "Cálculo", "Introducción a los Computadores"]
    califications = 0

    for key in keywords:
        califications += int(input(f'Introduce tu calificación de {key}: '))

    califications /= len(keywords)
    print(f'Calificación media: {califications}')

###########################################################
#   Segundo más barato
#
#   Prepara una lista con los precios de 10
#   productos y recorre la lista para encontrar el 2º
#   más barato.
############################################################
def SegundoMasBarato():
    prices = []

    for i in range(0, 10):
        prices.append(random.randrange(1, 150))

    prices.sort()
    print(f'Segundo más barato: {prices[1]}')

###########################################################
#   Sublista
#
#   Prepara dos listas de números de diferente
#   tamaño y muestra si una lista está dentro de
#   otra lista
############################################################
def Sublista():
    a = list(input("Lista a: "))
    b = list(input("Lista b: "))

    if all(a.index(b[i]) >= 0 for i in a):
        print("b es una sublista de a")
    else:
        print("b NO es una sublista de b")

###########################################################
#   More
#
#   Prepara una lista con todas las letras del
#   alfabeto y otra lista con sus equivalentes en
#   código Morse en el mismo orden. Recibe una
#   frase por teclado y muéstrala en código Morse.
############################################################
def Morse():
    dictionary = {
        'a' : ".-",
        'b': "-...-",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",
        'k': "-.--",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-",
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--..",
    }

    word = input("Frase: ")
    morse = ""

    for i in word:
        morse += dictionary[i]

    print(f"Morse: {morse}")

#Call executing function
if __name__ == '__main__': Morse()