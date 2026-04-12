import cv2
from skimage import io
import numpy as np
from skimage.filters.rank import mean
from skimage.morphology import square
from skimage.restoration import denoise_bilateral, denoise_wavelet, denoise_tv_chambolle
import matplotlib.pyplot as plt
from skimage import filters
from skimage.filters import threshold_local


def main():
    saturn = io.imread('Saturn.jpg')
    gray = cv2.cvtColor(saturn, cv2.COLOR_RGB2GRAY)
    

    saturn_denoised_A = mean(gray, square(3))
    saturn_denoised_B = cv2.GaussianBlur(gray, (5,5), 0)
    saturn_denoised_C = denoise_tv_chambolle(gray, weight=0.15)
    saturn_denoised_D = denoise_bilateral(gray, sigma_color=0.12, sigma_spatial=8)
    saturn_denoised_E = denoise_wavelet(gray)
    saturn_denoised_Z = denoise_tv_chambolle(cv2.GaussianBlur(saturn_denoised_D, (3,3),0), weight=0.05)

    fig = plt.figure(figsize=(11,7))
    ax1 = fig.add_subplot(2,3,1)
    ax1.imshow(saturn_denoised_A, cmap='gray')
    ax1.set_title('mean')
    ax2 = fig.add_subplot(2,3,2)
    ax2.imshow(saturn_denoised_B, cmap='gray')
    ax2.set_title('gaussian')
    ax3 = fig.add_subplot(2,3,3)
    ax3.imshow(saturn_denoised_C, cmap='gray')
    ax3.set_title('tv')
    ax4 = fig.add_subplot(2,3,4)
    ax4.imshow(saturn_denoised_D, cmap='gray')
    ax4.set_title('bilateral')
    ax5 = fig.add_subplot(2,3,5)
    ax5.imshow(saturn_denoised_E, cmap='gray')
    ax5.set_title('wavelet')
    ax6 = fig.add_subplot(2,3,6)
    ax6.imshow(saturn_denoised_Z, cmap='gray')
    ax6.set_title('final')

    plt.show()
    plt.imsave('resultC1.jpg', saturn_denoised_A, cmap='gray')
    plt.imsave('resultC2.jpg', saturn_denoised_B, cmap='gray')
    plt.imsave('resultC3.jpg', saturn_denoised_C, cmap='gray')
    plt.imsave('resultC4.jpg', saturn_denoised_D, cmap='gray')
    plt.imsave('resultC5.jpg', saturn_denoised_E, cmap='gray')
    plt.imsave('resultC_final.jpg', saturn_denoised_Z, cmap='gray')

if __name__ == "__main__":
    main()
    
    
