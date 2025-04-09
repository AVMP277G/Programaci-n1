# Variable Op
opcion = (input("Ingrese una opción: "))
#Estructura de control While
while opcion != 0:
    print("Opción ingresada: ", opcion)
    opcion = int(input("Ingrese una opción: "))

# While
while opcion != "salir":
    print("Dentro del bucle de repetición")
print("Fuera del bucle while")

# While true
while True:
    opcion = input("Ingrese una opción: ")
    if opcion == "salir":
        break
    print("Dentro del bucle de repetición")