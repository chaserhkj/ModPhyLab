import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as lr

c = [14.45,27.7,53.6,106]
u = [29,54,100,195]

x = np.linspace(10, 110, 200)

k, b, r, _, _ = lr(c, u)

y = k *x + b

plt.plot(x,y, color='blue', label = 'Fitted line')
plt.scatter(c, u, 100, color = 'black',  marker = 'x', label = 'Experiment data')
plt.legend()
plt.xlabel("$C_x$/pF")
plt.ylabel("$u_i$/$\mu$V")
plt.text(10, 225, 'r = {0}'.format(r), bbox = {'pad':10, 'facecolor':'white'}, fontsize = 15)
plt.savefig('plot1.pdf')
