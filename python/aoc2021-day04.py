import numpy as np
import pandas as pd

import common

__author__ = 'Daniël'


boards = []
board = None
input = common.read_input('04')
numbers = list(map(int, input[0].split(',')))
for line in input[1:]:
    line = line.strip()
    if line == '':
        if board is not None:
            boards.append(pd.DataFrame(board))
        board = []
    else:
        board.append(list(map(int, line.split())))

def has_win(board):
    for col in board:
        c = board[col]
        if (len(c[c.isna()]) == 5):
            return True
    for row in board.iterrows():
        r = row[1]
        if (len(r[r.isna()]) == 5):
            return True
    return False

def part1():
    boards2 = [b.copy(deep=True) for b in boards]
    for n in numbers:
        for i in range(len(boards2)):
            b = boards2[i]
            b.replace(n, np.nan, inplace=True)
            if has_win(b):
                print(b.stack().sum() * n)
                return

def part2():
    boards2 = [b.copy(deep=True) for b in boards]
    has_won = []
    for n in numbers:
        for i in range(len(boards2)):
            if i in has_won:
                continue
            b = boards2[i]
            b.replace(n, np.nan, inplace=True)
            if has_win(b):
                print(i, b.stack().sum() * n)
                has_won.append(i)


if __name__=='__main__':
    print(len(boards))
    part1()
    part2()
