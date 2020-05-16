#   Course: CS 2302
#   Assignment: Lab II
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 02/14/2020
#   Purpose of the Program: to identify the
#   brightest region in a solar image.

import numpy as np
import matplotlib.pyplot as plt
import os
import time as t

def read_image(imagefile):
    # Reads image in imagefile and returns color and gray-level images
    #
    img = (plt.imread(img_dir+file)*255).astype(int)
    img = img[:,:,:3]  # Remove transparency channel
    img_gl = np.mean(img,axis=2).astype(int)
    return img, img_gl

def integral_image(img):
    S = img.cumsum(axis=0).cumsum(axis=1)   # Creates an integral image.
    S = np.insert(S,0,0,axis=0)   # Adds a row of zeros into the array.
    S = np.insert(S,0,0,axis=1)   # Adds a column of zeros into the array.
    return S 

def integral_regions(S,h,w):
    m = len(S)
    n = len(S[0])
    A = S[:m-h,:n-w]   # First array (region) of size m by n
    B = S[:m-h,w:]    # Second array
    C = S[h:,:n-w]   # Third array
    D = S[h:,w:]   # Fourth array
    R = A-B-C+D   # We compute the sum of the entire image by accesing four arrays.
    return R

def display_img_and_rectangle(ax1,img,r,c,h,w):
    
    p0 = [r,c]   # Upper left corner point.
    p1 = [r,c+h]   # Upper right corner point.
    p2 = [r+w,c+h]   # Bottom right corner point.
    p3 = [r+w,c]   # Bottom left corner point.
    p = np.array([p0,p1,p2,p3,p0])   # Creates the given shape of size m by n.
    ax1.imshow(img)
    ax1.plot(p[:,0],p[:,1],linewidth=1.5,color='chartreuse')
    
def find_brightest_pixel(I):
    max_pix = 0
    for m in range(len(I)):
        for n in range(len(I)):
            if I[m][n] >= max_pix:
                max_pix = I[m][n]
                r = n
                c = m
    return r,c

def brightest_region_v11(ax,orig_img,gray_img,h,w):
    r = 0
    c = 0
    max_region = 0
    for m in range(0,len(gray_img)-h+1):   # for loop m moves the region vertically.   
        for n in range(0,len(gray_img)-w+1):   # for loop n moves the region horizontally.
            sum_region = 0
            for i in range(m,h+m):   # for loop i and j visits every element in
                for j in range(n,w+n):   # the region of size h by w.
                    sum_region += gray_img[i][j]
            if sum_region > max_region:
                max_region = sum_region
                r = n
                c = m
    display_img_and_rectangle(ax,orig_img,r,c,h,w)

def brightest_region_v12(ax,orig_img,gray_img,h,w):
    r = 0
    c = 0
    max_region = 0
    for m in range(0,len(gray_img)-h+1):
        for n in range(0,len(gray_img)-w+1):
            sum_region = np.sum(gray_img[m:m+h,n:n+w])   # Creates a 2D array (region),
            if sum_region > max_region:           # using slicing, of size h by w.
                max_region = sum_region
                r = n
                c = m
    display_img_and_rectangle(ax,orig_img,r,c,h,w)

def brightest_region_v21(ax,orig_img,gray_img,h,w):
    S = integral_image(gray_img)
    r = 0
    c = 0
    max_region = 0
    for m in range(0,len(S)-w):
        for n in range(0,len(S[0])-h):
            sum_region = S[m+w][n+h]-S[m][n+h]-S[m+w][n]+S[m][n]   # We compute the sum of the
            if sum_region > max_region:                 # current region by accesing four elements.
                max_region = sum_region
                r = n
                c = m
    display_img_and_rectangle(ax,orig_img,r,c,h,w)

def brightest_region_v22(ax,orig_img,gray_img,h,w):
    S = integral_image(gray_img)
    R = integral_regions(S,h,w)
    indices = np.argmax(R)   # We locate the position of the max element in R.
    r = indices%len(R)   # Operation to know the row index position of the max element.
    c = indices//len(R)   # Operation to know the column index position of the max element.
    display_img_and_rectangle(ax,orig_img,r,c,h,w)
    
img_dir = '.\\solar images\\' # Directory where imagea are stored

img_files = os.listdir(img_dir)  # List of files in directory

if __name__ == "__main__": 
    
    plt.close('all')
    
    sum_t = 0
    for file in img_files:
        #print(file)
        if file[-4:] == '.png': # File contains an image
            img, img_gl = read_image(img_dir+file)
            fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
        
            ax1.imshow(img)                  #Display color image
            ax2.imshow(img_gl,cmap='gray')   #Display gray-leval image
            
            plt.show()
            
            h = 100
            w = 100
            
            ''' 
            Uncomment to test each version of the method brightest_region()
            '''
            
            #print(find_brightest_pixel(img_gl))
            '''
            start = t.time()
            brightest_region_v11(ax1,img,img_gl,h,w)  # Uncomment to see Running Time of Version 1.1
            end = t.time()
            print(end-start)
            '''
            '''
            start = t.time()
            brightest_region_v12(ax1,img,img_gl,h,w) # Uncomment to see Running Time of Version 1.2
            end = t.time()
            print(end-start)
            '''
            '''
            start = t.time()
            brightest_region_v21(ax1,img,img_gl,h,w) # Uncomment to see Running Time of Version 2.1
            end = t.time()
            print(end-start)
            '''
            
            start = t.time()
            brightest_region_v22(ax1,img,img_gl,h,w)  # Uncomment to see Running Time of Version 2.2
            end = t.time()
            print(end-start)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        