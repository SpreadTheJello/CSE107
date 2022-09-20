# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Create a grayscale image of size 100 rows x 256 columns in which the value of each row varies  from  0  in  the  left  column  to  255  in  the  right  column.  Thus,  the  image  contains  a  grayscale gradient from black on the left to white on the right.
img_gray_pixels = np.zeros(shape=(100, 256))
rows, cols = img_gray_pixels.shape
for row in range(0, rows):
    for col in range(0, cols):
        img_gray_pixels[row,col] = col

# Create an image from the new matrix.
img_gray = Image.fromarray(np.uint8(img_gray_pixels))

# Display the image on the screen.
img_gray.show()

# Save the image as a .tif file.
img_gray.save("Gradient.tif")

# Compute the average pixel value of the gradient image. You must use nested for loops to do this. You are not allowed to use any built-in functions to compute the average.
sum = 0
for row in range(rows):
    for col in range(cols):
        sum = sum + int(img_gray_pixels[row][col])
avg = sum / (cols*rows)
print("avg pixel value of gradient image: " + str(avg))

# Questions for task 3: 
# 1. What is the average pixel value in your gradient image?
# - 127.5
# 2. Why did you expect to get this value from the gradient image?
# - This value was expected because there are 0-255 values and since we're doing an incremental value in each column, we can expect our average to be 255/2.
# 3. What was the most difficult part of this task? 
# - Remembering to do -1 since pixels go up to 255 not 256.