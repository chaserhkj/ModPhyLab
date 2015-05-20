from PIL import Image

xscale = 5.0 / 100
yscale = 10.0 / 100
x0 = 1638
y0 = 1543

ystart = 1885

start = 600
end = 2645
step = 5

im = Image.open("data3.png")
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

x = start
while x < end:
    y = ystart
    while pixels[y][x][3] <  200:
        y = y - 1
    print '{0},{1}'.format((x - x0) * xscale,  (y0 - y) * yscale)
    x = x + step


