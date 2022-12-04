import sys


def part_one(data):
    count = 0
    for line in data:
        lr_split = line.split(',')
        ranges_1 = list(map(int, lr_split[0].split('-')))
        ranges_2 = list(map(int, lr_split[1].split('-')))
        if (ranges_1[0] >= ranges_2[0] and ranges_1[1] <= ranges_2[1]):
            count += 1
            continue
        if (ranges_2[0] >= ranges_1[0] and ranges_2[1] <= ranges_1[1]):
            count += 1
            continue
    return count


def part_two(data):
    count = 0
    for line in data:
        lr_split = line.split(',')
        ranges_1 = list(map(int, lr_split[0].split('-')))
        ranges_2 = list(map(int, lr_split[1].split('-')))
        set_1 = set(range(ranges_1[0], ranges_1[1] + 1))
        set_2 = set(range(ranges_2[0], ranges_2[1] + 1))
        intersect = set_1 & set_2
        if len(intersect) != 0:
            count += 1
    return count


with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()
    print(part_one(input_data))
    print(part_two(input_data))