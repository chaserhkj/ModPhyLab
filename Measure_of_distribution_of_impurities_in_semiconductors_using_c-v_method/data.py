from PIL import Image

xscale = 9.0 / ( 2795 - 613)
yscale = 106.0 / ( 2190 - 360)
x0 = 613
y0 = 2190

ystart = 2150

start = 625
end = 2795
step = 10

im = Image.open("data.png")
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

x = start
while x < end:
    y = ystart
    while pixels[y][x][3] == 0:
        y = y - 1
    print '{0},{1}'.format((x - x0) * xscale,  (y0 - y) * yscale)
    x = x + step


