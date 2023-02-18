#lista de empleados con formato: (nombre, cantidad de ventas)
empleados = [("Harrison", 15), ("william", 25), ("jorge", 30), ("juan", 7), ("Diego", 37), ("Rosa", 20), ("Gilma", 42), ("sofia", 30), ("elizabeth", 34), ("Elena", 22)]

mayventas = 0
nomemp = ""

for empleado in empleados:
    nombre,ventas = empleado
    
    if ventas > mayventas:
        mayventas = ventas
        nomemp = nombre

print(f"El empleado con mayor cantidad de ventas es {nomemp}, con {mayventas} ventas.")
