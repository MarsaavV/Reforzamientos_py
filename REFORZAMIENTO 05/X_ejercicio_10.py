
def decorador_mensaje(func):

    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")

        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")

        return resultado

    return wrapper


@decorador_mensaje
def multiplicar_numeros(a, b, c, **kwargs):

    d = kwargs.get('d', 1)
    e = kwargs.get('e', 1)
    f = kwargs.get('f', 1)


    resultado = a * b * c * d * e * f
    print("Multiplicación de los valores: {} * {} * {} * {} * {} * {} = {}".format(a, b, c, d, e, f, resultado))

    return resultado

multiplicar_numeros(2, 3, 4, d=5, e=6, f=7)
