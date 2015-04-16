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
u = u[:-1]
c = c[:-1]

A = 5.03e-3
ee0 = 11.8 * 8.854e-14
q = 1.602e-19

N = (- 1.0 / q / ee0 / A / A) * np.array(c) ** 3 / np.array(dc)
w = ee0 * A /  np.array(c)

plt.xlabel("w/cm")
plt.ylabel("N/cm$^{-3}$")
plt.plot(w, N)
plt.savefig("Nw.pdf")

