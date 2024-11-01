import os

# Diccionario para almacenar clientes
clientes = {}

# Función para agregar un cliente nuevo
def agregar_cliente(nombre, descripcion):
    if nombre in clientes:
        print("El cliente ya existe. Actualizando descripción...")
        clientes[nombre].append(descripcion)
    else:
        print("Creando un nuevo cliente...")
        clientes[nombre] = [descripcion]
    guardar_cliente(nombre)

# Función para guardar cliente en un archivo
def guardar_cliente(nombre):
    with open(f"{nombre}.txt", "w") as file:
        for descripcion in clientes[nombre]:
            file.write(f"{descripcion}\n")
    print(f"Información guardada en {nombre}.txt")

# Función para leer la información de un cliente
def leer_cliente(nombre):
    if nombre in clientes:
        print(f"Información del cliente {nombre}:")
        for descripcion in clientes[nombre]:
            print(f"- {descripcion}")
    else:
        print("Cliente no encontrado.")

# Función para eliminar un cliente
def eliminar_cliente(nombre):
    if nombre in clientes:
        os.remove(f"{nombre}.txt")
        del clientes[nombre]
        print(f"Cliente {nombre} eliminado.")
    else:
        print("Cliente no encontrado.")

# Ejemplo de uso
agregar_cliente("Empresa ABC", "Servicio de consultoría")
leer_cliente("Empresa ABC")
eliminar_cliente("Empresa ABC")
