__author__ = 'Daniël'


def read_input(day, year=2021):
     with open(f'aoc{year}-day{day}.txt', 'r') as f:
         return f.readlines()
