#A program to converts an image into a sepia tone

from PIL import Image #You must have Pillow installed to run this code
im = Image.open("/Users/jeremiahbanks/Documents/Coding/Python/thinkCSpy3/Chapter_8/LutherBellPic.jpg")

def sepia(image):
    for row in range(image.height):
        for col in range(image.width):
            p = image.getpixel((col, row))
            
            """The formula for creating a sepia tone is as follows:
			newR = (R × 0.393 + G × 0.769 + B × 0.189)
			newG = (R × 0.349 + G × 0.686 + B × 0.168)
			newB = (R × 0.272 + G × 0.534 + B × 0.131)"""
            new_red = int((p[0] * 0.393 + p[1] * 0.769 + p[2] * 0.189))
            new_green = int((p[0] * 0.349 + p[1] * 0.686 + p[2] * 0.168))
            new_blue = int((p[0] * 0.272 + p[1] * 0.534 + p[2] * 0.131))
            
            new_pixel = (new_red, new_green, new_blue)
            
            image.putpixel((col, row), new_pixel)


sepia(im)

im.show() 



