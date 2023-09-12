from PIL import Image
from PIL.Image import Image as IMG
import math

def local_histogram_equalize(image:IMG, neighbor_width, neighbor_height, constants:tuple):
    image = image.convert("L") # convert to gray scale
    new_image = Image.new("L", (image.width, image.height))
    clamp = lambda n, upper_bound: max(min(upper_bound, n), 0) # prevent image coordinate out of bound
    MAX_X = image.height - 1
    MAX_Y = image.width - 1

    # global statistic
    Hk = [0 for _ in range(256)]
    for x in range(image.height):
        for y in range(image.width):
            r = image.getpixel((y,x))
            Hk[r] += 1
    Pk = [h/(image.height*image.width) for h in Hk]
    global_mean = sum([k*Pk[k] for k in range(256)])
    global_variance = sum([math.pow((k-global_mean), 2) * Pk[k] for k in range(256)])

    def histogram_equalize(coordinate:tuple, neighbor_width, neighbor_height, constants:tuple, global_mean, global_variance):
        x, y = coordinate
        k0, k1, k2 = constants
        x_upper = clamp(round(x + (neighbor_height-1)/2), MAX_X)
        x_lower = clamp(round(x - (neighbor_height-1)/2), MAX_X)
        y_upper = clamp(round(y + (neighbor_width-1)/2), MAX_Y)
        y_lower = clamp(round(y - (neighbor_width-1)/2), MAX_Y)
        # compute Hk
        Hk = [0 for _ in range(256)]
        pixel_cnt = 0
        for i in range(x_lower, x_upper+1):
            for j in range(y_lower, y_upper+1):
                r = image.getpixel((j,i))
                Hk[r] += 1
                pixel_cnt += 1

        # compute Pk from Hk
        Pk = [h/pixel_cnt for h in Hk]

        # local statistic
        local_mean = sum([k*Pk[k] for k in range(256)])
        local_variance = sum([math.pow((k-local_mean), 2) * Pk[k] for k in range(256)])

        # Conditions
        old_value = image.getpixel((y, x))
        if (local_mean < k0*global_mean) and (k1*global_variance <= local_variance) and (local_variance <= k2*global_variance):
            # compute Sk
            Sk = [0 for _ in range(256)]
            Sk[0] = Pk[0]
            for i in range(1, old_value + 1): # exclude i = 0, no need to compute
                Sk[i] = Sk[i-1] + Pk[i]

            # convert new_value to 256 gray level
            new_value = round(Sk[old_value] * 255)

            # # apply to image
            new_image.putpixel((y,x), new_value)

        else:
            new_image.putpixel((y,x), old_value)
        

    # driver
    for x in range(image.height):
        for y in range(image.width):
            histogram_equalize((x, y), neighbor_width, neighbor_height, constants, global_mean, global_variance)
    
    new_image.show()
    # new_image.save(f"ImageProcessing/assign2/q3_output.jpg")
   
img = Image.open("ImageProcessing/assign2/assignment2_image1.jpg")
local_histogram_equalize(img, 7, 7, (0.4, 0.001, 0.04))