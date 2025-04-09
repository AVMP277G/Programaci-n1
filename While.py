# Variable Op
opción = (input("Ingrese una opción: "))
#Estructura de control While
while opción != 0:
    print("Opción ingresada: ", opción)
    opción = int(input("Ingrese una opción: "))

# While
while opción != "salir":
    print("Dentro del bucle de repetición")
print("Fuera del bucle while")

# While true
while True:
    opción = input("Ingrese una opción: ")
    if opción == "salir":
        break
    print("Dentro del bucle de repetición")
