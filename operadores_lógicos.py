
num1 = 5
num2 = 5
num3 = 10

#Operador lógico "and" multiplicación &
print(num1 == num2 and num1 != num3) # 1 * 1 = 1
print(num1 == num2 and num1 > num3) # 1 * 0 = 0
print(num1 != num2 and num1 > num3) # 0 * 0 = 0
print(num1 != num2 and num1 < num3) # 0 * 1 = 0

#Operador lógico "or" suma lógica |
print(num1 == num2 or num1 != num3) # 1  1 = 1
print(num1 == num2 or num1 != num3) # 1 * 1 = 1
print(num1 == num2 and num1 != num3) # 1 * 1 = 1
print(num1 == num2 and num1 != num3) # 1 * 1 = 1
