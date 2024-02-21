# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:58:58 2024

@author: Asus
"""

import numpy as np
import cv2
import math

def main():
    print("Assignment 1")
    color_mode = input("Enter the colormode \n RGB(1) \n GRAY(0) :")
    color_mode = int(color_mode)
    img = cv2.imread(r"D:\4.1\image lab\sonjoy image\Image_Processing\2k19_labfiles\Assignment\assignment of lab1\Lena.jpg",color_mode)
    img = cv2.resize(img, (500,500))
    apply_filter_str = input("Enter the filter code \n Smoothing Filter: \n 1. Gaussian Filter\n 2. Mean Filter \n Sharpening Filter :\n 3. Laplacian Filter \n 4. LoG  \n 5. Sobel filter  : ")
    apply_filter = int(apply_filter_str)
    cv2.imshow("lenna",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


#Convolution Code 

def convolution(img,kernel):
    for()
    
    
#definition of smoothing filters 

#1. MEAN filter1
def mean_filter(height,weidth):
    kernel= np.ones((height,weidth))/height*width
    
    return kernel















if __name__ == "__main__":
    main()



