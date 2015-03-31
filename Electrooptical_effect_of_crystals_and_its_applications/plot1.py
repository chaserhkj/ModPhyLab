# encoding=utf8
from matplotlib import pyplot as plt
from scipy.interpolate import spline
import numpy as np

U = [
        -300,
        -250,
        -200,
        -150,
        -100,
        -50,
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
        1350,
        1400,
        1450,
        1488
        ]

I = [
        0.0665,
        0.0509,
        0.0377,
        0.0296,
        0.0249,
        0.0234,
        0.028,
        0.031,
        0.035,
        0.044,
        0.056,
        0.071,
        0.089,
        0.113,
        0.142,
        0.178,
        0.218,
        0.267,
        0.315,
        0.366,
        0.437,
        0.500,
        0.574,
        0.637,
        0.710,
        0.776,
        0.840,
        0.916,
        0.978,
        1.038,
        1.124,
        1.166,
        1.192,
        1.133,
        1.124,
        1.114,
        1.109
       ]

xnew = np.linspace(-300, 1480, 500)
smooth = spline(U, I, xnew)
plt.plot(xnew, smooth, label="Spline curve")
plt.scatter(U, I, marker='x', color='black', s=50,label="Data points")
plt.xlabel("U / V")
plt.ylabel("I / mW")
plt.legend(loc="upper left")
plt.show()
