# CREAR UN PEQUENO MENU DE OPCIONES



while True:
    print('1.- Sumar')
    print('2.- Restar')
    print('3.- Salir')
    opcion = int(input('Digite una opcion: '))
    
    print()
    
    if opcion == 1:
        num1 = int(input('Digite el numero 1: '))
        num2 = int(input('digite el numero 2: '))
        print('La suma es ', num1 + num2)
    elif opcion == 2:
        num1 = int(input('digite el numero 1: '))
        num2 = int(input('Digite el numero 2: '))
        print('La resta es ', num1 - num2)
    elif opcion == 3: 
        print('gracias por visitarnos')
        break
    else:
        print('creo que haz cometido un error, revisa tu respuesta')
        