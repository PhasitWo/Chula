import pickle
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
import skimage
from scipy.signal import find_peaks
import numpy as np
from numpy import diff

def extract_brand(original_img, hdistance, min_hheight, vdistance, min_vheight, padding):
    img = rgb2gray(original_img)
    img = skimage.util.img_as_ubyte(img)
    footprint = skimage.morphology.square(10)
    img = skimage.filters.rank.mean(img, footprint)
    img = skimage.filters.prewitt(img)
    thresh = skimage.filters.threshold_otsu(img)
    img = img > thresh
    height, width = img.shape[0], img.shape[1]

    horizons = []
    for x in range(height):
        data = []
        for y in range(width):
            data.append(img[x, y])
        peaks, _ = find_peaks(data, distance=10, height=0.5)
        horizons.append(len(peaks))

    # verticals = []
    # for y in range(width):
    #     cnt = 0
    #     for x in range(height):
    #         if img[x, y] == 1:
    #             cnt += 1
    #     verticals.append(cnt)

    horizons = np.array(horizons)
    # max_ = max(horizons)
    # horizons = np.array([int(v/max_*100) for v in horizons]) # normalize
    # hpeaks, hinfo = find_peaks(horizons, distance=hdistance, height=min_hheight)
    # print(hpeaks)
    # print(hinfo["peak_heights"])

    # verticals = np.array(verticals)
    # max_ = max(verticals)
    # verticals = np.array([int(v/max_*100) for v in verticals]) # normalize
    # vpeaks, vinfo = find_peaks(verticals, distance=vdistance, height=min_vheight)
    # print(vpeaks)
    # print(vinfo["peak_heights"])

    # dx = [i for i in range(width-1)]
    # z = diff(horizons)/dx
    fig, ax = plt.subplots(1,2,figsize=(15,8))
    ax[0].plot(horizons)
    ax[1].imshow(img)
    plt.show()

# Driver code
original = imread("ImageProcessing/project/sample2.jpg")
img = extract_brand(original, hdistance=100, min_hheight=20, vdistance=100 , min_vheight=30, padding=-70)
# img = extract_brand(img, hdistance=100, min_hheight=30, vdistance=50 , min_vheight=30, padding=100)
# this params work with 3 samples





# import pickle
# with open("ImageProcessing/project/pickleY", "rb") as file:
#     verticals = pickle.load(file)
# with open("ImageProcessing/project/pickleX", "rb") as file:
#     horizons = pickle.load(file)
# fig, ax = skimage.filters.try_all_threshold(img, figsize=(10, 8), verbose=False)