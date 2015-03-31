# encoding=utf8
from matplotlib import pyplot as plt
from scipy.interpolate import spline
import numpy as np

U = [
        -1,
        50,
        100,
        150,
        200,
        250,
        300,
        350,
        400,
        450,
        500,
        550,
        600,
        650,
        700,
        750,
        800,
        850,
        900,
        950,
        1000,
        1050,
        1100,
        1150,
        1200,
        1250,
        1300,
        1341,
        1350,
        1400,
        1450,
        1490
        ]

I = [
        1.124,
        1.119,
        1.109,
        1.100,
        1.074,
        1.052,
        1.024,
        0.992,
        0.956,
        0.912,
        0.867,
        0.817,
        0.762,
        0.701,
        0.642,
        0.576,
        0.513,
        0.424,
        0.345,
        0.289,
        0.221,
        0.173,
        0.089,
        0.061,
        0.034,
        0.016,
        0.008,
        0.0048,
        0.0053,
        0.0115,
        0.026,
        0.042
       ]

print len(U)
print len(I)
xnew = np.linspace(-1, 1489, 500)
smooth = spline(U, I, xnew)
plt.plot(xnew, smooth, label="Spline curve")
plt.scatter(U, I, marker='x', color='black', s=50,label="Data points")
plt.xlabel("U / V")
plt.ylabel("I / mW")
plt.legend()
plt.show()
