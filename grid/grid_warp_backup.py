import svgwrite
import math
import random

i_length = 21
j_length = 21

def chaos_dampener(limit, num):
    half_limit = limit/2
    if num <= half_limit:
        return float(float(num) / float(half_limit))
    if num > half_limit:
        return float((float(limit) - float(num)) / float(half_limit))

grid = []
for i in range(0, i_length):
    grid.append([])
    for j in range (0, j_length):
        x_nudge = (random.random() - 0.5) * (10 * chaos_dampener(i_length-1, i) * chaos_dampener(j_length-1, j))**2
        y_nudge = (random.random() - 0.5) * (10 * chaos_dampener(i_length-1, i) * chaos_dampener(j_length-1, j))**2
        grid[i].append([i*25 + y_nudge, j*25 + x_nudge])

dwg = svgwrite.Drawing('test.svg', size=(500, 500), profile='tiny')
for i, row in enumerate(grid):
    for j, coords in enumerate(row):
        # print(coords)
        if j < j_length - 1:
            dwg.add(dwg.line(start=(coords[0], coords[1]), end=(grid[i][j+1][0], grid[i][j+1][1]), fill="none",stroke_width=0.5,stroke='black'))
            if i < i_length - 1:
                dwg.add(dwg.line(start=(coords[0], coords[1]), end=(grid[i+1][j][0], grid[i+1][j][1]), fill="none",stroke_width=0.5,stroke='black'))
        elif j < j_length:
            if i < i_length - 1:
                dwg.add(dwg.line(start=(coords[0], coords[1]), end=(grid[i+1][j][0], grid[i+1][j][1]), fill="none",stroke_width=0.5,stroke='black'))
dwg.saveas("grid_warp_2_2.svg")