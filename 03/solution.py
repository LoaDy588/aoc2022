import sys

def chunks(input, n):
    for i in range(0, len(input), n):
        yield input[i:i+n]

def get_priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def part_one(data):
    sum = 0
    for line in data:
        c_size = len(line) // 2
        compartment_a = set(line[:c_size])
        compartment_b = set(line[c_size:])
        intersect = compartment_a & compartment_b
        sum += get_priority(intersect.pop())
    return sum

def part_two(data):
    sum = 0
    for group in chunks(data, 3):
        a = set(group[0][:-1])
        b = set(group[1][:-1])
        c = set(group[2][:-1])
        common = a & b & c
        sum += get_priority(common.pop())
    return sum

with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()
    print(part_one(input_data))
    print(part_two(input_data))