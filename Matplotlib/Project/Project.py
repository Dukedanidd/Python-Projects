import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Datos+Meteorológicos_Arg_2023.csv')

df['Fecha'] = pd.to_datetime(df['Fecha'])

lista_ciudades = []

for c in df['Ciudad']:
    if c not in lista_ciudades:
        lista_ciudades.append(c)
        
dict_meses = {1: 'Enero', 
              2: 'Febrero', 
              3: 'Marzo', 
              4: 'Abril', 
              5: 'Mayo', 
              6: 'Junio', 
              7: 'Julio', 
              8: 'Agosto', 
              9: 'Septiembre', 
              10: 'Octubre', 
              11: 'Noviembre', 
              12: 'Diciembre'}

def consultar_temperatura():
    while True:
        print('Ciudades disponibles: ', lista_ciudades)
        ciudad = input('Digita el nombre de la ciudad: ')
        
        print('Meses disponibles: ', dict_meses.values())
        mes = int(input('Digita el numero del mes, EJEMPLO: 1 para Enero: '))
        
        if ciudad not in lista_ciudades or mes not in dict_meses not in range(1,13):
            print('Ciudad o mes no validos')
            continue
        
        df_ciudad_mes= df[(df['Ciudad'] == ciudad) & (df['Fecha'].dt.month == mes)]
        
        # Creamos el grafico
        plt.figure(figsize=(10, 6))
        plt.plot(df_ciudad_mes['Fecha'], df_ciudad_mes['Temperatura Maxima'], label = 'Temperatura Maxima', color = 'red')
        plt.plot(df_ciudad_mes['Fecha'], df_ciudad_mes['Temperatura Minima'], label = 'Temperatura Minima', color = 'blue')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura')
        plt.title(f'Temperatura en {ciudad} en el mes de {dict_meses[mes]}')
        plt.legend()
        plt.show()

consultar_temperatura()

