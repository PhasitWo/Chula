import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb


def prewitt_filter(file_path):
    maskX = [
    [-1,0,1],
    [-1,0,1],
    [-1,0,1]
    ]
    maskY = [
    [-1,-1,-1],
    [ 0, 0, 0],
    [ 1, 1, 1] 
    ]
    img = imread(file_path)
    new_img = img.copy()
    height, width, _ = img.shape
    mask_center_x = 1
    mask_center_y = 1
    mask_height = len(maskX)
    mask_width = len(maskX[0])
    mask_hspan = int((mask_height - 1)/2)
    mask_wspan = int((mask_width - 1)/2)
    for x in range(mask_hspan, height - mask_hspan):
        for y in range(mask_wspan, width - mask_wspan):
            # offset : find offset by center of mask and current x,y
            offset_x = x - mask_center_x
            offset_y = y - mask_center_y
            # apply
            r = 0; g = 0; b = 0
            for i in range(mask_height):
                for j in range(mask_width):
                    value = img[i+offset_x, j+offset_y]
                    r += maskX[i][j] * value[0]
                    g += maskX[i][j] * value[1]
                    b += maskX[i][j] * value[2]
            new_img[x, y] = (r, g, b)
    plt.imshow(new_img)
    plt.show()

prewitt_filter("ImageProcessing/project/sample1.jpg")