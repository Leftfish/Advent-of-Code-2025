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


def get_k_best_digits(row, k):
    n = len(row)
    dp = {}

    def dfs(idx, remaining):
        # Base case: no more digits to add, so we add nothing more
        if remaining == 0:
            return ''
        # Base case: we reached the end of the row without building a k-digit number
        if idx == n:
            return None
        # Base case: we do not have enough digits left in the row to build a k-digit number
        if (n - idx) < remaining:
            return None
        # DP: we have already been there (at idx p with q digits to go) so pick the state from the cache
        if (idx, remaining) in dp:
            return dp[(idx, remaining)]


        # Take/skip approach: we try either append the next digit to the result and move forward
        # (take_result if it does not lead to a dead-end base case) or just move forward (skip_result)
        take_next = dfs(idx+1, remaining-1)

        if take_next is not None:
            take_result = row[idx] + take_next
        else:
            take_result = None

        skip_result = dfs(idx+1, remaining)

        # Then we move forward with the better option, saving it in the cache
        if take_result is None:
            best = skip_result
        elif skip_result is None:
            best = take_result
        else:
            best = max(take_result, skip_result)

        dp[(idx, remaining)] = best
        return best

    return dfs(0, k)


DAY = 3
TEST_DATA = '''987654321111111
811111111111119
234234234234278
818181911112111'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
rows = parse_data(TEST_DATA)
print('Best joltages from left to right (2 batteries):', sum(check_row(r) for r in rows) == 357)
print('Best joltages from left to right (2 batteries recursive):', sum(int(get_k_best_digits(r, 2)) for r in TEST_DATA.splitlines()) == 357)
print('Best joltages from left to right (12 batteries recursive):', sum(int(get_k_best_digits(r, 12)) for r in TEST_DATA.splitlines()) == 3121910778619)

input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    rows = parse_data(data)
    print('Best joltages from left to right (2 batteries):', sum(check_row(r) for r in rows))
    print('Best joltages from left to right (2 batteries recursive):', sum(int(get_k_best_digits(r, 2)) for r in data.splitlines()))
    print('Best joltages from left to right (12 batteries recursive):', sum(int(get_k_best_digits(r, 12)) for r in data.splitlines()))
