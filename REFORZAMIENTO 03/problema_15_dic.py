
print("Ingresa 4 números:")
numeros = []
for i in range(4):
    numero = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(numero)

diccionario = {num: num**3 for num in numeros}

print("\nDiccionario creado:")
for numero, cubo in diccionario.items():
    print(f"{numero}: {cubo}")