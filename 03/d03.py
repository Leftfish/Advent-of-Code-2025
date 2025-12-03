import os


def parse_data(data):
    return [[int(i) for i in row] for row in data.splitlines()]

def find_best(row):
    best = 0
    idx = 0
    for i, battery in enumerate(row):
        if battery > best:
            best = battery
            idx = i
    return best, idx

def check_row(row):
    first, idx = find_best(row[:len(row)-1])
    second, _ = find_best(row[idx+1:])
    return 10* first + second

DAY = 3
TEST_DATA = '''987654321111111
811111111111119
234234234234278
818181911112111'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
rows = parse_data(TEST_DATA)
print('Best joltages from left to right:', sum(check_row(r) for r in rows) == 357)


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    rows = parse_data(inp.read())
    print('Best joltages from left to right:', sum(check_row(r) for r in rows))