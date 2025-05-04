# Calculadora con While
# Libreria Math
import math
# While true
while True:
<<<<<<< HEAD
    # Menú
    print("\nBienvenido a la Calculadora de Operaciones Básica")
print("Menú de opciones")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicación")
print("4. Divición") 
print("5. Potencia")
print("6. Raíz cuadrada")
print("7. Salir")
# Opción
opción = int (input("Ingrese una opción: "))
=======
    #Menú
    print("/n Bienvenido a la Calculadora de Operaciones Básica")
    print("Menú de opciones")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicación")
    print("4. Divición") 
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")
    # Opción
    opción = int (input("Ingrese una opción: "))
>>>>>>> bc008c64ea13687e6faa6565b66f0a81a334c193

if opción == 1:
        num_1 = float(input("Ingrese el primer número: "))
        num_2 = float(input("Ingrese el segundo número: "))
        suma = num_1 + num_2
        print(f"El resultado de la suma es: {suma}")
        
elif opción == 2:
        num_1 = float(input("Ingrese el primer número: "))
        num_2 = float(input("Ingrese el segundo número: "))
        resta = num_1 - num_2
        print(f"El resultado de la resta es: {resta}")

elif opción == 3:
        num_1 = float(input("Ingrese el primer número: "))
        num_2 = float(input("Ingrese el segundo número: "))
        producto= num_1 * num_2
        print(f"El resultado de la multiplicación es: {producto}")

elif opción == 4:
        num_1 = float(input("Ingrese el primer número: "))              
        num_2 = float(input("Ingrese el segundo número: "))
        cociente = num_1 / num_2
        print(f"El resultado de la división es: {cociente}")

elif opción == 5:
        num_1 = float(input("Ingrese la base: "))
        num_2 = float(input("Ingrese la potencia: "))
        potencia = num_1 ** num_2
        print(f"El resultado de la potencia es: {potencia}")

elif opción == 6:
        num_1 = float(input("Ingrese la base: "))
        raiz = math.sqrt(num_1)
        print(f"El resultado de la raíz cuadrada es: {raiz}")  

elif opción == 7:
    print("Saliendo de la Calculadora ......")
<<<<<<< HEAD
    print("Gracias por usar la Calculadora de Operaciones Básica!!!")
    break
=======
    
>>>>>>> bc008c64ea13687e6faa6565b66f0a81a334c193
else:
        print("Opción errónea, intente de nuevo")


<<<<<<< HEAD
    print("Dentro del bucle de repetición")
=======
print("Dentro del bucle de repetición")
print("Gracias por usar la Calculadora de Operaciones Básica!!!")
break 
>>>>>>> bc008c64ea13687e6faa6565b66f0a81a334c193
