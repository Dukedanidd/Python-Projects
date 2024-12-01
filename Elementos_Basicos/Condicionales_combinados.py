#Condicionales Combinados

edad = int(input("Digite su edad: "))

if 0<edad<100:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")