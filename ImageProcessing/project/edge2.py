import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
import skimage
from scipy.signal import find_peaks
import numpy as np

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
        cnt = 0
        for y in range(1, width):
            if img[x,y] == 0:
                continue
            if img[x, y-1] == 1:
                continue
            else:
                cnt += 1
        horizons.append(cnt)

    horizons = np.array(horizons)
    max_ = max(horizons)
    horizons = np.array([int(v/max_*100) for v in horizons]) # normalize
    hpeaks, hinfo = find_peaks(horizons, distance=hdistance, height=min_hheight)
    print(hpeaks)
    print(hinfo["peak_heights"])

    x1 = max(hpeaks[0]-padding, 0)
    x2 = min(hpeaks[-1]+padding, img.shape[0])

    img = img[x1:x2, : ]

    verticals = []
    for y in range(width):
        cnt = 0
        for x in range(1, img.shape[0]):
            if img[x, y] == 0:
                continue
            if img[x-1, y] == 1:
                continue
            else:
                cnt += 1
        verticals.append(cnt)

    verticals = np.array(verticals)
    max_ = max(verticals)
    verticals = np.array([int(v/max_*100) for v in verticals]) # normalize
    vpeaks, vinfo = find_peaks(verticals, distance=vdistance, height=min_vheight)
    print(vpeaks)
    print(vinfo["peak_heights"])

    new_img = original_img[x1:x2, max(vpeaks[0]-padding, 0):min(vpeaks[-1]+padding, img.shape[1])]

    fig, ax = plt.subplots(2,2,figsize=(15,8))
    ax[0][0].imshow(img)
    ax[0][1].imshow(new_img)
    ax[1][0].plot(horizons)
    ax[1][0].plot(hpeaks, horizons[hpeaks], "x")
    ax[1][0].title.set_text("horizon")
    ax[1][1].plot(verticals)
    ax[1][1].plot(vpeaks, verticals[vpeaks], "x")
    ax[1][1].title.set_text("vertical")
    plt.show()
    return new_img

# Driver code
original = imread("ImageProcessing/project/sample3.jpg")
img = extract_brand(original, hdistance=2, min_hheight=50, vdistance=2 , min_vheight=50, padding=-5)
# img = extract_brand(img, hdistance=100, min_hheight=30, vdistance=50 , min_vheight=30, padding=100)
# this params work with 3 samples





# import pickle
# with open("ImageProcessing/project/pickleY", "rb") as file:
#     verticals = pickle.load(file)
# with open("ImageProcessing/project/pickleX", "rb") as file:
#     horizons = pickle.load(file)
# fig, ax = skimage.filters.try_all_threshold(img, figsize=(10, 8), verbose=False)