
from PIL import Image

im = Image.open('images/mara_2.png')
pix = im.load()
width = im.size[0]
height = im.size[1]

for x in range(width):
    for y in range(height):
        r, g, b, a = im.getpixel((x,y))
        rgba = r, g, b, a

        if(0 < a < 255):
            im.putpixel((x,y),(0, 0, 0, 255))
            

im = im.convert('RGBA')
im.save('images/mara_3.png')