catalogo = {
"BK001": ["El Quijote", "Miguel de Cervantes", "físico", 1200, "Editorial Planeta", "español"],
"BK002": ["1984", "George Orwell", "digital", 328, "Penguin", "inglés"],
"BK003": ["Rayuela", "Julio Cortázar", "físico", 600, "Sudamericana", "español"],
"BK004": ["Sapiens", "Yuval Noah Harari", "digital", 450, "Debate", "inglés"],
}

inventario = {
"BK001": [15990, 3],
"BK002": [8990, 0],
"BK003": [18990, 7],
"BK004": [12500, 5],
}

def stock_editorial():
    print("Esto esta organizado por título, autor, tipo, páginas, editorial, idioma")
    editorial = input("Ingrese nombre de una editorial: ")
    editorial.lower
    if editorial == "Editorial Planeta" in catalogo["BK001"]:
        print("La editorial mas cercana es" ,catalogo["BK001"])
    elif editorial == "Penguin" in catalogo["BK002"]:
        print("La editorial mas cercana es" ,catalogo["BK002"])
    elif editorial == "Sudamerica" in catalogo["BK003"]:
        print("La editorial mas cercana es",catalogo["BK003"])
    elif editorial == "Debate" in catalogo["BK004"]:
        print("La editorial mas cercana es",catalogo["BK004"])
    else:
        print("Editorial no encontrada")

def buscar_por_precio():
    p_min = int(input("Ingrese el precio minimo: "))
    p_max = int(input("Ingrese el precio maximo: "))

def actualizar_precio():
    codigo = input("Ingrese el codigo del libro : ")
    if codigo == "BK001":
        nuevo_precio = input("Ingrese nuevo precio: ")
        nuevo_precio.append(inventario["BK001"])
        print(nuevo_precio)

while True:
    print("***MENU***")
    print("1.- Stock por editorial")
    print("2.- Buscar libros por precio")
    print("3.- Actualizar precio por libro")
    print("4.- Salir")
    op = input("Ingrese opcion: ")
    if op == "1":
        stock_editorial()
    elif op == "2":
        buscar_por_precio()
    elif op == "3":
        actualizar_precio()
    elif op == "4":
        print("Saliendo del sistema...")
        break