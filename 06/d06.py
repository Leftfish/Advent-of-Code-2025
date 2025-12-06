import os
from functools import reduce
from operator import mul, add


def parse_data(data):
    cols = [[] for _ in range(len(data[0].split()))]
    for i, col in enumerate(cols):
        for line in data:
            cols[i].append(line.split()[i])
    return cols


def calculate_column_normal(col):
    nums = [int(n) for n in col[:-1]]
    op = mul if col[-1] == '*' else add
    return reduce(op, nums)


def get_ranges(operator_ln):
    ranges = []
    start = 0
    cur = 1
    while cur < len(operator_ln):
        if operator_ln[cur] != ' ':
            ranges.append([start, cur-1])
            start = cur
        cur += 1
    ranges.append([start, cur])
    return ranges


def count_cephalophod_numbers(data, ranges):
    s = 0
    for r in ranges:
        nums = []
        curr = ''
        for i in range(r[0], r[1]+1):
            for line in data[:-1]:
                curr += line[i]
            if not curr.isspace():
                nums.append(int(curr))
            curr = ''
        op = mul if data[-1][r[0]] == '*' else add
        s += reduce(op, nums)
    return s


DAY = 6
TEST_DATA = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + '''.splitlines()


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
print('Calculating the normal way:', sum(calculate_column_normal(col) for col in parse_data(TEST_DATA)) == 4277556)
print('Calculating the cephalophod way:', count_cephalophod_numbers(TEST_DATA, get_ranges(TEST_DATA[-1])) == 3263827)

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.readlines()
    print('Calculating the normal way:', sum(calculate_column_normal(col) for col in parse_data(data)))
    print('Calculating the cephalophod way:', count_cephalophod_numbers(data, get_ranges(data[-1])))
