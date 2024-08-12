"""upper_pixel = original_image.getpixel((399, abs(243 - 1))) #abs() is added to create exception for first pixel, so it doesn't try to grab a pixel that doesn't exist
print(upper_pixel)

if 243 != 243: #if column < column
    lower_pixel = original_image.getpixel((399, 243 + 1))
if 243 >= 243: #elif column >= column
    lower_pixel = original_image.getpixel((399, 243 -1)) #creates an exception for the final pixel, so it doesn't try to grab a pixel that doesn't exist
print(lower_pixel)

#left_pixel = original_image.getpixel((abs(399 - 1), 243))
#print(left_pixel)
#if 399 < 399: #if row < row
    #right_pixel = original_image.getpixel((399 + 1, 243))
#elif 399 >= 399: #elif row >= row
    #right_pixel = original_image.getpixel((399-1, 243))
#print(right_pixel)"""


from PIL import Image

original_image = Image.open("/Users/jeremiahbanks/Documents/Coding/Python/thinkCSpy3/Chapter_8/LutherBellPic.jpg")

column = int(input("What column do you want to test? (0-399) "))
row = int(input("What row do you want to test? (0-243) "))

upper_pixel = original_image.getpixel((column, abs(row - 1))) #abs() added to create exception for first pixel, so it doesn't try to grab a pixel that doesn't exist
lower_pixel = original_image.getpixel((column, abs(row - 1))) 
if column < column: #if statement creates an exception for the final pixel, so it doesn't try to grab a pixel that doesn't exist
    lower_pixel = original_image.getpixel((column, row + 1)) #All lower_pixel(s) until final pixel are written as variable outside of loop then rewritten inside of loop. Any more efficient way to do this?
left_pixel = original_image.getpixel((abs(column - 1), row))
right_pixel = original_image.getpixel((abs(column - 1), row))
if row < row:
    right_pixel = original_image.getpixel((column + 1, row))

print(upper_pixel)
print(lower_pixel)
print(left_pixel)
print(right_pixel)

"""upper_pixel = original_image.getpixel((399, abs(243 - 1))) #abs() is added to create exception for first pixel, so it doesn't try to grab a pixel that doesn't exist
print(upper_pixel)
lower_pixel = original_image.getpixel((399, 243 -1))
if 243 < 243:
    lower_pixel = original_image.getpixel((399, 243 + 1))
print(lower_pixel)
left_pixel = original_image.getpixel((abs(399 - 1), 243))
print(left_pixel)
right_pixel = original_image.getpixel((399-1, 243))
if 399 < 399:
    right_pixel = original_image.getpixel((399 + 1, 243))
print(right_pixel)"""