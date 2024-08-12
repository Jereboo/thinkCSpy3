"""Task: After you have scaled an image too much it looks blocky. One way of reducing the
blockiness of the image is to replace each pixel with the average values of the pixels
around it. This has the effect of smoothing out the changes in color. Write a function 
that takes an image as a parameter and smooths the image. Your function should return 
a new image that is the same as the old but smoothed."""

"""A program that smooths an image out by averaging each pixel by its surrounding pixels 
(based on an original)"""

from PIL import Image

to_open = input("Please enter the path of the photo you want to enlarge and smooth: ")
original_image = Image.open(to_open)

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

def smoothed_img(image):
    new_image = Image.new("RGB", (image.width, image.height))
    for column in range(image.width):
        for row in range(image.height):        
            #Below code block finds values of surrounding pixels from current pixel
            upper_pixel = image.getpixel((column, abs(row - 1))) #abs() added to create exception for first pixel, so it doesn't try to grab a pixel that doesn't exist
            lower_pixel = image.getpixel((column, abs(row - 1)))
            if column < column: #if statement creates an exception for the final pixel, so it doesn't try to grab a pixel that doesn't exist
                lower_pixel = image.getpixel((column, row + 1)) #All lower_pixel(s) until final pixel are written as variable outside of loop then rewritten inside of loop. Any more efficient way to do this?
            left_pixel = image.getpixel((abs(column - 1), row))
            right_pixel = image.getpixel((abs(column - 1), row))
            if row < row:
                right_pixel = image.getpixel((column + 1, row))
            
            #Averages these values together and creates a new pixel for each color with this averaged value
            average_red = (upper_pixel[0] + lower_pixel[0] + left_pixel[0] + right_pixel[0]) // 4
            average_green = (upper_pixel[1] + lower_pixel[1] + left_pixel[1] + right_pixel[1]) // 4
            average_blue = (upper_pixel[2] + lower_pixel[2] + left_pixel[2] + right_pixel[2]) // 4
            new_pixel = (average_red, average_green, average_blue)
            
            #inserts this new_pixel into the proper column and row
            new_image.putpixel((column, row), new_pixel)
    
    return new_image

big_img = double_size(original_image)
big_img.show()

smoothed_image = smoothed_img(big_img)
smoothed_image.show()