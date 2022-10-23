
def myImageResize( inImage_pixels, M, N, interpolation_method ):

    Minput, Ninput = inImage_pixels.shape
    # create a new output matrix
    out = np.zeros(shape=(M, N))

    for m in range(M+1):  # int
        for n in range(N+1):   # int
            # loop  all the pixels from the out

            # 1. we estimate the index of input image -> estimate row and col
            m_inter = (((m-0.5)/M) * Minput) + 0.5   # folat number,
            n_inter = (((n-0.5)/N) * Ninput) + 0.5

            # 1.2， 2.7
            # 300.5， 396.8

            if interpolation_method == 'nearest':
                # use nn
                # round()
                m_inter = round()
                n_inter = round()
                print("m_inter: ", m_inter)
                print("n_inter: ", n_inter)  # 100 x 175
                out[m-1, n-1] = inImage_pixels[]

            elif interpolation_method == 'bilinear':
                # use the bilinear

                # 1.2， 2.7
                # 300.5， 396.8

                # find the 4 points
                # use the if else from the hw
                # m_inter -> m1, m2  which are the nearest row index
                if m_inter < 1:
                    m1, m2 =
                elif m_inter > M_input:
                    m1, m2 =
                ...

                # n_inter -> n1, n2  which are the nearest col index
                if n_inter < 1:
                    n1, n2 =
                elif n_inter > N_input:
                    n1, n2 =
                ...

                m -> x
                n -> y
                p -> inImage_pixels[m_, n_]
                after you have m1, m2, n1, n2 -> 4 points
                p1, m1, n1
                p2, m1, n2
                p3, m2, n1
                p4, m2, n2
                m_inter, n_inter ----> p5

                print("x1, y1, p1: ", m1, n1, p1)
                print("x2, y2, p2: ", m1, n1, p1)
                ...
                print("x5, y5: ", m1, n1, p1)   1.2, 11.8  -> 1, 2  11,12

                p5 = mybilinear(m1,n1,p1,m2,n2,p2 ... )

                |  |
                |  |

                out[m-1, n-1] = p5

    return out



def myRMSE( first_im_pixels, second_im_pixels ):
    # I1, I2

    total = 0
    M,N = ..
    for m in M:
        for n in N:
            total += ...

    # now you have sum
    total = total / (M * N)

    return math.sqrt(total)


def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5):
    # use eq from hw
    # apply eq on p1 and p3  -> t1
    # apply eq on p2 and p4  -> t2
    # ....        t1 and t2  -> p5

    ...

    ...
    return p5
