# While

import math

numero = int(input("Digite un numero: "))

while numero < 0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}" )