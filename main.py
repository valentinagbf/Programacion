import sys
from ficheros import *


comando = sys.argv
if len(comando) > 1:
    if len(comando) == 6:
        if comando[1].lower() == "afegir" and comando[2].lower() == "habitacio":
            num = comando[3]
            capacidad = comando[4]
            precio = comando[5]
            afegirHabitacio(num, capacidad, precio)
    if len(comando) == 8:
        if comando[1].lower() == "afegir" and comando[2].lower() == "reserva":
            num = comando[3]
            nom = comando[4]
            ap = comando[5]
            dni = comando[6]
            tel = comando[7]
            afegirReserva(num, nom, ap, dni, tel)
    if len(comando) == 5:
        if comando[1].lower() == "finalitzar" and comando[2].lower() == "habitacio":
            num = comando[3]
            dias = comando[4]
            finalitzarHabitacio(num, dias)
    if len(comando) == 2:
        if comando[1].lower() == "reserves":
            mostrarReservas()

