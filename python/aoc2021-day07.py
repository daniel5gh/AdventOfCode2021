import common
from collections import defaultdict
import math

__author__ = 'Daniël'

input = common.read_input('07')
# input = common.read_input('07test')
pos = list(map(int, input[0].split(',')))


def part1():
    f = 0
    for p in pos:
        # 362 median
        f += math.fabs(362 - p)
    print(f)


def part2():
    cheap = 1e100
    actual_mid = 1e100
    # 500 guess, turned out 499!
    for mid in range(500):
        f = 0
        for p in pos:
            c = 0
            # guess
            # steps = int(math.fabs(math.floor(df.std()) - p))
            steps = int(math.fabs(mid - p))
            # for i in range(steps + 1):
            #     c += i
            c = steps * (steps + 1) / 2
            f += c
        old_cheap = cheap
        cheap = min(cheap, f)
        if old_cheap != cheap:
            actual_mid = mid
    print(cheap, actual_mid)


if __name__ == '__main__':
    print(len(input))
    part1()
    part2()
