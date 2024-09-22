
def contar_argumentos_decorator(func):

    def wrapper(*args, **kwargs):

        cantidad_args = len(args) + len(kwargs)
        print("La cantidad de argumentos que tiene la función es: {}".format(cantidad_args))

        resultado = func(*args, **kwargs)

        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado

    return wrapper


@contar_argumentos_decorator
def suma(*args):

    return sum(args)

resultado = suma(4, 1, 10, 2, 50, 64)
print("Resultado de la suma: {}".format(resultado))
