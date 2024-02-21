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
    if apply_filter == 1:
        kernel = get_gaussian_kernel()
    elif apply_filter == 2:
        x=input("height:")
        x=int(x)
        y=input("width:")
        y=int(y)
        kernel = get_mean_kernel(x,y)
        center_x=int(input("kernel center_x:"))
        center_y=int(input("kernel_center_y:"))
        b1, g1, r1 = cv2.split(img)
        b1 = convolution("blue",b1, kernel,center_x,center_y)
        g1 = convolution("green",g1 , kernel,center_x,center_y)
        r1 = convolution("red",r1 , kernel,center_x,center_y)
        merged = cv2.merge((b1, g1, r1))
        print(b1)
        cv2.imshow("merged", merged)
        
        
        
    elif apply_filter == 3:
        kernel = get_laplacian_kernel()
    elif apply_filter == 4:
        kernel = get_log_kernel()
    elif apply_filter == 5:
        kernel = get_sobel_kernel()
    else:
        print("Invalid filter code.")
    print(kernel)
    cv2.imshow("lenna",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


#Convolution Code 

def convolution(s,img,kernel,p,q):
    k = kernel.shape[0] // 2
    l = kernel.shape[1] // 2
    padding_bottom = kernel.shape[0] - 1 - p
    padding_right = kernel.shape[1] - 1 - q
    img_bordered = cv2.copyMakeBorder(src=img, top=p, bottom=padding_bottom, left=q, right=padding_right,borderType=cv2.BORDER_CONSTANT)
    out = img_bordered.copy()
    # cv2.imshow('bordered image', img_bordered)

    for i in range(p, img_bordered.shape[0] - padding_bottom - k):
        for j in range(q, img_bordered.shape[1] - padding_right - l):
            res = 0
            for x in range(-k, k + 1):
                for y in range(-l, l + 1):
                    res += kernel[x + k, y + l] * img_bordered[i - x, j - y]
            out[i, j] = res    

    cv2.normalize(out, out, 0, 255, cv2.NORM_MINMAX)
    out = np.round(out).astype(np.uint8)
    print(f"normalized {out}") 
    out = out[p: -padding_bottom, q:-padding_right]
    cv2.imshow(s, out)       
    return out
    
    
    
    
    
#definition of smoothing filters 

def get_gaussian_kernel():
    
    return gaussian_kernel

def get_mean_kernel(height,width):
    mean_kernel= np.ones((height,width),dtype=np.float32)
    mean_kernel = mean_kernel / (height * width)
    return mean_kernel

def get_laplacian_kernel():
    
    return laplacian_kernel

def get_log_kernel():
    # Implement LoG kernel generation here
    return log_kernel

def get_sobel_kernel():
    # Implement Sobel kernel generation here
    return sobel_kernel














if __name__ == "__main__":
    main()



