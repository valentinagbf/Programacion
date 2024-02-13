# Este modulo contiene las funciones relacionadas con los ficheros y el almacenamiento de datos del programa


import os


habitaciones = {}
reservas = {}
nombre_carpeta = "./datos"
ruta_archivo1 = nombre_carpeta + "/habitaciones.txt"
ruta_archivo2 = nombre_carpeta + "/reservas.txt"


def cargarDatos():
    if os.path.exists(nombre_carpeta):
        if os.path.exists(ruta_archivo1):
            f = open(ruta_archivo1, "r")
            lineas = f.readlines()
            f.close()
            for linea in lineas:
                linea = linea.split(",")
                num = linea[0]
                capacidad = int(linea[1])
                precio = float(linea[2])
                estat = linea[3].replace("\n", "")
                habitaciones[num] = {
                    "Capacidad": capacidad,
                    "Precio": precio,
                    "Estado": estat
                }
        if os.path.exists(ruta_archivo2):
            f = open(ruta_archivo2, "r")
            lineas = f.readlines()
            f.close()
            for linea in lineas:
                linea = linea.split(",")
                num = linea[0]
                nom = linea[1]
                ap = linea[2]
                dni = linea[3]
                tel = int(linea[4].replace("\n", ""))
                reservas[num] = {
                    "Nombre": nom,
                    "Apellido": ap,
                    "DNI": dni,
                    "Telefono": tel
                }
    else:
        os.mkdir(nombre_carpeta)


def leer(ruta):
    f = open(ruta, "r")
    lineas = f.readlines()
    f.close()
    return lineas


def escribir(ruta, datos):
    f = open(ruta, "a")
    for dato in datos:
        f.write(f"{dato}\n")
    f.close()


def reescribirDato(ruta, num, old, new):
    f = open(ruta, "r")
    lineas = f.readlines()
    f = open(ruta, "w")
    for linea in lineas:
        if linea.startswith(str(num)):
            linea = linea.replace(old, new)
        f.write(linea)
    f.close()


def eliminar(ruta, num):
    f = open(ruta, "r")
    lineas = f.readlines()
    f = open(ruta, "w")
    for linea in lineas:
        if linea.startswith(str(num)):
            reservas.pop(num)
        else:
            f.write(linea)
