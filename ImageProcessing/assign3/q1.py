from PIL import Image
from PIL.Image import Image as IMG

def averaging_filter(img:IMG) -> IMG:
    mask = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ]
    constant = len(mask) * len(mask[0])
    filename = img.filename.strip(".jpg")
    img = img.convert("L") # convert to gray scale
    new_img = img.copy() # copy img to new_img
    mask_height = len(mask)
    mask_width = len(mask[0])
    mask_hspan = int((mask_height - 1)/2)
    mask_wspan = int((mask_width - 1)/2)
    mask_center_x = int((mask_height + 1)/2 - 1) # - 1 for converting to index
    mask_center_y = int((mask_width + 1)/2 - 1)
    # map sample coordinate to mask coordinate
    for x in range(mask_hspan, img.height - mask_hspan):
        for y in range(mask_wspan, img.width - mask_wspan):
            # offset : find offset by center of mask and current x,y
            offset_x = x - mask_center_x
            offset_y = y - mask_center_y
            # apply
            res = 0
            for i in range(len(mask)):
                for j in range(len(mask[0])):
                    res += mask[i][j] * img.getpixel((j+offset_y, i+offset_x))
            res = round(res/constant)
            new_img.putpixel((y, x), res)
    new_img.save(f"{filename}_avg.jpg")
    return new_img

# Averaging Filter Driver Code
img = Image.open("ImageProcessing/assign3/noisy_img2.jpg")
new_img = averaging_filter(img)
new_img.show()


def median_filter(img:IMG) -> IMG:
    mask = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ]
    filename = img.filename.strip(".jpg")
    img = img.convert("L") # convert to gray scale
    new_img = img.copy() # copy img to new_img
    mask_height = len(mask)
    mask_width = len(mask[0])
    mask_hspan = int((mask_height - 1)/2)
    mask_wspan = int((mask_width - 1)/2)
    mask_center_x = int((mask_height + 1)/2 - 1) # - 1 for converting to index
    mask_center_y = int((mask_width + 1)/2 - 1)
    # map sample coordinate to mask coordinate
    for x in range(mask_hspan, img.height - mask_hspan):
        for y in range(mask_wspan, img.width - mask_wspan):
            # offset : find offset by center of mask and current x,y
            offset_x = x - mask_center_x
            offset_y = y - mask_center_y
            # apply
            lst = []
            for i in range(len(mask)):
                for j in range(len(mask[0])):
                    lst.append(img.getpixel((j+offset_y, i+offset_x)))
            lst.sort()
            median_index = round((len(lst) + 1)/2 - 1)
            res = lst[median_index]
            new_img.putpixel((y, x), res)
    new_img.save(f"{filename}_median.jpg")
    return new_img

# Median Filter Driver Code
# img = Image.open("ImageProcessing/assign3/noisy_img2.jpg")
# new_img = median_filter(img)
# new_img.show()