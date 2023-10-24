import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

LOWPASS = 0
HIGHPASS = 1
def notch_filter(img_path, radius, type_=0):
    img = imread(img_path)
    height, width= img.shape[0], img.shape[1]
    centroid_x = int((height + 1)/2 - 1)
    centroid_y = int((width + 1)/2 - 1)
    r = pow(radius, 2)
    transformed_channels = []
    fig, ax = plt.subplots(1,3,figsize=(15,5))
    for i in range(3):
        img_fourier = np.fft.fftshift(np.fft.fft2(img[:,:,i]))
        for x in range(height):
            for y in range(width):
                dist = pow(x - centroid_x, 2) + pow(y - centroid_y, 2)
                if type_ == LOWPASS:
                    if dist > r:
                        img_fourier[x, y] = 1
                elif type_ == HIGHPASS:
                    if dist < r:
                        img_fourier[x, y] = 1
        transformed_channels.append(abs(np.fft.ifft2(img_fourier)))
    final_image = np.dstack([
        transformed_channels[0].astype(int), 
        transformed_channels[1].astype(int), 
        transformed_channels[2].astype(int)])
    # matpotlib Figure
    t = "lowpass" if type_ == 0 else "highpass"
    fig.suptitle(f'{t} Radius:{radius}', fontsize=16)
    ax[0].imshow(img)
    ax[0].set_title('Original Image', fontsize=15)
    ax[1].imshow((np.log(abs(img_fourier))), cmap="gray")
    ax[1].set_title('Masked Fourier (blue channel)', fontsize=15)
    ax[2].imshow(final_image)
    ax[2].set_title('Transformed Image', fontsize = 15)
    file_name = img_path.strip(".jpg").split()[-1]
    plt.savefig(f'{file_name}_notch_{t}{radius}')

# MAIN
if __name__ == '__main__':
    for r in [10, 50, 100]:
        notch_filter('ImageProcessing/assign4/fruit.jpg', radius = r, type_ = LOWPASS)
        notch_filter('ImageProcessing/assign4/fruit.jpg', radius = r, type_ = HIGHPASS)
