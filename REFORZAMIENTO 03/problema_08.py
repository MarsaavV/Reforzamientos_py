numeros = [0] * 10  # Inicializa la lista con ceros


print("Por favor, ingresa 10 números:")
for i in range(10):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros[i] = numero
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")


suma = sum(numeros)
media = suma / len(numeros)

print(f"\nLa suma de los números ingresados es: {suma}")
print(f"La media de los números ingresados es: {media}")