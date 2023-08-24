from PIL import Image
from PIL.Image import Image as IMG

def enhancePowerLaw(image:IMG, c, gamma):
    image = image.convert("L") # convert to gray scale
    for x in range(image.height): # height
        for y in range(image.width): # width
            r = image.getpixel((y,x))
            s = c*pow(r, gamma)
            image.putpixel((y,x), round(s))
    image.save(f"ImageProcessing/assign1/q3/scenery2-PowerLaw-c{c}-y{gamma}.jpg")

img = Image.open("ImageProcessing/assign1/sample/scenery2.jpg")

c_arr = [0.5, 1, 2]
y_arr = [0.4, 2.5]

for c in c_arr:
    for y in y_arr:
        enhancePowerLaw(img, c, y)