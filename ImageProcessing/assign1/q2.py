from PIL import Image
from PIL.Image import Image as IMG

def enhance(image:IMG):
    image = image.convert("L") # convert to gray scale
    max_level = 255 # max gray scale value of this image (255 for 8 bit)
    for x in range(image.height): # height
        for y in range(image.width): # width
            r = image.getpixel((y,x))
            if r < (max_level/3):
                s = 5*max_level/6
            elif r < (2*max_level/3):
                s = (-2 * r) + (9 * max_level /6)
            else:
                s = max_level/6
            image.putpixel((y,x), round(s))
    image.save(f"ImageProcessing/assign1/q2/tram-ENHANCE.jpg")

img = Image.open("ImageProcessing/assign1/sample/tram.jpg")
enhance(img)