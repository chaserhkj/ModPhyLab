from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as ius
import numpy as np

x = []
y = []

rt = """70 17.224 75 19.337 80 21.464 85 23.598 90 25.731 95 27.861 100 29.984 105 32.101 110 34.209 115 36.311 120 38.404 125 40.491 130 42.569 135 44.641 140 46.706 145 48.765 150 50.818 155 52.865 160 54.906 165 56.942 170 58.973 175 61.000 180 63.022
185 65.041 190 67.055 195 69.066 200 71.073 205 73.076 210 75.076 215 77.072 220 79.065 225 81.054 230 83.039 235 85.021 240 86.998 245 88.972 250 90.943 255 92.911 260 94.875 265 96.836 270 98.795 273.15 100.027 275 100.750 280 102.703 285
104.654 290 106.601 295 108.546 300 110.487"""

rt = rt.split()
rt = [float(i) for i in rt]
t = rt[::2]
r = rt[1::2]

func = ius(r, t)


with open('data1.txt') as f:
    line = f.readline()
    while line:
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
        line = f.readline()
x = [i/0.9 for i in x]
y = [i/50e-3 for i in y]
x = [func(i) for i in x]
plt.xlabel("T/K")
plt.ylabel("R/$\Omega$")
plt.plot(x, y)
plt.savefig("rt1.pdf")
plt.show()

