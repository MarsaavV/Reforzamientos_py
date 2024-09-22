import M_ejercicio_05

def main():

    nombre_usuario = input("Por favor, ingresa un nombre de usuario: ")
    resultado = M_ejercicio_05.validar_nombre_usuario(nombre_usuario)

    if resultado is True:
        print("El nombre de usuario es válido.")

    else:
        print("Error: {}".format(resultado))


if __name__ == "__main__":
    main()