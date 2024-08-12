#A program to converts an image to black and white

from PIL import Image #You must have Pillow installed to run this code
im = Image.open("/Users/jeremiahbanks/Documents/Coding/Python/thinkCSpy3/Chapter_8/LutherBellPic.jpg")

def black_and_white(image):
    grayscale_image = Image.new("RGB", image.size, (255, 255, 255))
    
    for row in range(image.height):
        for col in range(image.width):
            p = image.getpixel((col, row))
            
            """From lesson: You can create a gray scale pixel by averaging the red, green 
            and blue intensities and then using that value for all intensities."""
            average_intensity = (p[0] + p[1] + p[2]) // 3
            new_red = average_intensity
            new_green = average_intensity
            new_blue = average_intensity
            
            """From the gray scale you can create black white by setting a threshold and 
            selecting to either insert a white pixel or a black pixel into the empty 
            image."""
            
            new_pixel = (new_red, new_green, new_blue) 
            
            grayscale_image.putpixel((col, row), new_pixel)
    
    blackwhite_image = Image.new("RGB", image.size)
    for row in range(image.height):
        for col in range(image.width):
            p = grayscale_image.getpixel((col, row))
            red_threshold = p[0]
            if red_threshold > 128:
                bw_value = 255
            else:
                bw_value = 0
            
            new_pixel = (bw_value, bw_value, bw_value)
            blackwhite_image.putpixel((col, row), new_pixel)
    return blackwhite_image
    

bw_im = black_and_white(im)

bw_im.show() 

