# Ejercicio 1 Cap 2
'''
Hacer un programa que pida
2 numeros y se de cuenta
cual es par o si ambos lo son
'''

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos son par")
elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f"{num1} es par")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print(f"{num2} es par")
else:
    print("Ninguno es par")
