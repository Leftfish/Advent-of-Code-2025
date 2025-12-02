import os


def parse_data(data):
    ranges = []
    for rng in data.split(','):
        start, end = rng.split('-')
        ranges.append((int(start), int(end)))
    return ranges


def factorize(n):
    factors = []
    for i in range(1, n+1):
        if n / i == n // i:
            factors.append(i)
    return factors


def find_multiples(rng):
    duplicates = set()
    multiples = set()
    start, end = rng
    digs_start, digs_stop = int(len(str(start))), int(len(str(end)))
    to_check = [digs_start] if digs_start == digs_stop else [digs_start, digs_stop]

    for dig_number in to_check:
        for factor in factorize(dig_number):
            if factor != dig_number:
                for i in range(1, 10**factor):
                    repeated = int(str(i) * (dig_number // factor))
                    if start <= repeated <= end:
                        multiples.add(repeated)
                        if dig_number // factor == 2:
                            duplicates.add(repeated)

    return sum(duplicates), sum(multiples)


DAY = 2
TEST_DATA = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''


print(f'Day {DAY} of Advent of Code!')
print('Testing...')
rngs = parse_data(TEST_DATA)
print('Sum of duplicates:', sum((find_multiples(rng)[0]) for rng in rngs) == 1227775554)
print('Sum of multiples:', sum((find_multiples(rng)[1]) for rng in rngs) == 4174379265)


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    rngs = parse_data(inp.read())
    print('Sum of duplicates:', sum((find_multiples(rng)[0]) for rng in rngs))
    print('Sum of multiples:', sum((find_multiples(rng)[1]) for rng in rngs))
