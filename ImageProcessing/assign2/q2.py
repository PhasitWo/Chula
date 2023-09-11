from PIL import Image
from PIL.Image import Image as IMG

def global_histogram_equalize(image:IMG):
    Hk = [0 for _ in range(256)]
    image = image.convert("L") # convert to gray scale
    # compute Hk
    for x in range(image.height):
        for y in range(image.width):
            r = image.getpixel((y,x))
            Hk[r] += 1
    # compute Pk from Hk
    pixel_cnt = image.height * image.width
    Pk = [h/pixel_cnt for h in Hk]
    Sk = [0 for _ in range(256)]
    # compute Sk
    Sk[0] = Pk[0]
    for i in range(1, 256): # exclude i = 0, no need to compute
        Sk[i] = Sk[i-1] + Pk[i]
    # convert Sk to 256 gray level
    Sk = [round(s*255) for s in Sk]
    # apply to image
    for x in range(image.height):
        for y in range(image.width):
            r = image.getpixel((y,x))
            image.putpixel((y,x), Sk[r])
    image.save(f"ImageProcessing/assign2/q2_output.jpg")


img = Image.open("ImageProcessing/assign2/assignment2_image1.jpg")
global_histogram_equalize(img)