import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
import skimage

def invert_image(img_path):
    image = imread(img_path)
    image = skimage.util.invert(image)
    file_name = img_path.strip(".jpg").split("/")[-1]
    imsave(f"ImageProcessing/assign5/output/{file_name}_inverted.jpg",image)
    plt.imshow(image)
    plt.show()

invert_image("ImageProcessing/assign5/fruit.jpg")
