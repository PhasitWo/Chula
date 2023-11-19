import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
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
        for y in range(width):
            if img[x, y] == 1:
                cnt += 1
        horizons.append(cnt)

    verticals = []
    for y in range(width):
        cnt = 0
        for x in range(height):
            if img[x, y] == 1:
                cnt += 1
        verticals.append(cnt)

    horizons = np.array(horizons)
    hpeaks, hinfo = find_peaks(horizons, distance=hdistance, height=min_hheight)
    print(hpeaks)
    print(hinfo["peak_heights"])

    verticals = np.array(verticals)
    vpeaks, vinfo = find_peaks(verticals, distance=vdistance, height=min_vheight)
    print(vpeaks)
    print(vinfo["peak_heights"])

    new_img = original_img[hpeaks[0]-padding:hpeaks[-1]+padding, vpeaks[0]-padding:vpeaks[-1]+padding]
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
img = imread("ImageProcessing/project/sample2.jpg")
img = extract_brand(img, hdistance=100, min_hheight=400, vdistance=100 , min_vheight=50, padding=-100)
img = extract_brand(img, hdistance=20, min_hheight=300, vdistance=50 , min_vheight=50, padding=200)


# import pickle
# with open("ImageProcessing/project/pickleY", "rb") as file:
#     verticals = pickle.load(file)
# with open("ImageProcessing/project/pickleX", "rb") as file:
#     horizons = pickle.load(file)

# fig, ax = skimage.filters.try_all_threshold(img, figsize=(10, 8), verbose=False)