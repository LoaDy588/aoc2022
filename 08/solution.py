import sys
import numpy as np
from functools import partial

def rotate(data):
    return [list(x) for x in zip(*data[::-1])]

def parse_input(data):
    edge_len = len(data)
    output = np.empty([edge_len, edge_len], dtype=int)
    for index, line in enumerate(data):
        line_parsed = list(map(int, line[:-1]))
        output[index] = line_parsed
    return output

def is_visible(data,x, y):
    value = data[y, x]
    line = data[y, :]
    column = data[:, x]
    l_r = min(max(line[:x]), max(line[x+1:]))
    t_b = min(max(column[:y]), max(column[y+1:]))
    return l_r < value or t_b < value


def part_one(data):
    parsed = parse_input(data)
    count = 0
    edge_len = len(parsed)
    for x in range(1, edge_len-1):
        for y in range(1, edge_len-1):
            if is_visible(parsed, x, y):
                count += 1
    count += 2 * edge_len + 2 * (edge_len - 2)
    return count

def visible_length(data, value):
    if data.size == 1:
        return 1
    if data.size == 0:
        return 0
    visible = 0
    while data[visible] < value:
        visible += 1
        if visible == data.size - 1:
            break
    return visible + 1


def visibility(data, x, y):
    value = data[y, x]
    line = data[y, :]
    column = data[:, x]
    splits = [np.flip(line[:x]), line[x+1:], np.flip(column[:y]), column[y+1:]]
    vis_func = partial(visible_length, value=value)
    output = list(map(vis_func, splits))
    return np.prod(output)

def part_two(data):
    parsed = parse_input(data)
    max_visibility = 0
    edge_len = len(parsed)
    for x in range(edge_len):
        for y in range(edge_len):
            max_visibility = max(max_visibility, visibility(parsed, x, y))
    return max_visibility


with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()
    print(part_one(input_data))
    print(part_two(input_data))