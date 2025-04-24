#Datos inicio de sesión
Angie = "AVMP277G"
password = 7027
print(type(password))
#Solicitud datos
usuario = input("Usuario: ")
contraseña = int(input("Contraseña: "))
print(type(contraseña))
#Validación
#Operadores de comparación
if (Angie == usuario and password == contraseña):
    print("Bienvenido Sistema")
else:
    print("Usuario o contraseña incorrectos")
