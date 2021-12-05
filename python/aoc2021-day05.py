import math

import numpy as np
import pandas as pd

import common

__author__ = 'Daniël'


lines = []
# input = common.read_input('05test')
input = common.read_input('05')
maxx = 0
maxy = 0
for line in input:
    p1, p2 = line.strip().split(' -> ')
    x1, y1 = list(map(int, p1.split(',')))
    x2, y2 = list(map(int, p2.split(',')))
    lines.append(((x1, y1), (x2, y2)))
    maxx = max(x1, maxx)
    maxx = max(x2, maxx)
    maxy = max(y1, maxy)
    maxy = max(y2, maxy)

assert maxx == maxy

maxx+=1
maxy+=1

def part1():
    grid = np.zeros(maxx * maxy).reshape(maxx, maxy)
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            r1 = min(y1, y2)
            r2 = max(y1, y2) + 1
            for y in range(r1, r2):
                grid[y][x1] += 1
        if y1 == y2:
            r1 = min(x1, x2)
            r2 = max(x1, x2) + 1
            for x in range(r1, r2):
                grid[y1][x] += 1

    print((grid > 1).sum())


def part2():
    grid = np.zeros(maxx * maxy).reshape(maxx, maxy)
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            r1 = min(y1, y2)
            r2 = max(y1, y2) + 1
            for y in range(r1, r2):
                grid[y][x1] += 1
        elif y1 == y2:
            r1 = min(x1, x2)
            r2 = max(x1, x2) + 1
            for x in range(r1, r2):
                grid[y1][x] += 1
        else:
            delta_x = x2 - x1
            delta_y = y2 - y1
            assert np.abs(delta_x) == np.abs(delta_y)
            steps = np.abs(delta_x)
            delta_x //= steps
            delta_y //= steps
            x = x1
            y = y1
            for step in range(steps+1):
                grid[y][x] += 1
                x += delta_x
                y += delta_y
    pass


    print((grid > 1).sum())

if __name__=='__main__':
    print(len(lines))
    part1()
    part2()
