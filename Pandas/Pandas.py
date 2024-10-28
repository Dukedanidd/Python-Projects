import pandas as pd

df = pd.read_csv('customers-100.csv')

print(df.head()) # Este sirve para mostrar las primeras filas del archivo
print(df.isnull().sum()) # Este sirve para mostrar las celdas vacias o valores nulos

# Esta elimina las filas con nulos
df_clened = df.dropna()

# Para filtrar (Por ejemplo aqui estamos filtrando las personas que tengan como country chile)
chile_customers = df[df['Country'] == 'Chile']
print(chile_customers)

# Tambien se pueden filtros anidados
chile_customers = df[(df['Country'] == 'Chile') & (df['Company'] == 'Rasmussen Group')]
print(chile_customers)

# Para agregar nueva informacion (Aqui estamos diciendole que esto es un DataTime)
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])
# Aqui agregamos la columna Days Since Subscription
df['Days since Subscription'](pd.Timestamp.now() - df['Subscription Date']).dt.days

# Para crear un nuevo archivo ya actualizado con lo que agregamos seria asi
df.to_csv('newfile.csv' , index = false)

# Para agrupar Datos
customers_by_country = df.groupby('Country')['Customer Id'].count()
print(customers_by_country)