#A program to converts an image into grayscale 

from PIL import Image #You must have Pillow installed to run this code
im = Image.open("/Users/jeremiahbanks/Documents/Coding/Python/thinkCSpy3/Chapter_8/LutherBellPic.jpg")

def grayscale(image):
    for row in range(image.height):
        for col in range(image.width):
            p = image.getpixel((col, row))
            
            """From lesson: You can create a gray scale pixel by averaging the red, green 
            and blue intensities and then using that value for all intensities."""
            average_intensity = (p[0] + p[1] + p[2]) // 3
            new_red = average_intensity
            new_green = average_intensity
            new_blue = average_intensity
            
            new_pixel = (new_red, new_green, new_blue)
            
            image.putpixel((col, row), new_pixel)


grayscale(im)

im.show() 

