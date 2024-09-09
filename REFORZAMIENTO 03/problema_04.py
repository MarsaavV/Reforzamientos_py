
nueva_lista = []

print("Ingresa 3 números flotantes:")
for i in range(3):
    float_item = float(input(f"Ingresa el número flotante {i+1}: "))
    nueva_lista.append(float_item)

print("\nIngresa 3 números enteros:")
for i in range(3):
    int_item = int(input(f"Ingresa el número entero {i+1}: "))
    nueva_lista.append(int_item)

print("\nIngresa 3 cadenas de texto:")
for i in range(3):
    string_item = input(f"Ingresa la cadena de texto {i+1}: ")
    nueva_lista.append(string_item)

cursos = [
    "Lenguaje",
    "Microeconomia",
    "Matemática",
    "Investigacion academica",
    "Estadistica",
    "Macroeconomia"
]

lista_final = cursos + nueva_lista

print("\nLista final:")
for item in lista_final:
    print(f"- {item}")