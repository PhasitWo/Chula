from PIL import Image
from PIL.Image import Image as IMG

def displayCustomGrayLevel(image:IMG, levels:int):
    image = image.convert("L") # convert to grayscale
    max_level = 255 # max gray scale value of this image (255 for 8 bit)
    new_level = levels - 1 # new max gray scale value
    for x in range(image.height): # height
        for y in range(image.width): # width
            old = image.getpixel((y,x))
            new = (round(old/max_level * new_level))/new_level*max_level
            image.putpixel((y,x), round(new))
    image.save(f"ImageProcessing/assign1/q1/fruit{levels}levels.jpg")


img = Image.open("ImageProcessing/assign1/sample/fruit.jpg")
displayCustomGrayLevel(img, 4)
displayCustomGrayLevel(img, 64)
displayCustomGrayLevel(img, 128)
displayCustomGrayLevel(img, 256)
