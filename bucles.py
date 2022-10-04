#
#	bucles.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 16/09/22
#	Copyright � 2022 Deusto. All Rights reserved
#

import math
import random

###########################################################
#   Museo
#
#   Pide la edad para calcular el precio de la entrada al museo:
###########################################################
def Museo():
    age = input("Edad: " )
    wednesday = input("¿Es miércoles? ")
    price = 0

    if wednesday:
        if age < 5:
            price = 0
        elif age < 18:
            price = 5
        elif age < 64:
            price = 10
        else:
            price = 7
    else:
        price = 0

###########################################################
#   Museo
#
#   Pide la edad para calcular el precio de la entrada al museo:
###########################################################
def IMC():
    weight = input('¿Peso? ')
    height = input('¿Altura? ')
    IMC = (float)(weight) / (float)(height)
    print(f'IMC: {IMC}')

    if IMC < 18.5:
        print('Bajo Peso')
    elif IMC <= 30:
        print('Peso normal')
    else:
        print('Sobrepeso')

###########################################################
#   Trivial
#
#   Programa un trivial con 3 preguntas y 3 alternativas:
###########################################################
def Trivial():
    questions = ["¿Cuál es la capital de España?",
                 "¿Cuál es la capital de Francia?",
                 "¿Cuál es la capital de Finlandia"]
    answers = ["1) Madrid", "2) Paris", "3) Helsinki"]
    i = 1

    for question in questions:
        print(question)
        for answer in answers:
            print(answer)

        lock = True

        while (lock):
            if i == (int)(input("¿Respuesta? ")):
                print("¡Correcto!")
                lock = False
                i += 1
            else:
                print("No, te has equivocado")

###########################################################
#   Calificaciones
#
#   Recibe un valor numérico de 0 a 10 y muestra
#   su calificación.
###########################################################
def Calificaciones():
    score = (float)(input("¿Nota? "))

    if score < 5:
        print("Suspenso")
    elif score < 6:
        print("Suficiente")
    elif score < 7:
        print("Bien")
    elif score < 8.5:
        print("Notable")
    else:
        print("Sobresaliente")

###########################################################
#   Zoltar
#
#   Pide el nombre de una persona y en función de la primera
#   letra, muestra un mensaje con su futuro(un mensaje para las iniciales A-H,
#   otro para I-Q y otro para R-Z)
###########################################################
def Zoltar():
    name = input("¿Como te llamas? ")

    if name[0] < 'H':
        print(name + ", te aseguro un futuro lleno de éxitos")
    elif name[0] < 'Q':
        print(name + ", te aseguro un futuro lleno de amores y lujurias")
    else:
        print(name + ", eres un inútil. No hay nada que se pueda hacer.")

###########################################################
#   Series
#
#   Muestra las siguientes series de números
###########################################################
def Series():
    for i in range(1, 11):
        print(i, end = ' ')

    print()

    for i in range(1, 1001):
        print(i, end = ' ')

    print()

    for i in range(20, 501, 10):
        print(i, end = ' ')

    print()

    for i in range(10, -1, -1):
        print(i, end = ' ')

    print()

###########################################################
#   Tabla de Multiplicar
#
#   Solicita un número y muestra su tabla de multiplicar
###########################################################
def TablaDeMultiplicar():
    number = (int)(input("Número? "))

    for i in range(1, 11):
        print(f'{number} x {i} = {number * i}')

###########################################################
#   Tablas de Multiplicar
#
#   Muestra todas las tablas de multiplicar del 1 al 10
###########################################################
def TablasDeMultiplicar():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i} x {j} = {j * i}')

###########################################################
#   Factorial
#
#   Recibe unu número por teclado y calcula su factorial
###########################################################
def Factorial():
    number = (int)(input("Dime un número: "))
    print(f'{number}! = {math.factorial(number)}')

###########################################################
#   Calculadora
#
#   Muestra un menú con operaciones aritmética básicas y
#   cuando se elija una opción, solicita los operandos y realiza
#   el cálculo.
###########################################################
def Calculadora():
    print('Opciones:\n1. Sumar\t\t3. Multiplicar\n2. Restar\t\t4. Dividir')
    option = (int)(input("Opción? "))
    leftop = (int)(input("Primer operandp? "))
    rightop = (int)(input("Segundo operando? "))

    if option == 1:
        print(f'{leftop} + {rightop} = {leftop + rightop}')
    elif option == 2:
        print(f'{leftop} - {rightop} = {leftop - rightop}')
    elif option == 3:
        print(f'{leftop} * {rightop} = {leftop * rightop}')
    elif option == 4:
        print(f'{leftop} / {rightop} = {leftop / rightop}')
    else:
        print("Código no válido")

