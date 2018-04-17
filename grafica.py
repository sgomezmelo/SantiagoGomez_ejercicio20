import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('resultados.txt')
u = datos[-1, 1:]
x = range(len(u))

plt.figure
plt.plot(x,u)
plt.savefig('PDE.pdf')
