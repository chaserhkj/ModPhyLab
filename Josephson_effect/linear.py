from scipy import stats

x = [-4 ,-3, -2, -1, 0, 1, 2, 3, 4]
y = [-0.58,-0.16,0.26,0.66,1.08,1.48,1.88,2.28,2.68]

k,b,r,p,s = stats.linregress(x, y)
print "k = ", k
print "b = ", b
print "r = ", r
