import os

from operator import add, sub


def parse_data(data):
    all_operations = []
    for line in data.splitlines():
        op = sub if line[0] == 'L' else add
        dist = int(line[1:])
        all_operations.append((op, dist))
    return all_operations

def find_zeros(all_operations, current=50, size=100):
    counter1 = 0
    counter2 = 0
    for op, dist in all_operations:
        current = op(current, dist) % size
        if current == 0:
            counter1 += 1
        # How many times did we pass 0 going right and did not end at 0 (avoid double count)
        counter2 += op == add and current < (dist % 100) and current != 0
        # How many times did we pass 0 going left
        counter2 += op == sub and current > 100 - (dist % 100)
        # How many full loops did we do?
        counter2 += dist // 100
    return counter1, counter1 + counter2


DAY = 1
TEST_DATA = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

res = find_zeros(parse_data(TEST_DATA))
print(f'Day {DAY} of Advent of Code!')
print('Testing...')
print(f'Ends on a 0: {res[0]} times and hits 0 a total of {res[1]} times.')

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    res = find_zeros(parse_data(inp.read()))
    print(f'Ends on a 0: {res[0]} times and hits 0 a total of {res[1]} times.')
