
persona = {
    'nombre': 'Juan Pérez',
    'edad': 30,
    'salario': 50000
}

lista_persona = list(persona.items())
print("Diccionario convertido a lista:")
print(lista_persona)

persona['dni'] = '12345678'

print(f"\nSalario: {persona['salario']}")

if 'edad' in persona:
    del persona['edad']

print("\nDiccionario actualizado:")
print(persona)

lista_actualizada = list(persona.items())
print("\nDiccionario actualizado convertido a lista:")
print(lista_actualizada)

print(f"\nTipo de datos final: {type(lista_actualizada)}")