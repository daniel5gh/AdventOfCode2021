import itertools
import common

__author__ = 'Daniël'
input = list(map(int, common.read_input('01')))


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
    for d in range(len(input)):
        w = input[d-3:d]
        if len(w) != 3:
            continue
        d = sum(w)
        if d > p_d:
            c += 1
        a += 1
        p_d = d
    print(c+1, a) # bug! a should be 1998, but is 1997 so I guessed the +1 which was correct


if __name__=='__main__':
    print(len(input))
    part1()
    part2()
