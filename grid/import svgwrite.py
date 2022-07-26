import svgwrite
import math
import random

grid = []
for i in range(0,10):
    grid.append([])
    for j in range (0,10):
        grid[i].append({ "x" : i, "y" : j })

dwg = svgwrite.Drawing('test.svg', size=(500, 500), profile='tiny')
for i in grid:
    for j in grid[i]:
        print(j)
dwg.saveas("grid_warp_0_0.svg")