import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

LOWPASS = 0
HIGHPASS = 1
def notch_reject_filter(img_path, radius, params_array:list[tuple]):
    img = imread(img_path)
    radius_sqr = pow(radius, 2)
    height, width= img.shape[0], img.shape[1]
    fig, ax = plt.subplots(1,4,figsize=(17,7), dpi=100)
    img_fourier = np.fft.fftshift(np.fft.fft2(img))
    ax[1].imshow(np.log(abs(img_fourier)), cmap="gray")
    ax[1].set_title('Fourier', fontsize = 15)
    for u0, v0 in params_array:
        for u in range(height):
            for v in range(width):
                d1 = pow(u-(height/2)-u0, 2) + pow(v-(width/2)-v0, 2)
                d2 = pow(u-(height/2)+u0, 2) + pow(v-(width/2)+v0, 2)
                if d1 <= radius_sqr or d2 <= radius_sqr:
                    h = 0
                else:
                    h = 1
                img_fourier[u, v] *= h
          
    final_image = abs(np.fft.ifft2(img_fourier))
    # matpotlib Figure
    title = f'Notch Reject radius:{radius}\nu0,v0 = {params_array}'
    fig.suptitle(title, fontsize=16)
    ax[0].imshow(img, cmap="gray")
    ax[0].set_title('Original Image', fontsize=15)
    # avoid log(0)
    img_fourier_log = np.ma.log(abs(img_fourier))
    img_fourier_log = img_fourier_log.filled(img_fourier_log.min()) 
    ax[2].imshow(img_fourier_log, cmap="gray")
    ax[2].set_title('Masked Fourier', fontsize=15)
    ax[3].imshow(final_image, cmap="gray")
    ax[3].set_title('Transformed Image', fontsize = 15)
    file_name = img_path.strip(".jpg").split()[-1]
    plt.savefig(f'{file_name}_notchReject_{radius}')
    plt.show()
# MAIN
if __name__ == '__main__':
    notch_reject_filter("ImageProcessing/assign4/Noisy_flower1_horizontal.jpg", 30, [(70, 0), (140, 0)])