import datetime

def buenos_dias_decorator(func):

    def wrapper():
        hora_actual = datetime.datetime.now()
        hora = hora_actual.hour
        minutos = hora_actual.minute

        print("Buenos días, son las {} horas con {} minutos.".format(hora, minutos))

        func()

        print("Hasta luego, que tenga buen día.")

    return wrapper


@buenos_dias_decorator
def saludar():

    nombre = input("¿Cuál es tu nombre? ")
    print("¡Hola, {}!".format(nombre))

saludar()
