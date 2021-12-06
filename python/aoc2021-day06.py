import common
from collections import defaultdict

__author__ = 'Daniël'

initial_fish = []
input = common.read_input('06')
initial_fish = list(map(int, input[0].split(',')))


def step1(fish):
    new_fish = []
    for f in fish:
        n = f - 1
        if n == -1:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(n)
    return new_fish


def part1():
    fish = initial_fish[:]
    for i in range(80):
        fish = step1(fish)
    print(len(fish))


def step2(fish):
    new_fish = defaultdict(int)
    for i, n in fish.items():
        if i == 0:
            new_fish[6] += n
            new_fish[8] += n
        else:
            new_fish[i - 1] += n
    return new_fish


def part2():
    fish = defaultdict(int)
    for n in initial_fish:
        fish[n] += 1
    for day in range(256):
        fish = step2(fish)
    print(sum(fish.values()))


if __name__ == '__main__':
    print(len(initial_fish))
    part1()
    part2()
