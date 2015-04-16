from matplotlib import pyplot as plt

u = []
c = []

with open('data.txt') as f:
    line = f.readline()
    while line:
        u.append(line.split(',')[0])
        c.append(line.split(',')[1])
        line = f.readline()

plt.xlabel("U/V")
plt.ylabel("C/pF")
plt.plot(u, c)
plt.savefig('uc.pdf')

