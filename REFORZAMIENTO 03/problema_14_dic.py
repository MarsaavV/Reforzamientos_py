
departamentos = {
    'Lima': 'Capital',
    'Arequipa': 'Ciudad blanca',
    'Cusco': 'Antigua capital',
    'Piura': 'Tierra de la eterna primavera',
    'Trujillo': 'Capital de la primavera',
    'Iquitos': 'Capital de la Amazonía'
}

departamento_a_borrar = 'Piura'
if departamento_a_borrar in departamentos:
    del departamentos[departamento_a_borrar]
    print(f"\nEl departamento '{departamento_a_borrar}' ha sido borrado.")
else:
    print(f"\nEl departamento '{departamento_a_borrar}' no se encuentra en el diccionario.")

if departamento_a_borrar not in departamentos:
    print(f"\nEl departamento '{departamento_a_borrar}' no existe en el diccionario.")

carrera = input("\nIngresa el nombre de tu carrera: ")
departamentos['Carrera'] = carrera

print("\nValores del diccionario actualizado:")
for departamento, descripcion in departamentos.items():
    print(f"{departamento}: {descripcion}")