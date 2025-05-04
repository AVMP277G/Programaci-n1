#Guardar archivo en formato JSON
#Libreria JSON
import json
#Guardar archivo en formato JSON
datos = {
        "nombre" : "Angie",
        "apellido" : "Martínez",
        "telefono" : 3102917653,
        "correo" : "angiemartinez224@unisangil.edu.co",
        "usuario": "AVMP277G"
}
#Variable para guardar el archivo
archivo = open("informacion.json", "w")
#Guardar el archivo en formato JSON
json.dump(datos, archivo)
#Cerrar el archivo
archivo.close()
