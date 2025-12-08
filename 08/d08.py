import os

from math import prod
from itertools import combinations
import networkx as nx

DAY = 8
TEST_DATA = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def parse_data(raw_data):
    return [tuple([int(i) for i in box.split(',')]) for box in raw_data.splitlines()]


def distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 # squared distance


def get_distances(boxes):
    distances = {}
    pairs = combinations(boxes, 2)

    for pair in pairs:
        distances[pair] = distance(*pair)
    sorted_distances = sorted(distances.items(), key=lambda a: a[1], reverse=True)

    return sorted_distances


def connect_circuits(distances, i):
    circuits = [set(distances.pop()[0])]

    for _ in range(i-1):
        pair_to_check = distances.pop()[0]
        box1, box2 = pair_to_check

        found_idx = set()
        for idx, circuit in enumerate(circuits):
            if box1 in circuit:
                circuits[idx] = circuits[idx].union(set(pair_to_check))
                found_idx.add(idx)
            if box2 in circuit:
                circuits[idx] = circuits[idx].union(set(pair_to_check))
                found_idx.add(idx)
        if not found_idx:
            circuits.append(set(pair_to_check))

        if len(found_idx) == 2:
            i, j = sorted(found_idx)
            circuits[i].update(circuits[j])
            circuits.pop(j)

    return circuits


def check_until_mst(distances):
    G = nx.Graph()
    for d in distances:
        pair, w = d
        u, v = pair
        G.add_edge(u, v, weight=w)

    T = nx.minimum_spanning_tree(G)
    max_w = 0
    max_edge = None

    for e in T.edges(data=True):
        w = e[2]['weight']
        if w > max_w:
            max_w = w
            max_edge = e
    return max_edge[0][0] * max_edge[1][0]


boxes = parse_data(TEST_DATA)
print(prod(len(c) for c in sorted(connect_circuits(get_distances(boxes), 10), key=len, reverse=True)[:3]))
print(check_until_mst(get_distances(boxes)))


print(f'Day {DAY} of Advent of Code!')
print('Testing...')


input_path = f"{os.getcwd()}\\{str(DAY).zfill(2)}\\inp"
with open(input_path, mode='r', encoding='utf-8') as inp:
    print('Solution...')
    data = inp.read()
    boxes = parse_data(data)
    print(prod(len(c) for c in sorted(connect_circuits(get_distances(boxes), 1000), key=len, reverse=True)[:3]))
    print(check_until_mst(get_distances(boxes)))
