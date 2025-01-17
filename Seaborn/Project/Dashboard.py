import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

diamantes = sns.load_dataset('diamonds')

diamantes.head()

sns.set_style('whitegrid')

g = sns.relplot(
    data = diamantes,
    x = 'carat',
    y ='price',
    aspect=1.5,
    height=6,
    kind = 'scatter'
)

# Ahora vamos a crear la distribucion de los precios
g = sns.displot(
    data = diamantes,
    x = 'price',
    kde = True,
    color = 'blue',
    height = 6,
    aspect = 2
)

g.fig.suptitle('Distribucion de los precios de los diamantes',
               va = 'baseline',
               ha = 'center')

g.set_axis_labels('Precio en dlls', 'Frecuencia')