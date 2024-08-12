#IN PROGRESS- A program that doubles the size of an image
from PIL import Image #You must have Pillow installed to run this code
im = Image.open("/Users/jeremiahbanks/Documents/Coding/Python/thinkCSpy3/Chapter_8/LutherBellPic.jpg")

def double_size(image):
    doubled_width = image.width * 2
    doubled_height = image.height * 2
    #Creates a new image instance to fill with original image data
    doubled_image = Image.new("RGB", (doubled_width, doubled_height))
    for row in range(image.height):
       	for column in range(image.width):
       	    p = image.getpixel((column, row))
       	    
       	    doubled_image.putpixel((2*column, 2*row), p)
       	    doubled_image.putpixel((2*column + 1, 2*row), p)
       	    doubled_image.putpixel((2*column, 2*row + 1), p)
       	    doubled_image.putpixel((2*column + 1, 2*row + 1), p)
    
    return doubled_image
            	
big_img = double_size(im)

big_img.show()