import itertools

import common

__author__ = 'Daniël'
input = list(map(int, common.read_input('01', 2020)))


def part1():
    for x, y in itertools.permutations(input, r=2):
        if x+y == 2020:
            print(x*y)
            break


def part2():
    for x, y, z in itertools.permutations(input, r=3):
        if x+y+z == 2020:
            print(x*y*z)
            break


if __name__=='__main__':
    part1()
    part2()
