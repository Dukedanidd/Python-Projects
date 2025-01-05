import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 5, 7, 11]})

plt.pie(df['A'], labels=df['B'])
plt.show()