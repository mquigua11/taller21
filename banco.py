import os

CARPETA = "clientes"
ARCHIVO = os.path.join(CARPETA, "clientes.csv")

def crear_archivo():
    if not os.path.exists(CARPETA):
        os.mkdir(CARPETA)
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("cedula,nombre,saldo\n")
        f.write("12345,jose,50.43\n")
        f.write("56789,santiago,43.12\n")
        f.write("90876,mauricio,99.60\n")
        f.write("93245,felipe,34.50\n")
        f.write("34567,samuel,78.90\n")
    print("Archivo clientes.csv creado con datos de ejemplo.")

def leer_clientes():
    clientes = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lineas = f.readlines()[1:] 
        for linea in lineas:
            cedula, nombre, saldo = linea.strip().split(",")
            clientes.append({"cedula": cedula, "nombre": nombre, "saldo": float(saldo)})
    return clientes

def consultar_saldo():
    nombre = input("Ingrese el nombre del cliente: ")
    clientes = leer_clientes()
    for c in clientes:
        if c["nombre"].lower() == nombre.lower():
            print("El saldo de", c["nombre"], "es:", c["saldo"])
            return
    print("Cliente no encontrado.")

def clientes_mayores_50():
    clientes = leer_clientes()
    contador = sum(1 for c in clientes if c["saldo"] > 50)
    print("Cantidad de clientes con saldo mayor a 50:", contador)

def listar_ordenados():
    clientes = leer_clientes()
    clientes_ordenados = sorted(clientes, key=lambda x: x["saldo"])
    print("\nClientes ordenados por saldo:")
    for c in clientes_ordenados:
        print(c["nombre"], "-", c["saldo"])

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear archivo con datos")
        print("2. Consultar saldo de un cliente")
        print("3. Contar clientes con saldo mayor a 50")
        print("4. Listar clientes ordenados por saldo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            consultar_saldo()
        elif opcion == "3":
            clientes_mayores_50()
        elif opcion == "4":
            listar_ordenados()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
