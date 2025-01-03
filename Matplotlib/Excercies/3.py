import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, 'ro-')
plt.axis([0,10,0,12])
plt.grid()
plt.show()