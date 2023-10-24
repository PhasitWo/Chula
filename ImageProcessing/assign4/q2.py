import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

LOWPASS = 0
HIGHPASS = 1
def gaussian_filter(img_path, cutoff, type_=0):
    img = imread(img_path)
    cutoff_sqr = pow(cutoff, 2)
    height, width= img.shape[0], img.shape[1]
    centroid_x = int((height + 1)/2 - 1)
    centroid_y = int((width + 1)/2 - 1)
    transformed_channels = []
    fig, ax = plt.subplots(1,3,figsize=(15,5))
    for i in range(3): # RGB channels
        img_fourier = np.fft.fftshift(np.fft.fft2(img[:,:,i]))
        for x in range(height):
            for y in range(width):
                dist_sqr = pow(x - centroid_x, 2) + pow(y - centroid_y, 2)
                h = pow(math.e, -1*dist_sqr/(2*cutoff_sqr))
                if type_ == LOWPASS:
                    img_fourier[x, y] *= h   
                elif type_ == HIGHPASS:
                    img_fourier[x, y] *= (1-h)      
        transformed_channels.append(abs(np.fft.ifft2(img_fourier)))
    final_image = np.dstack([
        transformed_channels[0].astype(int), 
        transformed_channels[1].astype(int), 
        transformed_channels[2].astype(int)])
    # matpotlib Figure
    t = "lowpass" if type_ == 0 else "highpass"
    fig.suptitle(f'Gaussian {t} cutoff:{cutoff}', fontsize=16)
    ax[0].imshow(img)
    ax[0].set_title('Original Image', fontsize=15)
    # avoid log(0)
    img_fourier_log = np.ma.log(abs(img_fourier))
    img_fourier_log = img_fourier_log.filled(img_fourier_log.min()) 
    ax[1].imshow(img_fourier_log, cmap="gray")
    ax[1].set_title('Masked Fourier (blue channel)', fontsize=15)
    ax[2].imshow(final_image)
    ax[2].set_title('Transformed Image', fontsize = 15)
    file_name = img_path.strip(".jpg").split()[-1]
    plt.savefig(f'{file_name}_gaussian_{t}{cutoff}')
    plt.show()
# MAIN
if __name__ == '__main__':
    for r in [10, 50, 100]:
        gaussian_filter('ImageProcessing/assign4/flower1.jpg', cutoff = r, type_ = LOWPASS)
        gaussian_filter('ImageProcessing/assign4/flower1.jpg', cutoff = r, type_ = HIGHPASS)
