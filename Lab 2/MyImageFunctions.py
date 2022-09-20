# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

def myImageInverse(inImage):
    # This function takes in a numpy matrix of grayscale image pixels and 
    # outputs another numpy matrix of grayscale image pixels that is inverse 
    # 
    # Syntax: 
    # out_matrix = myImageInverse(in_matrix)
    #
    # Input:
    # in_matrix = the grayscale pixel values of the input image
    #
    # History:
    # A. Fatali 9/26/22 Created
    rows, cols = inImage.shape
    outImage = np.zeros(shape=(rows, cols))    
    for row in range(0, rows):
        for col in range(0, cols):
            outImage[row][col] = 255-inImage[row][col]

    return outImage