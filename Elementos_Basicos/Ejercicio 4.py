#Ejercicio 4 - El area de un circulo y su longitud de la circunferencia
import math

radio = float(input("radio -->"))

area = (math.pi * radio**2)
longitud = 2 * math.pi * radio

print(f"El area es: {area}")
print(f"La longitud es: {longitud}")