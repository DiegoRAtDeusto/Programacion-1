#
#	ejerciciosprogramación1.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 14/09/22
#	Copyright � 2022 Deusto. All Rights reserved
#

import math

###########################################################
#   Dibujo
#
#   Dibuja tu nombre con asteriscos:
###########################################################
def Dibujo():
    print('******    ***   *******    ********    *******\n'
          '*     *    *    *          *           *     *\n'
          '*     *    *    *******    *   ****    *     *\n'
          '*     *    *    *          *           *     *\n'
          '******    ***   *******    ********    *******')

###########################################################
#   Hola, nombre
#
#   Define una variable con un nombre y saluda a
#   ese nombre
###########################################################
def holanombre():
    name = 'Ana'
    print(f'¡Hola, {name}!')

###########################################################
#   Millas a Km
#
#   Define una variable con una distancia millas y
#   devuelve esa distancia en km
###########################################################
def MillasaKM():
    distance = 20;
    print(f'{distance} millas son {distance * 1.609:.2f} km')

###########################################################
#   De años a minutos
#
#   Define una variable para indicar tu edad y
#   calcula el número de minutos que viviste
###########################################################
def Minutos():
    years = 20;
    print(f'Si tienes {years} años, viviste al menos {int(years * 365.25 * 24 * 60)} minutos')

###########################################################
#   Litros de agua
#
#   Define el ancho, largo y profundidad de una
#   piscina y calcula la cantidad de litros de agua
#   que contiene
###########################################################
def Piscina():
    height = 20
    length = 10
    depth = 2
    print(f'Una piscina de {height} m de largo, {length} m de ancho y {depth} m de profundidad contiene {height * length * depth * 1000} litros de agua.')

###########################################################
#   Farenheit a Celsius
#
#   Define una temperatura en grados Farenheit y
#   devuelve su equivalente en Celsius
###########################################################
def Farenheit():
    celsius = 22.222
    print(f'{celsius * 1.8 + 32} grados Farenheit son {celsius} grados Celsius')

###########################################################
#   Pintar una pared
#
#   Define la altura y anchura de una pared
###########################################################
def Pintura():
    height  = 3
    width = 10
    windows = 2
    doors = 1
    print(f'Una pared de {height} m de alto y {width} m de ancho con {windows} ventanas y {doors} puerta '
          f'necesita {(height*width-windows-(doors*1.6))/10} litros de pintura.')

###########################################################
#   Segundos a horas
#
#   Define un número de segundos y devuelve su
#   equivalencia en horas, minutos y segundos
###########################################################
def Seconds():
    seconds = 8000
    print(f'{seconds} segundos son {(int)(seconds / 3600)} horas, {seconds % 60} minutos y {seconds % 3600} segundos.')

###########################################################
#   Cambio
#
#   Define el coste de una compra y el dinero que se ha pagado para devolver los
#   cambios en monedas de 2 €, 1 €, 50 c., 20 c., 10 c., 5 c. y 1c.:
###########################################################
def Cambio():
    cost = 1878
    paid = 2000
    returned = paid - cost
    coin_types = [200, 100, 50, 20, 10, 5, 2, 1]

    print(f'Coste: {cost / 100}')
    print(f'Pagado: {paid / 100}')
    print(f'Devolver: {returned / 100}')

    #For each coin type, calculate how many can we return to the "costumer"
    for x in coin_types:
        print(f'{((int)(returned / x))} monedas de {x / 100} €')
        returned -= (int)(returned / x) * x

###########################################################
#   Salto de longitud
#
#   Define la velocidad inicial y el ángulo de salto
#   de una persona y la gravedad para devolver la
#   longitud que recorrería en ese planeta
###########################################################
def SaltoDeLongitud():
    angle = 45
    speed = 4
    gravity = 1.633
    print(f'Una persona que salte con un ángulo de {angle}º a {speed} m/s en un planeta con g = {gravity}'
          f' m/s2 recorrería {(pow(speed, 2) * math.sin(2* math.radians(angle))) / gravity} m.')

###########################################################
#   Herón de Alejandría
#
#   Define la longitud de los lados a, b y c de un
#   triángulo y calcula su área usando la fórmula de
#   Herón
###########################################################
def Heron():
    a = 11
    b = 13
    c = 17
    s = (a+b+c)/2

    print(f'Un triángulo con lados de {a}, {b} y {c} m tiene {math.sqrt(s*(s-a)*(s-b)*(s-c))} m2.')

###########################################################
#   Ecuación de segundo grado
#
#   Define a, b y c en una ecuación de segundo
#   grado y calcula sus raíces
###########################################################
def SegundoGrado():
    a = 1
    b = -5
    c = 6
    temp = math.sqrt(math.pow(b, 2) - 4 * a * c)
    print(f'Raices de {a} x2 + {b} x + {c} = 0:')

    if temp >= 0:
        print(f'x = {(-b + temp) / (2 * a)}')
        print(f'x = {(-b - temp) / (2 * a)}')

###########################################################
#   Caída libre
#
#   Muestra qué velocidad y cuál sería el espacio recorrido de un
#   cuerpo en caída libre durante los 10 primeros segundos.
###########################################################
def CaidaLibre():
    for i in range(0, 11):
        print(f't = {i:.2f}, v = {9.8 * i:.2f} m/s, {4.9 * math.pow(i, 2):.2f} m recorridos.')