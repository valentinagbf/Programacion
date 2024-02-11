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


cargarDatos()


def afegirHabitacio(num, capacidad, precio):
    if num not in habitaciones:
        if capacidad.isdigit() and int(capacidad) > 0:
            if precio.replace(".", "", 1).isdigit() and precio.count(".") <= 1 and float(precio) > 0:
                habitaciones[num] = {
                    "Capacidad": capacidad,
                    "Precio": precio,
                    "Estado": "DISPONIBLE"
                }
                f = open(ruta_archivo1, "a")
                f.write(f"{num},{capacidad},{precio},DISPONIBLE\n")
                f.close()
                print("Habitacion Registrada")
            else:
                print("Precio Incorrecta. Debe ser mayor que 0.")
        else:
            print("Capacidad Incorrecta. Debe ser mayor que 0.")
    else:
        print("Ya existe una habitacion con el numero indicado")


def afegirReserva(num, nom, ap, dni, tel):
    #num = int(num)

    if num in habitaciones:
        if habitaciones[num]["Estado"] == "DISPONIBLE":
            if len(dni) == 9:
                if len(tel) == 9 and tel.isdigit():
                    reservas[num] = {
                        "Nombre": nom,
                        "Apellido": ap,
                        "DNI": dni,
                        "Telefono": tel
                    }
                    habitaciones[num]["Estado"] = "OCUPADA"
                    f = open(ruta_archivo2, "a")
                    f.write(f"{num},{nom},{ap},{dni},{tel} \n")
                    f.close()
                    f = open(ruta_archivo1, "r")
                    lineas = f.readlines()
                    f = open(ruta_archivo1, "w")
                    for linea in lineas:
                        if linea.startswith(str(num)):
                            linea = linea.replace("DISPONIBLE", "OCUPADA")
                        f.write(linea)
                    f.close()
                    print("Reserva Registrada")
                    print(reservas)
                else:
                    print("El Formato del Telefono es Incorrecto.")
            else:
                print("El Formato del DNI es Incorrecto.")
        else:
            print("La habitacion indicada no se encuentra disponible para reservar")
    else:
        print("No existe una habitacion con el numero indicado")


def finalitzarHabitacio(num, dias):
    #num = int(num)
    print(habitaciones)
    print(reservas)
    if num in habitaciones:
        if num in reservas:
            precio = habitaciones[num]["Precio"]
            if int(dias) > 0:
                total = precio * int(dias)
                habitaciones[num]["Estado"] = "SUCIA"
                f = open(ruta_archivo1, "r")
                lineas = f.readlines()
                f = open(ruta_archivo1, "w")
                for linea in lineas:
                    if linea.startswith(str(num)):
                        linea = linea.replace("OCUPADA", "SUCIA")
                    f.write(linea)
                f.close()
                f = open(ruta_archivo2, "r")
                lineas = f.readlines()
                f = open(ruta_archivo2, "w")
                for linea in lineas:
                    if linea.startswith(str(num)):
                        reservas.pop(num)
                    else:
                        f.write(linea)
                f.close()
                print(f"Precio total de la estadia: {total}. La habitacion queda en espera del servicio de limpieza")
            elif dias == 0:
                habitaciones[num]["Estado"] = "DISPONIBLE"
                reservas.pop(num)
                print("Reserva Anulada. Sin costo por el cliente. La habitacion vuelve a estar disponible")
            else:
                print("El numero de dias no puede ser negativo. Si quiere anular la reserva "
                      "debe indicar el numero de dias 0")
        else:
            print("La habitacion no se encuentra reservada")
    else:
        print("No exite una habitacion con el numero indicado.")


def mostrarReservas():
    f = open(ruta_archivo2, "r")
    for linea in f:
        partes = linea.strip().split(',')
        print(f"{partes[0]} : {partes[1]} - {partes[2]} {partes[3]} - {partes[4]}")
    f.close()
    # if reservas:
    #  print("========    RESERVAS    ========")
    #  for n, i in reservas.items():
    #      print(f"{n} : {i['DNI']} - {i['Nombre']} {i['Apellido']} - {i['Telefono']}")
    # else:
        # print("No hay reservas.")