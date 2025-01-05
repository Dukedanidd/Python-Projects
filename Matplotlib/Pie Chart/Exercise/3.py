import matplotlib.pyplot as plt
import pandas as pd 
df = pd.DataFrame({
    "frutas": ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos'],
    "cantidades": [40, 25, 15, 20]
})

plt.pie(df['cantidades'], 
        labels=df['frutas'], 
        autopct='%1.1f%%',
        colors = ['red', 'yellow', 'darkred', 'orange'],
        shadow = 'True',
        explode = (0,0,0.5,0))
plt.title('Distribución de frutas en el almacén')
plt.show()