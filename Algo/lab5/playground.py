import matplotlib.pyplot as plt

def draw_polygon(points:list, triangles:list, diagonals:list):
    points.append(points[0])
    xs, ys = zip(*points) #create lists of x and y values
    plt.figure(figsize=(15, 8), dpi=80)
    for d in diagonals:
        i, j = zip(*d)
        plt.plot(i, j, color="red", linestyle="dashed")
    plt.plot(xs,ys, color="blue")
    for p in points:
        plt.text(p[0], p[1], f"({p[0]},{p[1]})")
    plt.axis("off")
    plt.show()