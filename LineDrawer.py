import os
import PIL
from PIL import Image, ImageDraw

im = Image.open("testpic.png")
im2 = Image.new('RGBA', im.size, "black")
width, height = im.size
points = []
img2 = ImageDraw.Draw(im2)
for x in range(width):
    for y in range(height):
        r,g,b = im.getpixel((x, y))
        if((r+g+b) == 765):
            print(x, y)
            points.append([x, y])

for i in range(len(points)):
    for x in range(len(points)):
        print("Drawing:", [points[x][0], points[x][1]], "->",[points[x][0], points[x][1]])
        point = [(points[i][0], points[i][1]), (points[x][0], points[x][1])]
        img2.line(point, fill ="white", width = 0)

im2.save('lines.png')
im2.show()
