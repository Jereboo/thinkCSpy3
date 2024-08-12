#A program to remove all red from an image 

from PIL import Image #You must have Pillow installed to run this code
im = Image.open("/Users/jeremiahbanks/Documents/Coding/Python/thinkCSpy3/Chapter_8/LutherBellPic.jpg")

def remove_red(image):
    for row in range(image.height):
        for col in range(image.width):
            p = image.getpixel((col, row))
            
            no_red = p[0]- p[0]
            original_green = p[1]
            original_blue = p[2]
            
            new_pixel = (no_red, original_green, original_blue)
            
            image.putpixel((col, row), new_pixel)


remove_red(im)

im.show()