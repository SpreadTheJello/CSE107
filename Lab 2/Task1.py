# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Read the image “Beginnings.jpg”.
img = Image.open('Beginnings.jpg')

# Display the image on the screen.
img.show()

# Convert the image from color to grayscale.
img_gray = ImageOps.grayscale(img)

# Display the image on the screen again.
img_gray.show()

# Create a numpy matrix that has the pixel values from the image.
img_gray_pixels = asarray(img_gray)
rows, cols = img_gray_pixels.shape
# print(img_gray_pixels)

# Use nested for loops to compute the maximum pixel value in the numpy matrix and print this value out to the terminal. Note, you cannot use any built-in functions to compute the maximum—you must loop through the pixel values.
max = img_gray_pixels[0,0]
for row in range(rows):
    for col in range(cols):
        if(img_gray_pixels[row,col] > max):
            max = img_gray_pixels[row,col]
print("max pixel value: " + str(max))

# Create a new numpy matrix which is the original matrix rotated by 90 degrees 
# counterclockwise.  The  Beginnings  grayscale  image  should  have  dimensions  800  (rows) x 
# 533  (columns).  Your  new  matrix  should  have  dimensions  533  x  800  (but  don’t  hardcode  
# these  values—use  the  number  of  rows  and  columns  of  the  Beginnings  grayscale  image). 
# Steps to do this: 
# - Create a new blank numpy matrix. 
# - Use nested for loops to copy the pixel values from the original matrix image to 
# the counterclockwise rotated one.
rows, cols = img_gray_pixels.shape
img_gray_pixels_rotated_CCW = np.zeros(shape=(cols, rows))
for col in range(0, cols):
    for row in range(0, rows):
        img_gray_pixels_rotated_CCW[col][row] = img_gray_pixels[row][col]

# Create an image from the rotated matrix.
img_gray_rotated_CCW = Image.fromarray(np.uint8(img_gray_pixels_rotated_CCW))

# Display the counterclockwise rotated image on the screen.
img_gray_rotated_CCW.show()

# Write the counterclockwise rotated image to a file.
img_gray_rotated_CCW.save("Beginnings_grayscale_rotated_CCW.jpg")

# Create a new numpy matrix which is the original matrix rotated by 90 degrees clockwise.
rows, cols = img_gray_pixels.shape
img_gray_pixels_rotated_CW = np.zeros(shape=(cols, rows))
for col in range(0, cols):
    for row in range(0, rows):
        img_gray_pixels_rotated_CW[col][row] = img_gray_pixels[rows-row-1][cols-col-1]

# Create an image from the rotated matrix.
img_gray_rotated_CW = Image.fromarray(np.uint8(img_gray_pixels_rotated_CW))

# Display the counterclockwise rotated image on the screen.
img_gray_rotated_CW.show()

# Write the counterclockwise rotated image to a file.
img_gray_rotated_CW.save("Beginnings_grayscale_rotated_CW.jpg")

# Compute and print the maximum pixel value of the clockwise rotated image. Again, you must compute the maximum value yourself using nested for loops.
max = img_gray_pixels_rotated_CW[0,0]
rows, cols = img_gray_pixels_rotated_CW.shape
for row in range(rows):
    for col in range(cols):
        if(img_gray_pixels_rotated_CW[row,col] > max):
            max = img_gray_pixels_rotated_CW[row,col]
print("max pixel value of clockwise rotated image: " + str(int(max)))

# Questions for task 1: 
# 1. What is the maximum pixel value of your grayscale Beginnings image? 
# - 240
# 2. What is the maximum pixel value of your clockwise rotated grayscale image? 
# - 240
# 3. Should these be the same? Why or why not? 
# - They should be the same since none of the pixel values were changed, only the position changed. 
# 4. What was the most difficult part of this task? 
# - Figuring out how to rotate the image with a nested loop rather than using the numpy.rot90() function.