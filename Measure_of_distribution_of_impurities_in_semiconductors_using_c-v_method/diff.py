from matplotlib import pyplot as plt
import numpy as np

u = []
c = []

with open('data.txt') as f:
    line = f.readline()
    while line:
        u.append(float(line.split(',')[0]))
        c.append(float(line.split(',')[1]))
        line = f.readline()

du = 10 *  9.0 / ( 2795 - 613)
dc = np.divide(np.diff(c) , du)

plt.xlabel("U/V")
plt.ylabel(r"$\frac{dC}{dU}$/pFV$^{-1}$")
plt.plot(np.array(u[:-1]), dc)
plt.savefig("diff.pdf")

