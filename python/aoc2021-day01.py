import itertools
import common

__author__ = 'Daniël'
input = list(map(int, common.read_input('01')))


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in itertools.pairwise(itertools.pairwise(iterable)):
        yield a, b, c


def part1():
    c = 0
    p_d = max(input)
    for d in input:
        if d > p_d:
            c += 1
        p_d = d
    print(c)

def part2():
    c = 0
    a = 0
    p_d = max(input) * 3
    for d in range(len(input)+1):
        w = input[d-3:d]
        if len(w) != 3:
            continue
        d = sum(w)
        if d > p_d:
            c += 1
        a += 1
        p_d = d
    print(c, a)


def part2better():
    c = 0
    p_d = max(input) * 3
    for x, y, z in triplewise(input):
        d = x + y + z
        if d > p_d:
            c += 1
        p_d = d
    print(c)

if __name__=='__main__':
    print(len(input))
    part1()
    part2()
    part2better()
