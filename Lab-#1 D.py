#Lab #1 - Ejercicio D: Calculo de una compra c descuentos
#Autor: Angie Valentina Martínez Poveda,Camila Contreras,Daniela Martínez
#Fecha y Hora: 25-03-25 /12:00 p.m.
#Programa: Ingeniería de Sistemas 
#Docente: Jesús David Garcia Caro 
# Entrada de datos
monto_compra = float(input("Ingrese el monto de la compra: "))
es_vip = input("¿Es cliente VIP? (s/n): ")
tiene_codigo = input("¿Tiene código de descuento especial? (s/n): ")

# Cálculo de descuentos
total_pagar = monto_compra

if monto_compra > 100:
    total_pagar *= 0.80  # Descuento del 20%

if es_vip == "s":
    total_pagar *= 0.90  # Descuento del 10%

if tiene_codigo == "s":
    total_pagar *= 0.95  # Descuento del 5%

# Resultado
print("El total a pagar después de los descuentos es: $", round(total_pagar, 2))