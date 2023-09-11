from PIL import Image
from PIL.Image import Image as IMG

def enhancePowerLaw(image:IMG, c, gamma):
    image = image.convert("L") # convert to gray scale
    max_level = 255 # max gray scale value of this image (255 for 8 bit)
    max_transformed_value = pow(max_level, gamma)
    for x in range(image.height): # height
        for y in range(image.width): # width
            r = image.getpixel((y,x))
            s = c*pow(r, gamma)
            s = s/max_transformed_value * max_level # convert value back to 0-255 range
            image.putpixel((y,x), round(s))
    image.save(f"ImageProcessing/assign2/q1_output.jpg")

img = Image.open("ImageProcessing/assign2/assignment2_image1.jpg")
enhancePowerLaw(img, 1, 0.5)