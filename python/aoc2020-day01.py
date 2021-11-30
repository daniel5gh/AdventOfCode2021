import itertools
import logging

__author__ = 'Daniël'

import common


_log = logging.getLogger(__name__)
print = _log.info

input = list(map(int, common.read_input('01', 2020)))

def part1():
    for x, y in itertools.permutations(input, r=2):
        if x+y == 2020:
            print(x*y)


def part2():
    for x, y, z in itertools.permutations(input, r=3):
        if x+y+z == 2020:
            print(x*y*z)


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    part1()
    part2()
