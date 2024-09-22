
def acceder_a_diccionario():
    persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
    clave = input("Ingrese la clave que desea consultar (nombre, apellido, dni, profesion, etc.): ")

    try:
        valor = persona[clave]

    except KeyError:
        print(f"Error: La clave '{clave}' no existe en el diccionario.")
        print("Causa: Estás intentando acceder a un dato que no está registrado.")
        print("Solución: Asegúrate de que la clave sea una de las siguientes: 'nombre', 'apellido', 'dni'.")

    except TypeError:
        print("Error: La clave debe ser de tipo cadena (string).")
        print("Causa: Estás intentando acceder con un dato que no es una cadena.")
        print("Solución: Asegúrate de ingresar una clave válida en formato de texto (string).")

    except Exception:
        print("Error inesperado")
        print("Causa: Ocurrió un error no previsto.")
        print("Solución: Revisa el valor ingresado y vuelve a intentarlo.")

    else:
        print("El valor asociado a la clave {} es: {}".format(clave, valor))


acceder_a_diccionario()