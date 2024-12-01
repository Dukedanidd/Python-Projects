# Ejercicio 5 Cap 2

'''
Hacer un programa que simule un cajero automatico con un
 saldo inicial de $1000 y tendra las siguientes opciones

 1 Ingresar dinero a la cuenta
 2 Retirar dinero
 3 Mostrar dinero disponible
 4 Salid
'''

saldo = 1000

print(saldo)

print("\t.:Menu:.")
print("1 Ingresar dinero a la cuenta")
print("2 Retirar dinero")
print("3 Mostrar dinero disponible")
print("4 Salir")
opcion = int(input("Digite una opcion de menu: "))

print()

if opcion == 1 :
    extra = float(input("Cuanto dinero desea ingresar: "))
    saldo += extra
elif opcion == 2 :
    retiro = float(input("Cuanto dinero desea retirar: "))
    saldo -= retiro
elif opcion == 3 :
    mostrar = saldo
elif opcion == 4 :
    print("Gracias por usar su cajero automatico")
else:
    print("ERROR , Se equivoco de Opcion de menu")
print()

print(saldo)
