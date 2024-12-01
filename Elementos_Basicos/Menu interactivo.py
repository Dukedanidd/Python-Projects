#Menu Interactivo
saldo = 1000

while True:

    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))

    print()

    if opcion==1:
        extra = float(input("Cuánto dinero desea ingresar -> "))
        saldo += extra
        print(f"Dinero en la cuenta: " , saldo)
    elif opcion==2:
        retirar = float(input("Cuánto dinero desea retirar -> "))
        if retirar>saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta: ${saldo}")
    elif opcion==3:
        print(f"Dinero en la cuenta: ${saldo}")
    elif opcion==4:
        print("Gracias por utilizar su cajero automático")
        break
    else:
        print("Error, se equivocó de opción de menú")

    print()