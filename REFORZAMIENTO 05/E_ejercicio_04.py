
def mensaje_personalizado():
    nombre = input("Por favor, ingresa tu nombre: ")

    string = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
    string = string.replace("NOMBRE", nombre)
    string = string.replace("DÍA", "04")
    string = string.replace("MES", "Mayo")
    string = string.replace("AÑO", "2024")

    try:
        print(string / 0)

    except ZeroDivisionError:
        print("Error: No puedes dividir una cadena o cualquier valor por cero.")
        print("Causa: Estás intentando realizar una operación matemática inválida.")
        print("Solución: Revisa el código para evitar operaciones de división por cero.")

    except TypeError:
        print("Error: No puedes dividir una cadena por un número.")
        print("Causa: La operación que intentas hacer es entre tipos de datos incompatibles (cadena y número).")
        print("Solución: Asegúrate de que las operaciones matemáticas sean entre números.")

    except Exception:
        print("Error inesperado")
        print("Causa: Ocurrió un error no previsto.")
        print("Solución: Revisa el código y los datos ingresados.")

    else:
        print(string)

mensaje_personalizado()