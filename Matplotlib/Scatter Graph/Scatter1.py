import matplotlib.pyplot as plt
import numpy as np

x = np.random.RandomState(0)
marcadores = ['o', 's', 'D', 'x', 'v', '^', '>', '<', 'p', 'h']

for marcador in marcadores:
    plt.plot(x.rand(5), x.rand(5), marcador)

plt.show()