###########################################################
#   Piedra-papel-tijera
#
#   Juega a piedra-papel-tijera contra el orderandor, al mejor
#   de 3 partidas
###########################################################
def PiedraPapelTijera():
    win_count = 0
    rounds = 0
    items = ['Piedra', 'Papel', 'Tijera']

    while(rounds < 3):
        print('Jugada?\n1. Piedra\n2. Papel\n3. Tijera')
        option = (int)(input('Opción? ')) - 1
        computer_choice = random.randint(0, 2)

        print(f'Tu elijes {items[option]} y yo {items[computer_choice]}, ', end='')

        if computer_choice == option:
            print('¡Empate!')
            continue
        if computer_choice == 0:
            if option == 1:
                print('tú ganas')
                win_count += 1
            else:
                print('tu pierdes')
        elif computer_choice == 1:
            if option == 2:
                print('tú ganas')
                win_count += 1
            else:
                print('tu pierdes')
        else:
            if option == 0:
                print('tú ganas')
                win_count += 1
            else:
                print('tu pierdes')
        rounds += 1

    endings = ['yo gano', 'tú ganas']
    print(f'Tu has ganado {win_count} veces y yo {3-win_count}, {endings[win_count >= 2]}')

###########################################################
#   Frase
#
#   Pide una frase por teclado y calcula el número de espacios
#   que contiene
###########################################################
def Frase():
    phrase = input("Frase: ")
    print(f'{phrase.count(" ")} espacios')

###########################################################
#   Vocales
#
#   Pide una frase en minúsculas por teclado y muestra la misma
#   frase, cambiando las vocales por *.
###########################################################
def Vocales():
    phrase = input("Frase: ")
    vowels = "AEIOUaeiou"

    for letter in vowels:
        phrase = phrase.replace(letter, '*')

    print(phrase)

###########################################################
#   Sumatorio
#
#   Pide un número por teclado y calcula el sumatorio desde 1
#   hasta ese número.
###########################################################
def Sumatorio():
    print((int)(math.fsum(range(1, (int)(input("¿Número? ")) + 1))))

###########################################################
#   Producto
#
#   Pide un número por teclado y calcula el producto desde 1
#   hasta ese número
###########################################################
def Producto():
    print((int)(math.prod(range(1, (int)(input("¿Número? ")) + 1))))

###########################################################
#   Poker
#
#   Muestra todas las cartas de una baraja de Poker
###########################################################
def Poker():
    decks = ['picas', 'oros', 'espadas', 'corazones']
    indexes = ['As', '2', '3', '4', '5', '6', '7', '8', '9', 'Sota', 'Reina', 'Rey']

    for deck in decks:
        for index in indexes:
            print(f'{index} de {deck}')

###########################################################
#   Serie de Madhava-Leibniz
#
#   Solicita un número de iteracciones para calcular PI por la
#   serie de Madhava-Leibniz
###########################################################
def Pi():
    number = (int)(input("¿N? "))
    result = 0

    for i in range(0, number + 1):
        result += ((-1)**i)/(2*i + 1)

    print(f'PI = {result * 4}')

###########################################################
#   FizzBuzz
#
#   La serie FizzBuzz
###########################################################
def Fizzbuzz():
    modulus = [
        (3, "Fizz"),
        (5, "Buzz")
    ]

    for i in range(1, 101):
        result = ""
        for mod in modulus:
            if i % mod[0] == 0:
                result += mod[1]

        if result == "":
            print(i)
        else:
            print(result)

###########################################################
#   Reves
#
#   Recibe una frase por teclado y escríbela al revés
###########################################################
def Reves():
    print(input("Frase: ").__reversed__())

###########################################################
#   Ultima
#
#   Recibe una frase por teclado y muestra solo la última palabra
###########################################################
def Ultima():
    word_list = input("Frase: ").split(" ")
    print(word_list[len(word_list) - 1])

###########################################################
#   Primeros Pares
#
#   Recibe dos números, inicio y fin y muestra los 5 primeros
#   pares entre esos números
###########################################################
def PrimerosPares():
    start = (int)(input("inicio: "))
    end = (int)(input("fin: "))

    if (start % 2) == 1:
        start += 1

    if (end - start) > 11:
        end = start + 9

    for i in range(start, end, 2):
        print(i, end=' ')

