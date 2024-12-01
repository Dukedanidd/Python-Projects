# Ejercicio 4 Cap 2

'''
Construir un programa que simule el funcionamiento de una calculadora
realizando las 4 operaciones basicas
'''

num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))

operacion = input("Digite la operacion: ").upper()

if operacion == 'S' :
    suma = num1 + num2
    print(f"\n La suma es: {suma}")
elif operacion == 'R':
    resta = num1 - num2
    print(f"\n La resta es: {resta}")
elif operacion == 'M':
    multiplicacion = num1 * num2
    print(f"\n La multiplicacion es: {multiplicacion}")
elif operacion == 'D':
    division = num1 / num2
    print(f"\n La division es: {division: .2f}")

