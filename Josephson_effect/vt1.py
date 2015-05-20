from matplotlib import pyplot as plt

x = []
y = []

with open('data2.txt') as f:
    line = f.readline()
    while line:
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
        line = f.readline()
y = [i/50 for i in y]
plt.xlabel("I/mA")
plt.ylabel("U/$\mu$V")
plt.plot(x, y)
plt.savefig("vt1.pdf")
plt.show()

