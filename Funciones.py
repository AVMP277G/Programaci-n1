#Función simple
def mensaje():
    """
    Muestra un mensaje en pantalla
    """
    print("Unisangil")

#Llamada a la función
mensaje()

#Función con parametros
def suma(a, b):
    """
    Suma dos números: int a, int b
    imprime el resultado
    """
    rta = a + b
    print(rta)
#LLamada a la función
suma(10,5)

#Función con retorno
def multiplicación(a,b):
    """
    Multiplica dos números: int a, int b
    Devuelve el resultado de la multiplicación
    Devuelve: int
    """
    rta = a * b
    return rta

#Llamada a la función
rta = multiplicación(10,5)
print(rta * 2)

#Función con retorno y sin parametros
def solicitar_datos():
    """
    Solicitar 2 numeros int
    y los retorna num1 y num2
    """
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    return num1, num2

#Llamada a la función
a,b = solicitar_datos()
print(f"primer número = {a} y segundo número = {b}")
#Llamar suma
suma(a,b)
#Llamar multiplicación
mul = multiplicación(a,b)
print(f"Multiplicación = {mul}")
