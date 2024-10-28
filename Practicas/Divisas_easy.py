# Crear un programa que haga una conversion de divisas
#Este debera contener lo siguiente:
# 1. Nombre del usuario
# 2. Fecha en que se realiza la informacion
# 3.Momento del dia
# 4.Cantidad de dolares a cambiar

# Un saludo de bienvenida
# Informacion de la cantidad de dolares que va a entregar el usuario
# Informacion de la cantidad de euros que va a recibir
# Detalle especifico de cuantos billetes de $10 de $1 y monedas le seran entregadas
# Despedida

name = 'Daniel'
date = '12/10/2021'
moment = 'Buenas tardes'


dolar = 210.0
euros = dolar * 0.88

billetes_10 = euros // 10
billetes_1 = euros % 10 // 1
monedas = euros % 10 // 1

welcome = f'{moment} {name}, bienvenido a la casa de cambio, hoy {date}'
change = f'Usted va a entregar {dolar} dolares y recibira {euros} euros'
type = f'Le entregaremos {billetes_10} billetes de 10 euros, {billetes_1} billetes de 1 euro y {monedas} monedas de euro'
print(welcome)
print(change)
print(type)