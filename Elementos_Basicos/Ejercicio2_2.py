# Ejerciocio 2 Capitulo 2
'''
Hacer un programa que pida 3 numeros y
determine cual es mayor
'''

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

if num1 > num2 > num3:
    print(f"{num1} es mayor a {num2} y a {num3}")
elif num2 > num1 > num3:
    print(f"{num2} es mayor a {num1} y a {num3}")
elif num2 > num1 > num3:
    print(f"{num3} es mayor a {num1} y a {num2}")

# Otra solucion
'''
if num1 >= num2 and num1 >= num3:
    print(f"{num1} es mayor a {num2} y a {num3}")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} es mayor a {num1} y a {num3}")
elif num3 >= num1 and num3 >= num2:
    print(f"{num3} es mayor a {num1} y a {num2}")
'''