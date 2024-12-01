# Programa Proyecto "CASHDOWN" EDD

print("\n \tBienvenido, digite una opcion de inicio")
print("\n 1 Sign up/Inicio de Sesion")
print("\n 2 Log up/Registrarse")
Usuario = 0
opcion = int(input("\n Digite una opción "))

print()

if opcion == 1 :
    Usuario = (input("Digite su Usuario: "))
    contraseña = (input("Digite su contraseña: "))

elif opcion == 2 :
    Correo = (input("Digite su Correo Electronico: "))
    Usuario = (input("Nombre de Usuario: "))
    print("\n La contraseña debe de tener al menos 8 caracteres (numeros,puntos y comas etc.)")
    Contraseña = (input("\n Crear contraseña: "))
    Confirmar = (input("Confirmar Contraseña: "))
    Registro = (input("INICIANDO REGISTRO"))
    print("\n Registro EXITOSO")
else:
    print("ERROR, Opcion no disponible")
print()

Saldo = 500

Equipos_AFC = {"1 Pittsburgh Steelers","2 Baltimore Ravens","3 Cincinnati Bengals","4 Cleveland Browns","5 Buffalo Bills","6 Miami Dolphins",
               "7 New England Patriots","8 New York Jets","9 Houston Texans","10 Indianapolis Colts","11 Jacksonville Jaguars","12 Tennessee Titans",
               "13 Denver Broncos","14 Kansas City Chiefs","15 Las Vegas Raiders","16 Los Angeles Chargers"}

Equipos_NFC = {"1 Arizona Cardinals","2 Los Angeles Rams","3 San Francisco 49ers","4 Seattle Seahawks","5 Atlanta Falcons","6 Carolina Panters",
               "7 New Orleans Saints","8 Tampa Bay Buccaneers","9 Dallas Cowboys","10 New York Giants","11 Philadelphia Eagles","12 Washington Commanders",
               "13 Chicago Bears,""14 Detroit Lions","15 Green Bay Packers","16 Minnesota Vikings"}

Historial = []

while True:
    print(f"\n Su saldo es de: {Saldo}")

    print("Menu")
    print("1.Ingresar Efectivo")
    print("2.Retirar Efectivo")
    print("3.Saldo ")
    print("4.Equipos AFC")
    print("5.Equipos NFC")
    print("6.Salir")

    menu = int(input("\n Digite una opción "))

    if menu == 1:
        extra = float(input("Cuanto efectivo desea ingresar: "))
        Saldo += extra
    elif menu == 2:
        retiro = float(input("Cuanto efectivo desea retirar: "))
        Saldo -= retiro
    elif menu == 3:
        print({Saldo})
    elif menu == 4:
        print(Equipos_AFC)
        AFC = int(input("\n Digita tu equipo favorito de la AFC: "))
        print(AFC)
        print("\n Guardando Seleccion de equipo")
        print("Se a registrado su equipo")
    elif menu == 5:
        print(Equipos_NFC)
        print("\n Su equipo se ah guardado correctamente")
        NFC = int(input("\n Digita tu equipo favorito de la NFC: "))
        print(NFC)
        print("\n Guardando Seleccion de equipo")
        print("Se a registrado su equipo")
    elif menu == 6:
        print("Saliendo del menu")
        break
    else:
        print("ERROR--> OPCION NO DISPONIBLE")

print("Cuenta lista para empezar a GANAR DINERO!!")

print("\n Para empezar con buen pie. \n Empecemos a apostar")

while True:
    print("\n 1.Partidos/Calendario")
    print("2.Revisar historial de partidos pasados")
    print("3.Apostar a tu equipo")
    print("4.Apostar a equipo diferente")
    print("5.Tabla de posiciones")

    partidos = int(input("\n Digite una opción"))

    if partidos == 1:
        print("Da click en el siguiente link para acceder a los partidos y el calendario de los proximos partidos")
        print("\n https://www.espn.com.mx/futbol-americano/nfl/calendario")
    elif partidos == 2:
        print("\n El historial de partidos esta diponible en el siguiente enlace")
        print("https://www.espn.com.mx/futbol-americano/nfl/resultados")
    elif partidos == 3:
        print(f"\n Su saldo disponible es de: {Saldo}")
        extra = float(input("Cuanto deseas aposta?: "))
        Saldo += extra
        print(f"Has confiado en tus poderosos: {AFC} {NFC}")
    elif partidos == 4:
        print(f"\n Su saldo disponible es de: {Saldo}")
        print("A que equipo desea apostar")
        print(Equipos_AFC)
        print(Equipos_NFC)
        equipo = int(input("Seleccione el equipo que desee: "))
        print(f"Has confiado en los poderosos: {AFC} {NFC}")
    elif partidos == 5 :
        print("En el siguiente link puedes solicitar ver \n las pósiciones de tus equipos favoritos")
        print("https://www.espn.com.mx/futbol-americano/nfl/posiciones")











