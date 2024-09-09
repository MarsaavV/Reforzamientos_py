
agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado con el número: {telefono}")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"{nombre} tiene el número de teléfono: {agenda[nombre]}")
    else:
        print("No se encuentra registrado.")

while True:
    print("\n--- Agenda ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == '1':
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el número de teléfono: ")
        agregar_contacto(nombre, telefono)

    elif opcion == '2':
        nombre = input("Ingrese el nombre de la persona a buscar: ")
        buscar_contacto(nombre)

    elif opcion == '3':
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")