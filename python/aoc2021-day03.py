import pandas as pd

import common

__author__ = 'Daniël'

test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".split()

input = []
for line in common.read_input('03'):
# for line in test:
    input.append(list(map(int, list(line.strip()))))

def part1():
    gamma = []
    epsilon = []
    df = pd.DataFrame(input)
    for i in df:
        c = df[i].value_counts()
        if c[0] > c[1]:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
    gamma_decimal = int(''.join(gamma), 2)
    epsilon_decimal = int(''.join(epsilon), 2)
    print("{} * {} = {}". format(gamma_decimal, epsilon_decimal, gamma_decimal * epsilon_decimal))

def part2():
    df = pd.DataFrame(input)
    check_df = df
    for i in df:
        c = check_df[i].value_counts()
        if c[0] > c[1]:
            check_df = check_df[check_df[i] == 0]
        else:
            check_df = check_df[check_df[i] == 1]

        if len(check_df) == 1:
            break
    ox = int(''.join(check_df.iloc[0].astype(str)), 2)
    print("ox", ox)

    check_df = df
    for i in df:
        c = check_df[i].value_counts()
        if c[0] < c[1] or c[0] == c[1]:
            check_df = check_df[check_df[i] == 0]
        else:
            check_df = check_df[check_df[i] == 1]

        if len(check_df) == 1:
            break

    co2 = int(''.join(check_df.iloc[0].astype(str)), 2)
    print("co2", co2)
    print(co2 * ox)


if __name__=='__main__':
    print(len(input))
    part1()
    part2()
