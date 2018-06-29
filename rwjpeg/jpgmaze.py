from PIL import Image
import numpy as np

# 1维是图片高  2维是图片宽

inimg = "D:/red.jpg"
optxt = "D:/1.txt"

im = np.array(Image.open(inimg).convert('L'))

vslice = 10
hslice = 10

v_pixel = im.shape[0]
h_pixel = im.shape[1]

row_id = 0
col_id = 0

row_maze = int(v_pixel / vslice + 1)
col_maze = int(h_pixel / hslice + 1)

mazemat = np.zeros((row_maze, col_maze), dtype=int)

_wall = 2
_space = 1
_ground = 0

for v in range(0, v_pixel, vslice):
    for h in range(0, h_pixel, hslice):
        boxv = im[v:v + vslice, h:h + hslice].mean()
        if boxv < 200:
            mazemat[row_id, col_id] = _ground
        else:
            mazemat[row_id, col_id] = _space
        print(str(row_id) + " " + str(col_id))
        col_id += 1
    row_id += 1
    col_id = 0

with open(optxt, 'w', encoding='utf-8') as f:
    for v in range(1, row_maze - 1):
        for h in range(1, col_maze - 1):
            if mazemat[v, h] == _ground:
                if mazemat[v - 1, h] == _space:
                    mazemat[v - 1, h] = _wall
                if mazemat[v + 1, h] == _space:
                    mazemat[v + 1, h] = _wall
                if mazemat[v, h - 1] == _space:
                    mazemat[v, h - 1] = _wall
                if mazemat[v, h + 1] == _space:
                    mazemat[v, h + 1] = _wall

    for v in range(0, row_maze):
        for h in range(0, col_maze):
            f.write(str(mazemat[v, h]) + " ")
        f.write('\n')
