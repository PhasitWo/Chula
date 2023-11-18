import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb
import skimage
import random
from queue import Queue

file_path = "ImageProcessing/project/sample2.jpg"
diff = [0.1, 0.2, 0.2]
img = imread(file_path) 
img = rgb2hsv(img)
height, width, _ = img.shape
visited = [[False for _ in range(width)] for _ in range(height)]
for m in range(height):
    for n in range(width):
        if img[m, n].all() == 0:
            continue
        # grow
        q = Queue()
        # 2059, 889
        # 1830, 1300
        q.put((m, n))
        neighbor_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
        cnt = 0
        max_cnt = 50_000
        zum = [0, 0, 0]
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
                    for u in range(3):
                        zum[u] += neighbor[u]
                    # new_img[x,y] = (0,255,0)
                    q.put((x, y))
            if cnt > max_cnt-1:
                break
        # slice
        if cnt > max_cnt-1:
            avg = tuple(value/cnt for value in zum)
            print(avg)
            for x in range(height):
                for y in range(width):
                    r = img[x, y]
                    in_cube = True
                    for k in range(3):
                        if abs(avg[k]-r[k]) > (diff[k]):
                            in_cube = False
                            break
                    if in_cube:
                        img[x, y] = (0, 0, 0)

img = hsv2rgb(img)
plt.imshow(img)
plt.show()