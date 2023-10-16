class Empleado:
    def __init__(self, id, nombre, apellido, cargo, area, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.salario = salario

SALARIO_MINIMO = 908526  # Ejemplo de salario mínimo vigente

def calcular_salario_neto(empleado):
    if empleado.salario < 2 * SALARIO_MINIMO:
        salario_neto = empleado.salario + 106454  # Valor del auxilio de transporte
    else:
        salario_neto = empleado.salario
    return salario_neto

def imprimir_colilla(empleado):
    salario_neto = calcular_salario_neto(empleado)
    print("Colilla de Pago")
    print(f"ID: {empleado.id}")
    print(f"Nombre: {empleado.nombre} {empleado.apellido}")
    print(f"Cargo: {empleado.cargo}")
    print(f"Área: {empleado.area}")
    print(f"Salario Bruto: ${empleado.salario:,.2f}")
    print(f"Salario Neto: ${salario_neto:,.2f}")

empleados = [
    Empleado(1, "Juan", "Perez", "Gerente", "Ventas", 3000000),
    Empleado(2, "Maria", "Lopez", "Analista", "Recursos Humanos", 1500000),
    Empleado(3, "Pedro", "Gomez", "Desarrollador", "Tecnología", 1800000),
]

def listar_empleados():
    print("Listado de Empleados:")
    for empleado in empleados:
        print(f"ID: {empleado.id}, Nombre: {empleado.nombre} {empleado.apellido}, Cargo: {empleado.cargo}")

def buscar_colilla(id_empleado):
    for empleado in empleados:
        if empleado.id == id_empleado:
            imprimir_colilla(empleado)
            return
    print("Empleado no encontrado")

def visualizar_todos_los_empleados():
    print("Listado de Empleados y Colillas de Pago (Analista RH):")
    for empleado in empleados:
        imprimir_colilla(empleado)

while True:
    print("\nMenú:")
    print("1. Listar empleados")
    print("2. Buscar colilla de pago por ID")
    print("3. Visualizar todos los empleados y colillas (Analista RH)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_empleados()
    elif opcion == "2":
        id_empleado = int(input("Ingrese el ID del empleado: "))
        buscar_colilla(id_empleado)
    elif opcion == "3":
        visualizar_todos_los_empleados()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente de nuevo.")

