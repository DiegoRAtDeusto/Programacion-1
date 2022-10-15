#
#	TresEnRaya.py
#	Fundamentos de la programación
#
#	Created by Diego Revilla on the 13/10/22
#	Copyright � 2022 Deusto. All Rights reserved
#

class Libro:
    def __init__(self, titulo, autor, anyo, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.ISBN = isbn
        pass

    def __str__(self):
        return self.titulo

class Hora:
    def __init__(self, segundos, minutos, horas):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __str__(self):
        return "{} segundos, {} minutos, {} horas".format(segundos, minutos, horas)

    def siguiente(self):
        self.segundos += 1

        if segundos == 60:
            self.minutos += 1
            self.segundos = 0

        if minutos == 60:
            self.horas += 1
            self.minutos = 0

        if horas == 24:
            self.horas = 0

    def am(self):
        return self.horas < 12

class

#Call executing function
if __name__ == '__main__': Conway()