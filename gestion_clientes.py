import os

# Diccionario para almacenar clientes
clientes = {}

# Función para agregar o actualizar un cliente
def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    descripcion = input("Ingrese la descripción del servicio solicitado: ")
    
    if nombre in clientes:
        print(f"El cliente {nombre} ya existe. Actualizando descripción...")
        clientes[nombre].append(descripcion)
    else:
        print(f"Creando un nuevo cliente: {nombre}")
        clientes[nombre] = [descripcion]
    
    guardar_cliente(nombre)

# Función para guardar cliente en un archivo
def guardar_cliente(nombre):
    with open(f"{nombre}.txt", "w") as file:
        for descripcion in clientes[nombre]:
            file.write(f"{descripcion}\n")
    print(f"Información guardada en {nombre}.txt")

# Función para leer la información de un cliente
def leer_cliente():
    nombre = input("Ingrese el nombre del cliente a consultar: ")
    if nombre in clientes:
        print(f"Información del cliente {nombre}:")
        for descripcion in clientes[nombre]:
            print(f"- {descripcion}")
    else:
        print("Cliente no encontrado.")

# Función para eliminar un cliente
def eliminar_cliente():
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    if nombre in clientes:
        os.remove(f"{nombre}.txt")
        del clientes[nombre]
        print(f"Cliente {nombre} eliminado.")
    else:
        print("Cliente no encontrado.")

# Función principal para interactuar con el usuario
def menu():
    while True:
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Agregar o actualizar un cliente")
        print("2. Consultar un cliente")
        print("3. Eliminar un cliente")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            leer_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
