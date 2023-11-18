import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb
import skimage
import random
from queue import Queue

file_path = "ImageProcessing/project/sample1.jpg"
diff = [0.139, 0.06, 0.06]
img = imread(file_path) 
new_img = img.copy()
img = rgb2hsv(img)
height, width, _ = img.shape
rh = random.randint(0, height-1)
rw = random.randint(0, width-1)
# grow
q = Queue()
# 2059, 889
# 1830, 1300
q.put((400, 400))
print(img[2059, 889])
print(img[2074, 870])
neighbor_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
visited = [[False for _ in range(width)] for _ in range(height)]
cnt = 0
max_cnt = 50_000
while(not q.empty()):
    i, j = q.get()
    visited[i][j] = True
    center = img[i, j]
    growed = False
    for offset in neighbor_offset:
        x, y = i+offset[0], j+offset[1]
        if x < 0 or x > height-1 or y < 0 or y > width-1 or visited[x][y]:
            continue
        neighbor = img[x, y]
        # criteria
        in_cube = True
        for k in range(3):
            if abs(center[k]-neighbor[k]) > (diff[k]):
                in_cube = False
                break
        if in_cube:
            visited[x][y] = True
            growed = True
            cnt += 1
            new_img[x,y] = (0,255,0)
            q.put((x, y))
    if cnt > max_cnt-1:
        break
print(cnt)
new_img = skimage.util.img_as_ubyte(new_img)
# img = hsv2rgb(img)
plt.imshow(new_img)
plt.show()