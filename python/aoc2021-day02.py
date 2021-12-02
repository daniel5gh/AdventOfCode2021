import itertools
from collections import defaultdict

import common

__author__ = 'Daniël'
input = common.read_input('02')
moves = [(x.split()[0], int(x.split()[1])) for x in input]

def part1():
    totals = defaultdict(int)
    for direction, magnitude in moves:
        totals[direction] += magnitude
    depth = totals['down'] - totals['up']
    print(totals['forward'] * depth)


def part2():
    depth = 0
    horizontal_position = 0
    aim = 0
    for direction, magnitude in moves:
        if direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude
        elif direction == 'forward':
            horizontal_position += magnitude
            depth += aim * magnitude
    print(horizontal_position * depth)


def part2better():
    """Using structural pattern matching of python 3.10
    """

    depth = 0
    horizontal_position = 0
    aim = 0
    for direction, magnitude in moves:
        match direction:
            case 'down':
                aim += magnitude
            case 'up':
                aim -= magnitude
            case 'forward':
                horizontal_position += magnitude
                depth += aim * magnitude
    print(horizontal_position * depth)



if __name__=='__main__':
    print(len(moves))
    part1()
    part2better()
