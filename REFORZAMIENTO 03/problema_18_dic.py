facturas = {
    "00054": 150.75,
    "00055": 200.50,
    "00056": 75.25
}

def mostrar_facturas():
    print("\nLista de facturas pendientes:")
    if not facturas:
        print("No hay facturas pendientes.")
    else:
        for numero, coste in facturas.items():
            print(f"Factura {numero}: ${coste:.2f}")

def agregar_factura(numero, coste):
    facturas[numero] = coste
    print(f"Factura {numero} agregada con un coste de ${coste:.2f}")

def pagar_factura(numero):
    if numero in facturas:
        del facturas[numero]
        print(f"Factura {numero} pagada y eliminada de la lista.")
    else:
        print(f"No se encontró la factura {numero}.")

while True:
    print("\n--- Gestión de Facturas ---")
    print("1. Agregar nueva factura")
    print("2. Pagar factura")
    print("3. Mostrar facturas pendientes")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        numero_factura = input("Ingrese el número de la nueva factura: ")
        coste_factura = float(input("Ingrese el coste de la factura: "))
        agregar_factura(numero_factura, coste_factura)
        mostrar_facturas()

    elif opcion == '2':
        numero_factura = input("Ingrese el número de la factura que fue pagada: ")
        pagar_factura(numero_factura)
        mostrar_facturas()

    elif opcion == '3':
        mostrar_facturas()

    elif opcion == '4':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")