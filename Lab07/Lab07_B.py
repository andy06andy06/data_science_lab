import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import cv2
import math

# Do NOT modifify the function names

def fade_gradually(processed):
    processed = processed.copy()

    # TODO_B1
    change_ratio = np.linspace(1,0,processed.shape[1])
    processed = cv2.cvtColor(processed,cv2.COLOR_BGR2HSV)
    for i in range(processed.shape[0]):
        processed[i,:,1]=processed[i,:,1]*change_ratio
    processed = cv2.cvtColor(processed, cv2.COLOR_HSV2BGR)

    return processed


def image_matting(processed):
    processed = processed.copy()

    # TODO_B2
    processed = cv2.cvtColor(processed, cv2.COLOR_BGR2BGRA)
    for i in range(0,processed.shape[0]): 
        for j in range(0,processed.shape[1]): 
            if processed[i,j,0]<=10 and processed[i,j,1]<=10 and processed[i,j,2]<=10:
                processed[i,j,3] = 0

    return processed

def my_resize(img, height, width):
    processed = img.copy()
    # TODO_B3
    old_height, old_width, c = processed.shape
    resized = np.zeros((height, width, c))
    w_scale_factor = (old_width )/(width) if height!=0 else 0
    h_scale_factor = (old_height )/(height) if width!=0 else 0
    for i in range(height):
        for j in range(width):
            x = i*h_scale_factor
            y = j*w_scale_factor
            x_floor = math.floor(x)
            x_ceil = min( old_height-1, math.ceil(x))
            y_floor = math.floor(y)
            y_ceil = min(old_width-1, math.ceil(y))

            if (x_ceil==x_floor) and (y_ceil==y_floor):
                q = processed[int(x), int(y), :]
            elif (x_ceil==x_floor):
                q1 = processed[int(x), int(y_floor), :]
                q2 = processed[int(x), int(y_ceil), :]
                q = q1*(y_ceil-y) + q2 * (y-y_floor)
            elif (y_ceil==y_floor):
                q1 = processed[int(x_floor), int(y), :]
                q2 = processed[int(x_ceil), int(y), :]
                q = (q1*(x_ceil-x)) + (q2*(x-x_floor))
            else:
                v1 = processed[x_floor, y_floor, :]
                v2 = processed[x_ceil, y_floor, :]
                v3 = processed[x_floor, y_ceil, :]
                v4 = processed[x_ceil, y_ceil, :]

                q1 = v1*(x_ceil-x) + v2*(x-x_floor)
                q2 = v3*(x_ceil-x) + v4*(x-x_floor)
                q = q1*(y_ceil-y) + q2*(y-y_floor)

            resized[i,j,:] = q
    return resized.astype(np.uint8)
        

# You are incouraged to test your program in the main function

def main():
    monkey = cv2.imread('monkey_island.jpg') #(500,800,3)
    cat = cv2.imread('cat.jpg') #(829,949,3)
    cv2.imwrite('resultB1.jpg', fade_gradually(monkey))
    cv2.imwrite('resultB2.png', image_matting(cat))
    cv2.imwrite('resultB3.jpg', my_resize(cat, 600, 400))

if __name__ == "__main__":
    main()


