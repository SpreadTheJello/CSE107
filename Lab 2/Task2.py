# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Import Inverse Function
import MyImageFunctions

# Read the image “Watertower.tif”
img = Image.open('Watertower.tif')

# Display the image on the screen.
img.show()

# Create a numpy matrix that has the pixel values from the image. 
img_pixels = asarray(img)
rows, cols = img_pixels.shape

# Call  the  function  myImageInverse()
inverse_img_pixels = MyImageFunctions.myImageInverse(img_pixels)

# What is the maximum pixel value of your inverse image?
max = inverse_img_pixels[0,0]
for row in range(rows):
    for col in range(cols):
        if(inverse_img_pixels[row,col] > max):
            max = inverse_img_pixels[row,col]
print("max pixel value of inverse image: " + str(max))

# How is this maximum value related to the values of the original image?
max = img_pixels[0,0]
for row in range(rows):
    for col in range(cols):
        if(img_pixels[row,col] > max):
            max = img_pixels[row,col]
print("max pixel value of original image: " + str(max))


# Create an image from the returned matrix.
inverse_img = Image.fromarray(np.uint8(inverse_img_pixels))

# Display the image on the screen.
inverse_img.show()

# Write the image to a .tif file.
inverse_img.save("Watertower_inverse.tif")

# Questions for task 2: 
# 1. What is the maximum pixel value of your inverse image?
# - 255
# 2. How is this maximum value related to the values of the original image?
# - The max value to the orginal image is also 255. Even though the pixel values are changing, we're still relatively keeping the same values just inversed, so anything pure black is now the highest value and anything pure white is now the lowest value.
# 3. What was the most difficult part of this task? 
# - Writing a comment to the method header I find to be more tedious than difficult; but otherwise respectively easy.
