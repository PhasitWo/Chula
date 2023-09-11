from PIL import Image
from PIL.Image import Image as IMG

img = Image.open("ImageProcessing/assign2/assignment2_image1.jpg")
print(img.getpixel((img.width-1, img.height-1)))
