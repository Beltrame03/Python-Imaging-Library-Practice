import os
import PIL
from PIL import Image, ImageDraw

class DrawLine():
    
    def __init__(self, picture):
        self.picture = Image.open(picture)

    def drawBetweenLines(self, RGBMIN, RGBMAX):
        im2 = Image.new('RGBA', self.picture.size, "black")
        width, height = self.picture.size
        points = []
        img1 = ImageDraw.Draw(self.picture)
        img2 = ImageDraw.Draw(im2)
        for x in range(width):
            for y in range(height):
                r,g,b = self.picture.getpixel((x, y))
                if(((r+g+b) <= RGBMAX) and ((r+g+b) >= RGBMIN)):
                    print([x, y])
                    print([r, g, b])
                    points.append([x, y])

        if(len(points) == 0):
            print("There is no points on the file that meet the RGBMIN of:", RGBMIN, "or RGBMAX:", RGBMAX)
            return

        for i in range(len(points)):
            for x in range(len(points)):
                print("Drawing:", [points[x][0], points[x][1]], "->",[points[x][0], points[x][1]])
                point = [(points[i][0], points[i][1]), (points[x][0], points[x][1])]
                img2.line(point, fill ="white", width = 0)
                img1.line(point, fill ="white", width = 0)

        im2.save('lines.png')
        im2.show()
        self.picture.show()
