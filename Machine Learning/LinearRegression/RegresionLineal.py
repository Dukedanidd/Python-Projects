import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.DataFrame()
df['Area'] = [2600,3000,3200,3600,4000]
df['Price'] = [550000,565000,610000,680000,725000]



X = df[['Area']]
y = df['Price']

modelo = linear_model.LinearRegression()
modelo.fit(X, y)

plt.plot(
    df['Area'],
    modelo.predict(X),
)
plt.scatter(df['Area'], df['Price']),
plt.show()
