# MyHEFunctions.py

# Import numpy
import numpy as np

# Write the functioncompute_histogram() that takes a numpy matrix 
# representing a grayscale image as input and outputs a length 256 
# numpy vector representing the normalized histogram of the image.
def compute_histogram( image_pixels ):
    # compute_histogram  Computes the normalized histogram of a 
    # grayscale image.
    #
    # Syntax:
    #   hist = compute_histogram( image_pixels )
    #
    # Input:
    #   image_pixels = The grayscale image as a numpy matrix.
    #
    # Output:
    #   hist = The 256 numpy vector representing a normalized 
    #   histogram.
    #
    # History:
    #   F. Angelo     11/13/2022   created

    # Create a length 256 vector of zeros.
    hist = np.zeros(shape=(256))

    # Loop through all the pixels in the image.
    for x in range(image_pixels.shape[0]):
        for y in range(image_pixels.shape[1]):
            # Increment the histogram bin corresponding to the pixel value.
            hist[int(image_pixels[x][y])] += 1

    # Normalize the histogram.
    hist = hist / np.sum(hist)

    return hist




# Write the function equalize() that takes a numpy matrix 
# representing a grayscale image as input and outputs a numpy 
# matrix representing the histogram equalized version of the 
# image. 
def equalize( in_image_pixels ):
    # equalize  Takes in as input a grayscale image 256 bits and returns 
    # the histogram equalized version.
    #
    # Syntax:
    #   eq_pixels = equalize( in_image_pixels )
    #
    # Input:
    #   in_image_pixels = The grayscale image as a numpy matrix.
    #
    # Output:
    #   eq_img = The equalized grayscale image as a numpy matrix.
    #
    # History:
    #   F. Angelo     11/13/2022   created

    # Get the histogram of the input image.
    hist = compute_histogram( in_image_pixels )

    # Compute the cumulative distribution function.
    cdf = np.cumsum( hist )

    # Normalize the cdf.
    cdf = (256-1) * cdf / cdf[-1]

    # Use linear interpolation of cdf to find new pixel values.
    equalized_image = np.interp(in_image_pixels.flatten(), range(256), cdf)

    # Reshape the equalized image.
    eq_img = equalized_image.reshape(in_image_pixels.shape)

    return eq_img


def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/23/2022   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()
