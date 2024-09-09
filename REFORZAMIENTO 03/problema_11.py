
bases_datos = ["MySQL", "PostgreSQL", "Oracle", "SQL Server", "SQLite"]

# Imprimir la lista inicial
print("Lista inicial de bases de datos:")
for base_datos in bases_datos:
    print(f"- {base_datos}")

# Pedir al usuario que ingrese el nombre de una base de datos
base_datos_ingresada = input("\nIngresa el nombre de una base de datos: ")

# Verificar si la base de datos ingresada está en la lista
if base_datos_ingresada in bases_datos:
    bases_datos.remove(base_datos_ingresada)
    print(f"La base de datos '{base_datos_ingresada}' ha sido eliminada de la lista.")
else:
    print(f"La base de datos '{base_datos_ingresada}' no se encuentra en la lista inicial.")
    bases_datos.append(base_datos_ingresada)
    print(f"La base de datos '{base_datos_ingresada}' ha sido agregada a la lista.")

# Imprimir la lista actualizada
print("\nLista actualizada de bases de datos:")
for base_datos in bases_datos:
    print(f"- {base_datos}")