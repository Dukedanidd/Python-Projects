# Calculadora basica

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def divisio(a, b):
    return a / b

while True:
    a = int(input('Ingresa el numero 1: '))
    b = int(input('Ingresa el numero 2: '))
    
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Salir')
    
    opcion = int(input('Elige una opcion: '))
    
    if opcion == 1:
        print(suma(a, b))
    elif opcion == 2:
        print(resta(a, b))
    elif opcion == 3:
        print(multiplicacion(a, b))
    elif opcion == 4:
        print(divisio(a, b))
    elif opcion == 5:
        break
    else:
        print('Opcion no valida')