###########################################################
#   Ultimos Múltiplos 5
#
#   Recibe dos números, inicio y fin y muestra los 3 últimos
#   múltiplos de 5 entre esos números
###########################################################
def UltimosMultiplos():
    start = (int)(input("inicio: "))
    end = (int)(input("fin: "))
    reminder = end % 5

    if reminder != 0:
        end -= reminder

    reminder = start % 5

    if (end - start) > 10:
        start = end - 10
    elif reminder != 0:
        start -= reminder

    for i in range(start, end + 1, 5):
        print(i, end=' ')

###########################################################
#   Factoriales
#
#   Recibe dos números, inicio y fin y muestra los factoriales
#   de los números comprendidos entre inicio y fin.
###########################################################
def Factoriales():
    start = (int)(input("inicio: "))
    end = (int)(input("fin: "))

    for i in range(start, end + 1):
        print(math.factorial(i))

###########################################################
#   Factoriales
#
#   Define una distancia aleatoria entre 5 y 100m para el
#   cerdito y solicita la velocidad en m/s y el ángulo en
#   en grados al jugador. Si el pájaro pasa al menos de 1 m
#   del cerdito, punto para el jugador. Si no pierde un pájaro
#   (tiene 3 inicialmente)
###########################################################
def AngryBirds():
    length = random.randint(5, 100)
    tries = 3
    print(f'El cerdito está a {length} m')

    while tries > 0:
        speed = (int)(input("¿Velocidad? "))
        angle = (int)(input("¿Angulo? "))
        distance = ((speed ** 2) * math.sin(2 * math.radians(angle))) / 9.8145

        if math.fabs(length - distance) < 1:
            print(f'¡Has avanzado {distance:.2f} y has dado al cerdito!\nGanas 1 punto y vuelves a tener 3 pájaros')
            tries = 3
            length = random.randint(5, 100)
            print(f'El cerdito está a {length} m')
        else:
            tries -= 1
            print(f'Has avanzado {distance:.2f}, te has quedado a {length - distance:.2f}\nTe quedan {tries} pájaros')

###########################################################
#   Estadística
#
#   Recibe 1o alturas en cm por teclado y calcula la media,
#   la deviación típica, el máximo y el mínimo
###########################################################
def Estadistica():
    heights = []

    for i in range(1, 11):
        heights.append((int)(input(f'¿Altura {i}? ')))

    count = len(heights)
    mean = math.fsum(heights) / count
    tipical_desviation = 0

    for height in heights:
        tipical_desviation += (height - mean) ** 2

    tipical_desviation = math.sqrt(tipical_desviation / count)

    print(f'Altura Media: {mean}\nDesv. Típica: {tipical_desviation:.2f}\nAltura mínima: {min(heights)}\nAltura máxima: {max(heights)}')

###########################################################
#   Penalty
#
#   Tanda de penalties (al mejor de 5, si no hay empates) contra
#   el ordenador.
###########################################################
def Penalty():
    points = [0, 0]
    dialogs = ["tirar", "¡Has marcado gol!", "parar", "¡Te han marcado gol!"]
    turn = 0
    rounds_remaining = 5

    while(rounds_remaining > 0):
        for i in range(0, 2):
            option = (int)(input(f'Elige dónde {dialogs[i * 2]}:\n ___________\n|2    3    4|\n|1         5|\n ¿Opción? '))
            goalkeeper = random.randint(1, 5)
            if goalkeeper != option:
                points[turn] += 1
                print(f'{dialogs[i * 2 + 1]}\n {"Vas empatado " if points[0] == points[1] else "Vas ganando" if points[0] > points[1] else "Vas perdiendo"} {points[0]} - {points[1]}')
            else:
                print("El balón se ha parado")
            turn = 1 if turn == 0 else 0

        if rounds_remaining == 0 & points[0] == points[1]:
            rounds_remaining = 1

###########################################################
#   PIN
#
#    Solicita un PIN por teclado (4 dígitos) y muestra el saldo de la
#    cuenta corriente solo si el usuario lo acierta en 3 intentos o
#    menos. Si no, muestra un error.
###########################################################
def PIN():
    password = random.randint(1000, 9999)
    for i in range(0, 3):
        if password == (int)(input("Pin: ")):
            print("Saldo: 0$")
            return
        else:
            print("Pin Incorrecto")
    print("Tarjeta Bloqueada")

###########################################################
#   SMS
#
#    Solicita una frase y muestra las pulsaciones de teclado
#    numérico que hacen falta para escribirla
###########################################################
def SMS():
    phrase = input("Frase: ")

    for letter in phrase:
        if letter != ' ':
            reg = (ord(letter.capitalize()) - ord('A'))
            number = int(reg / 3 + 2)
            for i in range(0, reg % 3 + 1):
                print(number, end='')
            print(' ')

#Call executing function
if __name__ == '__main__': SMS()