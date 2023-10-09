mask = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

sample_img = [
    [1,1,1],
    [1,1,1],
    [1,2,1],
    [1,1,1]
]
new_img = [row[:] for row in sample_img]  # deep copy

mask_height = len(mask)
mask_width = len(mask[0])
mask_hspan = int((mask_height - 1)/2)
mask_wspan = int((mask_width - 1)/2)
mask_center_x = int((mask_height + 1)/2 - 1) # - 1 for converting to index
mask_center_y = int((mask_width + 1)/2 - 1)
img_height = len(sample_img)
img_width = len(sample_img[0])
# map sample coordinate to mask coordinate
for x in range(mask_hspan, img_height - mask_hspan):
    for y in range(mask_wspan, img_width - mask_wspan):
        # offset : find offset by center of mask and current x,y
        offset_x = x - mask_center_x
        offset_y = y - mask_center_y
        # apply
        res = 0
        for i in range(len(mask)):
            for j in range(len(mask[0])):
                res += mask[i][j] * sample_img[i+offset_x][j+offset_y]
        new_img[x][y] = res
    
for row in new_img:
    print(row)