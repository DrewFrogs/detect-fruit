import sys
import ntpath
import argparse

#image
import numpy as np
import cv2
import matplotlib
matplotlib.use("WXAgg")
from matplotlib import pyplot as plt

from itertools import product

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

#File handling/terminal input handling
#this will get the file from the terminal input
##create the arguemnt parse/parse the arguemnt
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
#load the entered image
#image = cv2.imread(args["image"])

##main function to list each step/process
def main():
    colourDetect()

#Colour Dectection
#Simple colour detection will be handled within this function.
def colourDetect():
    image = cv2.imread("./mytestimgs/organic-apples.jpg")
    plt.imshow(image)
    plt.show()





def example(r):
    #gray values
    gvalues = np.unique(r)

    #d=1 and q=horizontal or vertical
    h = np.zeros_like(r)
    v = np.zeros_like(r)

    for p in product(gvalues,gvalues):
        #horizontal
        for i in xrange(1,r.shape[0]+1):
            #avoid edges
            j = i-1 if ((i-1)>=0) else 0
            h[p[0],p[1]] += pairs(p,r[j:i])

        #vertical
        for i in xrange(1,r.shape[1]+1):
            #avoid edges
            j = i-1 if ((i-1)>=0) else 0
            v[p[0],p[1]] += pairs(p,r[:,i-1])
    print(h)
    print(v)

# "On-tree fruit recognition using texture properties and fruit"
# appendix 7
def pairs(p,arr):
    #count number of pairs
    count = 0
    #add useless columns for pair check
    arr = np.append(-1,arr)
    arr = np.append(arr,-1)
    for i in xrange(1,arr.shape[0]-1):
        #match adj pairs
        if arr[i] == p[0]:
            if arr[i-1] == p[1]:
                count += 1
            if arr[i+1] == p[1]:
                count += 1
    return count


#example
R = np.asarray([[0,0,1,1],[0,0,1,1],[0,2,2,2],[2,2,3,3]])
#example(R)


if __name__ == '__main__':
    main()
