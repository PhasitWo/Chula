from PIL import Image
from PIL.Image import Image as IMG

def local_histogram_equalize(image:IMG, neighbor_width, neighbor_height):
    image = image.convert("L") # convert to gray scale
    new_image = Image.new("L", (image.width, image.height))
    clamp = lambda n, upper_bound: max(min(upper_bound, n), 0) # prevent image coordinate out of bound
    MAX_X = image.height - 1
    MAX_Y = image.width - 1
    def local(coordinate:tuple, neighbor_width, neighbor_height):
        x = coordinate[0]
        y = coordinate[1]
        x_upper = clamp(round(x + (neighbor_height-1)/2), MAX_X)
        x_lower = clamp(round(x - (neighbor_height-1)/2), MAX_X)
        y_upper = clamp(round(y + (neighbor_width-1)/2), MAX_Y)
        y_lower = clamp(round(y - (neighbor_width-1)/2), MAX_Y)
        # compute Hk
        Hk = [0 for _ in range(256)]
        pixel_cnt = 0
        for x in range(x_lower, x_upper+1):
            for y in range(y_lower, y_upper+1):
                r = image.getpixel((y,x))
                Hk[r] += 1
                pixel_cnt += 1
        print(Hk)
        # compute Pk from Hk
        Pk = [h/pixel_cnt for h in Hk]
        Sk = [0 for _ in range(256)]
        # compute Sk
        Sk[0] = Pk[0]
        old_value = image.getpixel((y,x))
        for i in range(1, old_value + 1): # exclude i = 0, no need to compute
            Sk[i] = Sk[i-1] + Pk[i]
        print([round(s*255) for s in Sk])
        # convert new_value to 256 gray level
        new_value = round(Sk[old_value] * 255)
        # apply to image
        new_image.putpixel((y,x), new_value)

    # driver
    # statistical conditions for finding the right spot to enhance 
    # TODO
    # local((x,y), neighbor_width, neighbor_height)
    # new_image.show()
    # new_image.save(f"ImageProcessing/assign2/q3_output.jpg")
    local((40,40), 7, 7)

    # image.save(f"ImageProcessing/assign2/q2_output.jpg")


img = Image.open("ImageProcessing/assign2/assignment2_image1.jpg")
local_histogram_equalize(img, 7, 7)