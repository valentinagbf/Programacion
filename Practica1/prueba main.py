import sys
from ficheros import *



com = [
    "main añadir habitacion -1 4 50",
    "main añadir habitacion 0 1 50",
    "main añadir habitacion 1 0 40",
    "main añadir habitacion aa 1 40",
    "main añadir habitacion 100 aa 50",
    "main añadir habitacion 100 1 -1",
    "main añadir",
    "main añadir habitacion",
    "main añadir reserva",
    "main añadir reserva -1 hornos jordi 123 123",
    "main añadir reserva 0 hornos jordi 123 123",
    "main añadir reserva 100 hornos jordi 123456789 123123123",
    "main añadir reserva 100 hornos jordi 12345678z 123",
    "main finalizar",
    "main finalizar 100 -1",
    "main limpiar",
    "main limpiar 100",
    "main finalizar 100 5",
    "main list",
    "main info 12345678Z",
    "main info asdf asdf",
    "main reservas",
    "main reservas 234",
    "main añadir habitacion 104 4 50",
    "main reservas",
    "main list",
    "main añadir reserva 104 hornos jordi 12345678z 123456789",
    "main añadir habitacion 105 2 60",
    "main list",
    "main finalizar 100 0",
    "main finalizar 105 4",
    "main añadir habitacion 106 2 40",
    "main añadir reserva 105 segura albert 45790286t 123456789",
    "main info 12345678z",
    "main info 23415678E",
    "main reservas",
    "main finalizar 104 0",
    "main list",
    "main finalizar 105 4",
    "main list",
    "main limpiar 106",
    "main limpiar 104",
    "main limpiar 105",
    "main list",
]

def main():

    for comand in com:
        comando = comand.split(" ")

        #comando = sys.argv
        if len(comando) > 1:
            if len(comando) == 6:
                if comando[1].lower() == "añadir" and comando[2].lower() == "habitacion":
                    num = comando[3]
                    capacidad = comando[4]
                    precio = comando[5]
                    afegirHabitacio(num, capacidad, precio)
            if len(comando) == 8:
                if comando[1].lower() == "añadir" and comando[2].lower() == "reserva":
                    num = comando[3]
                    nom = comando[4]
                    ap = comando[5]
                    dni = comando[6]
                    tel = comando[7]
                    afegirReserva(num, nom, ap, dni, tel)
            if len(comando) == 5:
                if comando[1].lower() == "finalizar" and comando[2].lower() == "habitacion":
                    num = comando[3]
                    dias = comando[4]
                    finalitzarHabitacio(num, dias)
            if len(comando) == 2:
                if comando[1].lower() == "reservas":
                    mostrarReservas()

main()