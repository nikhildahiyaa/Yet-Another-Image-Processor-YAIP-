# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Archita Srivastava - 301455231 and Nikhil Dahiya - 301449046
# Date: 6 December 2021
# Description:  Here we have defined all the functions for doing manipulation to the provided images and these functions will be called in main.py.
# Also this module will be imported in the main.py.



import cmpt120imageProjHelper
import numpy


# Apply Red Filter – Retains the R values of all pixels in the image, and sets G and B to zero
def applyRedfilter(pixels):

    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            pixel = pixels[row][col]
            r = pixel[0]
            pixels[row][col] = [r,0,0]
    return pixels



#Apply Blue Filter – Retains the B values of all pixels in the image, and sets R and G to zero.
def applyBluefilter(pixels):
    
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            pixel = pixels[row][col]
            b = pixel[2]
            pixels[row][col] = [0,0,b]
    return pixels



#Apply Green Filter – Retains the G values of all pixels in the image, and sets R and B to zero.
def applyGreenfilter(pixels):
    
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            pixel = pixels[row][col]
            g = pixel[1]
            pixels[row][col] = [0,g,0]
    return pixels



#Apply Sepia Filter – Gives all colours with warm brownish tone. The sepia colour for a pixel is calculated by a weighted average of the original R/G/B values 

def applySepiafilter(pixels):
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            pixel = pixels[row][col]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            Sepia_r = int((red * 0.393) + (green * 0.769) + (blue * 0.189))
            Sepia_g = int((red * 0.349) + (green * 0.686) + (blue * 0.168))
            Sepia_b = int((red * 0.272) + (green * 0.534) + (blue * 0.131))

            red = min([255, Sepia_r])
            green = min([255, Sepia_g])
            blue = min([255, Sepia_b])

            if red > 0 and green > 0 and blue > 0:
                pixels[row][col] = [red, green, blue]
    return pixels



#Apply Warm Filter – Gives all colours with a warm tone. The warm colour of a pixel is calculated by scaling the original R value up and B value down using this formula:

def applyWarmfilter(pixels):
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            pixel = pixels[row][col]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if red < 64:
                warm_red = red / 64 * 84
            elif 64 < red < 128:
                warm_red = (red - 64) / (128 - 64) * (160 - 80) + 80
            else:
                warm_red = (red - 128) / (255 - 128) * (255 - 160) + 160

            if blue < 64:
                warm_blue = blue / 64 * 50
            elif 64 < blue < 128:
                warm_blue = (blue - 64) / (128 - 64) * (100 - 50) + 50
            else:
                warm_blue = (blue - 128) / (255 - 128) * (255 - 100) + 100

            if red > 0 and green > 0 and blue > 0:
                pixels[row][col] = [warm_red, green, warm_blue]
    return pixels



#Apply Cold Filter – Gives all colours with a cold tone. The cold colour of a pixel is calculated by scaling the original R value down and B value up using the same formula for the warm filter.
def applyColdfilter(pixels):
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            pixel = pixels[row][col]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if blue < 64:
                warm_blue = blue / 64 * 84
            elif 64 < blue < 128:
                warm_blue = (blue - 64) / (128 - 64) * (160 - 80) + 80
            else:
                warm_blue = (blue - 128) / (255 - 128) * (255 - 160) + 160

            if red < 64:
                warm_red = red / 64 * 50
            elif 64 < red < 128:
                warm_red = (red - 64) / (128 - 64) * (100 - 50) + 50
            else:
                warm_red = (red - 128) / (255 - 128) * (255 - 100) + 100

            if red > 0 and green > 0 and blue > 0:
                pixels[row][col] = [warm_red, green, warm_blue]
    return pixels



# Double size – Double both width and height (so the size is actually 4 times as before)
def doubleSize(pixels):
    black = cmpt120imageProjHelper.getBlackImage(len(pixels[0])*2, len(pixels)*2)
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            new_row = row*2
            new_col = col*2
            black[new_row][new_col] = pixels[row][col]
            black[new_row+1][new_col] = pixels[row][col]
            black[new_row][new_col+1] = pixels[row][col]
            black[new_row+1][new_col+1] = pixels[row][col]
    return black



#Half Size – Half both width and height (so the size is actually 1/4 as before).
def halfSize(pixels):
    black = cmpt120imageProjHelper.getBlackImage(int(len(pixels[0]) * 0.5), int(len(pixels) * 0.5))
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            new_row = int(row * 0.5)
            new_col = int(col * 0.5)
            black[new_row][new_col] = pixels[row][col]
            black[new_row -1][new_col] = pixels[row][col]
            black[new_row][new_col - 1] = pixels[row][col]
            black[new_row - 1][new_col - 1] = pixels[row][col]
    return black



#Rotate left – Rotates the image counter-clockwise by 90 degrees
def rotateLeft(pixels):
    black = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))
    for row in range(len(pixels[0])):
        for col in range(len(pixels)):
            black[row][col] = pixels[col][-row-1]
    return black



#Rotate Right – Rotates the image clockwise by 90 degrees
def rotateRight(pixels):
    black = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))
    for row in range(len(pixels[0])):
        for col in range(len(pixels)):
            black[row][col] = pixels[-col-1][row]
    return black


# using isYellow function in locateFish function
def isYellow(r, g, b):
    hsv = cmpt120imageProjHelper.rgb_to_hsv(r, g, b)
    # hue
    if 45 <= hsv[0] <= 60:
        # saturation
        if 40 <= hsv[1] <= 70:
            # value
            if 85 <= hsv[2] <= 100:
                return True
    else:
        return False

#Locate Fish
def locateFish(pixels):
    black = cmpt120imageProjHelper.getBlackImage(len(pixels[0]), len(pixels))

    # box
    top, bottom, left, right = len(pixels), 0, len(pixels[0]), 0
  
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            r = pixels[row][col][0]
            g = pixels[row][col][1]
            b = pixels[row][col][2]
            # copy paste pixels to black
            black[row][col] = [r, g, b]
            if isYellow(r, g, b) == True:
                black[row][col] = pixels[row][col]
                if (row < top):
                    top = row # top of the box
                if(row > bottom):
                    bottom = row # bottom of box
                if(col < left): 
                    left = col # left side of box
                if(col > right): 
                    right = col # right side of box
    # Draw box
    for col in range(left, right + 1):
        black[top][col] = [0, 255, 0]    # top line
        black[bottom][col] = [0, 255, 0] # bottom line
    for row in range(top, bottom + 1):
        black[row][left] = [0, 255, 0]   # left line
        black[row][right] = [0, 255, 0]  # right line

    return black