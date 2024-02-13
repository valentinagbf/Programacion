# Este modulo almacena las funciones relacionadas con la gestion del hotel


from ficheros import *


cargarDatos()


def comprobarLong(comando, long):
    if len(comando) == long:
        return True
    print("Error: nº de argumentos incorrecto")
    return False


def afegirHabitacio(num, capacidad, precio):
    if num not in habitaciones:
        if num.isdigit() and int(num) > 0:
            if capacidad.isdigit() and int(capacidad) > 0:
                if precio.replace(".", "", 1).isdigit() and precio.count(".") <= 1 and float(precio) > 0:
                    habitaciones[num] = {
                        "Capacidad": capacidad,
                        "Precio": precio,
                        "Estado": "DISPONIBLE"
                    }
                    datos = [f"{num},{capacidad},{precio},DISPONIBLE"]
                    escribir(ruta_archivo1, datos)
                    print("Habitacion Registrada")
                else:
                    print("Precio Incorrecto. Debe ser mayor que 0.")
            else:
                print("Capacidad Incorrecta. Debe ser mayor que 0.")
        else:
            print("El Formato del numero es Incorrecto. Debe ser mayor que 0.")
    else:
        print("Ya existe una habitacion con el numero indicado")


def afegirReserva(num, nom, ap, dni, tel):
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
                    datos = [f"{num},{nom},{ap},{dni},{tel}"]
                    escribir(ruta_archivo2, datos)
                    reescribirDato(ruta_archivo1, num, "DISPONIBLE", "OCUPADA")
                    print("Reserva Registrada")
                else:
                    print("El Formato del Telefono es Incorrecto.")
            else:
                print("El Formato del DNI es Incorrecto.")
        else:
            print("La habitacion indicada no se encuentra disponible para reservar")
    else:
        print("No existe una habitacion con el numero indicado")


def finalitzarHabitacio(num, dias):
    if num in habitaciones:
        if num in reservas:
            precio = habitaciones[num]["Precio"]
            if int(dias) > 0:
                total = precio * int(dias)
                habitaciones[num]["Estado"] = "BRUTA"
                reescribirDato(ruta_archivo1, num, "OCUPADA", "BRUTA")
                eliminar(ruta_archivo2, num)
                print(f"Precio total de la estadia: {total}. La habitacion queda en espera del servicio de limpieza")
            elif int(dias) == 0:
                habitaciones[num]["Estado"] = "DISPONIBLE"
                reescribirDato(ruta_archivo1, num, "OCUPADA", "DISPONIBLE")
                eliminar(ruta_archivo2, num)
                print("Reserva Anulada. Sin costo por el cliente. La habitacion vuelve a estar disponible")
            else:
                print("El numero de dias no puede ser negativo. Si quiere anular la reserva "
                      "debe indicar el numero de dias 0")
        else:
            print("La habitacion no se encuentra reservada")
    else:
        print("No exite una habitacion con el numero indicado.")


def mostrarReservas():
    if reservas:
        print("========    RESERVAS    ========")
        for n, i in reservas.items():
            print(f"{n} : {i['DNI']} - {i['Nombre']} {i['Apellido']} - {i['Telefono']}")
    else:
         print("No hay reservas.")


def netejarHabitacio(num):
    if num in habitaciones:
        if habitaciones[num]["Estado"] == "BRUTA":
            habitaciones[num]["Estado"] = "DISPONIBLE"
            reescribirDato(ruta_archivo1, num, "BRUTA", "DISPONIBLE")
            print("Habitacion Limpia. Queda Disponible.")
        else:
            print("La habitacion no se encuentra sucia.")
    else:
        print("No exite una habitacion con el numero indicado.")


def info(dni):
    cliente = False
    for n, i in reservas.items():
        if i['DNI'] == dni:
            if not cliente:
                cliente = True
                print(f"Datos del Cliente:    {i['Apellido']} , {i['Nombre']} - Tfn: {i['Telefono']}")
            print(f"Habitacion: {n}")
    if not cliente:
        print("El hotel no tiene ninguna reserva con el DNI indicado.")


def list():
    if habitaciones:
        print("========      INFO HOTEL      ========")
        print("Hab     Cap      Estat")
        for n, i in habitaciones.items():
            if i['Estado'] == "OCUPADA":
                print(f"{n}      {i['Capacidad']}      {i['Estado']}      => Cliente: {reservas[n]['Nombre']} "
                      f"{reservas[n]['Apellido']}")
            else:
                print(f"{n}      {i['Capacidad']}      {i['Estado']}")
        print("=============================================")
        total = len(habitaciones)
        oc = 0
        disp = 0
        sucias = 0
        for d in habitaciones.values():
            estado = d['Estado']
            if estado == "DISPONIBLE":
                disp += 1
            elif estado == "OCUPADA":
                oc += 1
            elif estado == "BRUTA":
                sucias += 1
        print(f"Total Habitaciones: {total}")
        print(f"Disponibles: {disp}  Ocupadas: {oc}  Sucias: {sucias}")
    else:
        print("El hotel no tiene habitaciones registradas.")
