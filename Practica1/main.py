import sys
from hotel import *


comando = sys.argv
if len(comando) > 1:
    if len(comando) > 2 or len(comando) == 2:
        if comando[1].lower() == "afegir" and comando[2].lower() == "habitacio":
            if comprobarLong(comando, 6):
                num = comando[3]
                capacidad = comando[4]
                precio = comando[5]
                afegirHabitacio(num, capacidad, precio)
        elif comando[1].lower() == "afegir" and comando[2].lower() == "reserva":
            if comprobarLong(comando, 8):
                num = comando[3]
                nom = comando[4]
                ap = comando[5]
                dni = comando[6]
                tel = comando[7]
                afegirReserva(num, nom, ap, dni, tel)
        elif comando[1].lower() == "finalitzar":
            if comprobarLong(comando, 4):
                num = comando[2]
                dias = comando[3]
                finalitzarHabitacio(num, dias)
        elif comando[1].lower() == "reserves":
            if comprobarLong(comando, 2):
                mostrarReservas()
        elif comando[1].lower() == "netejar":
            if comprobarLong(comando,3):
                num = comando[2]
                netejarHabitacio(num)
        elif comando[1].lower() == "info":
            if comprobarLong(comando, 3):
                dni = comando[2]
                info(dni)
        elif comando[1].lower() == "list":
            if comprobarLong(comando, 2):
                list()
    else:
        print("Comando Incorrecto. Prueba otra vez")
else:
    print("Comando Incorrecto. Prueba otra vez")
