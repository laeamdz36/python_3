"""Practica de sumar n numeros"""

numInt = int(input("Ingrese numero entero"))

result = 0
for num in range(1, numInt+1, 1):
    print(num)
    result = result + num
    print(f"parcial result -> {result}")
print(f"Result -> {result}")
