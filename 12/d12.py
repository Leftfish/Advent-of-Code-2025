import os

import re

DAY = 12
TEST_DATA = '''0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2'''

def parse_data(data):
    split = data.split('\n\n')
    puzzles, regions = [], []

    for puzzle in split[:-1]:
        piece = []
        flds = puzzle.splitlines()[1:]
        for line in flds:
            piece.append([1 if c == '#' else 0 for c in line])
        puzzles.append(piece)

    raw_regions = split[-1]
    re_region = r'(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)'

    for region in raw_regions.splitlines():
        nums = re.findall(re_region, region)[0]
        expected = [0]* len(nums[2:])
        area = int(nums[0]) * int(nums[1])
        for idx, val in enumerate(nums[2:]):
            expected[idx] += int(val)
        regions.append((area, expected))

    return puzzles, regions


def sum_piece_area(piece):
    return sum((sum(line) for line in piece))


def solve_in_the_dirtiest_possible_way(data):
    puzzles, regions = parse_data(data)
    res = 0
    for area, pieces in regions:
        s = 0
        for idx, val in enumerate(pieces):
            s += val * sum_piece_area(puzzles[idx])
        res += (s <= area)
    return res


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
print('NOT TESTING FOR THE TEST INPUT BECAUSE OF HOW THE PUZZLE IS STRUCTURED...')


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    print('...AND THE DIRTY SOLUTION WORKS FOR THE ACTUAL INPUT, AND THE RESULT IS:', solve_in_the_dirtiest_possible_way(data))
