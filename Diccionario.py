#Imprimir diccionario
print(diccionario)
#Diccionario de datos
diccionario ={
        "Nombre":"Angie Valentina ",
        "Celular":3102917653,
        "Universidad":"Unisangil",
        "Estado":True,
        "Estatura":1.70,
        "Edad":17.5,
        "Lista":["Python", "Java", "C++"],
        "Apellido":"Martínez Poveda",
        "Estado académico":"Estudiante",
}
#Imprimir el diccionario
print(diccionario)

#Diccionario 2
programacion1 = {
    "docente" : {
        "nombre" : "Carlos",
        "apellido" : "Gonzalez",
        "telefono" : 4536748,
        "correo" : "ftgyug@gmail.com"
    },
    "estudiantes" : [
        {
            "nombre" : "Juan",
            "apellido" : "Pérez",
            "cedula" : 1234567890,
            "correo" : "ftuyg@gmai.com"
        },
        {
            "nombre" : "Camila",
            "apellido" : "Rosas",
            "cedula" : 1234545690,
            "correo" : "huhgjrkl@gmai.com"
        }
    ],
    "codigo" : "PROG-101",
    "creditos" : 3,
    "estado" : True
}
#Tipo de dato
print(type(programacion1))
#Imprimir informacion docente
print(programacion1["docente"])
print(programacion1["estado"])
print(programacion1["creditos"])
#Nombre docente
print(programacion1["docente"]["nombre"])
print(programacion1["docente"]["correo"])
#Lista de los estudiantes
for estudiante in programacion1["estudiantes"]:
    print(estudiante["nombre"])

#Items dentro de los diccionario
print(programacion1["docente"].items())
#Kkeys dentro de los diccionarios
print(programacion1.keys())
print(programacion1["docente"].keys())

#Lista de los estudiantes
for estudiante in programacion1["estudiantes"]:
    print(estudiante.keys())

#valores dentro de los diccionarios
print(programacion1["docente"].values())
#Lista de los estudiantes
for estudiante in programacion1["estudiantes"]:
    print(estudiante.values())
#Get dentro de los diccionarios
print(programacion1.get("creditos"))
#cambiar inrformacion dentro de los diccionarios
programacion1["docente"]["nombre"] = "Jesus caro"
print(programacion1["docente"]["nombre"])
#Agregar un atrubutio dentro de los diccionarios
programacion1["programa"] = "Ingenieria de sistemas"
print(programacion1)
#Agregar estuciente al diccionario
#Eliminar atributo
del programacion1["programa"]
print(programacion1)
