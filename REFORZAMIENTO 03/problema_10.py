
departamentos = ["Lima", "Arequipa", "Cusco", "Piura", "Lambayeque"]

print("Lista inicial de departamentos:")
for departamento in departamentos:
    print(f"- {departamento}")

print("\nIngresa 2 departamentos:")

while True:
    primer_departamento = input("Ingresa el primer departamento: ")
    if primer_departamento in departamentos:
        break
    else:
        print("El departamento ingresado no está en la lista inicial. Por favor, inténtalo de nuevo.")

segundo_departamento = input("Ingresa el segundo departamento: ")

indice_primer_departamento = departamentos.index(primer_departamento)
departamentos[indice_primer_departamento] = segundo_departamento

print("\nLista actualizada de departamentos:")
for departamento in departamentos:
    print(f"- {departamento}")