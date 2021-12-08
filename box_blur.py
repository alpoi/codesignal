# The pixels in the input image are represented as integers. 
# The algorithm distorts the input image in the following way: 
# Every pixel x in the output image has a value equal to the 
# average value of the pixel values from the 3 × 3 square that 
# has its center at x, including x itself. All the pixels on 
# the border of x are then removed. Return the blurred image 
# as an integer, with the fractions rounded down.

from math import floor

def solution(im):
    return[[floor((im[x - 1][y - 1] + im[x][y - 1] + im[x + 1][y - 1] +   \
                   im[x - 1][y]     + im[x][y]     + im[x + 1][y]     +   \
                   im[x - 1][y + 1] + im[x][y + 1] + im[x + 1][y + 1])/9) \
                   for y in range(1, len(im[0]) - 1)] 
                   for x in range(1, len(im) - 1)   ]

# passed all tests
# can be improved with slices