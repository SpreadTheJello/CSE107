import numpy as np
import math

# Write the functionmyimresize() that takes as input
# A numpy matrix representing a grayscale image.
# The number of rows in the resized image.
# The number of columns in the resized image.
# A string with values ‘nearest’ or ‘bilinear’.
# and outputs the resized numpy matrix image.
# Based off the TA's sample file
def myImageResize(inImage_pixels, M, N, interpolation_method ):

    Minput, Ninput = inImage_pixels.shape
    # create a new output matrix
    out = np.zeros(shape=(M, N))

    for m in range(M+1):  # int
        for n in range(N+1):   # int
            # loop  all the pixels from the out

            # 1. we estimate the index of input image -> estimate row and col
            m_inter = (((m-0.5)/M) * Minput) + 0.5   # float number,
            n_inter = (((n-0.5)/N) * Ninput) + 0.5

            if interpolation_method == 'nearest':
                # use nn
                # round()
                m_inter = round(m_inter)
                n_inter = round(n_inter)
                # print("m_inter: ", m_inter)
                # print("n_inter: ", n_inter)
                out[m-1, n-1] = inImage_pixels[m_inter-1, n_inter-1]
            
            elif interpolation_method == 'bilinear':
                # use the bilinear

                # find the 4 points
                # use the if else from the hw
                # m_inter -> m1, m2  which are the nearest row index
                if(m_inter == int(m_inter)):
                    m1 = m_inter-1
                    m2 = m_inter-1
                else:
                    if m_inter < 1:
                        m1, m2 = 1, 2
                    elif m_inter > Minput-1:
                        m1, m2 = Minput-2, Minput-1
                    else:
                        m1 = math.floor(m_inter-1)
                        m2 = math.ceil(m_inter-1)

                # n_inter -> n1, n2  which are the nearest col index
                if(n_inter == int(n_inter)):
                    n1 = n_inter-1
                    n2 = n_inter-1
                else:
                    if n_inter < 1:
                        n1, n2 = 1, 2
                    elif n_inter > Ninput-1:
                        n1, n2 = Ninput-2, Ninput-1
                    else:
                        n1 = math.floor(n_inter-1)
                        n2 = math.ceil(n_inter-1)

                p1 = inImage_pixels[m1, n1]
                p2 = inImage_pixels[m1, n2]
                p3 = inImage_pixels[m2, n1]
                p4 = inImage_pixels[m2, n2]
                p5 = 0

                p5 = mybilinear(m1,n1,p1,m1,n2,p2,m2,n1,p3,m2,n2,p4,m_inter-1,n_inter-1,p5)
                out[m-1, n-1] = p5
                
    
    return out

def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5,p5):
    # use eq from hw
    # apply eq on p1 and p3  -> t1
    # apply eq on p2 and p4  -> t2
    # ....        t1 and t2  -> p5

    p5_prime = (p3-p1)*((x5-x1)/(x3-x1))+p1
    p5_doubleprime = (p4-p2)*((x5-x2)/(x4-x2))+p2
    p5 = (p5_doubleprime-p5_prime)*((y5-y1)/(y2-y1))+p5_prime
    return p5

def myRMSE(first_im_pixels, second_im_pixels):

    total = 0
    M,N = first_im_pixels.shape
    for m in range(0,M):
        for n in range(0,N):
            total += (first_im_pixels[m,n] - second_im_pixels[m,n])**2

    # now you have sum
    total = total / (M * N)

    return math.sqrt(total)
