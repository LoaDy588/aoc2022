import sys


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

def print_fs(root, offset):
    print(offset * "-", root.name)
    for dir in root.dirs:
        print_fs(dir, offset+1)
    for file in root.files:
        print(offset * "-", file[0], file[1])

def find_dir(dirs, name):
    for dir in dirs:
        if dir.name == name:
            return dir
    return None

def dir_size(root):
     total = 0
     total += sum([file[0] for file in root.files])
     total += sum([dir_size(dir) for dir in root.dirs])
     return total

def parse_fs(data):
    root = Dir("/", None)
    current = root
    for line in data:
        split_line = line.split()
        if split_line[0] == "$" and split_line[1] == "cd":
            if split_line[2] == "/":
                current = root
                continue
            if split_line[2] == "..":
                current = current.parent
                continue
            current = find_dir(current.dirs, split_line[2])
            if current is None:
                raise Exception("Fucked up")
            continue
        if split_line[0] == "$" and split_line[1] == "ls":
            continue
        if split_line[0] == "dir":
            current.dirs.append(Dir(split_line[1], current))
            continue
        current.files.append((int(split_line[0]), split_line[1]))

    return root

def sum_max(root, threshold):
    count = 0
    if dir_size(root) <= threshold:
        count += dir_size(root)
    for dir in root.dirs:
        count += sum_max(dir, threshold)
    return count

def part_one(data):
    fs = parse_fs(data)
    total = 0
    for dir in fs.dirs:
        total += sum_max(dir, 100000)
    return total


def smallest_bigger(root, threshold):
    best = 70000000
    if dir_size(root) >= threshold:
        best = dir_size(root)
    for dir in root.dirs:
        best = min(smallest_bigger(dir, threshold), best)
    return best

def part_two(data):
    fs = parse_fs(data)
    space_left = 70000000 - dir_size(fs)
    free_required = 30000000 - space_left
    best = 70000000
    for dir in fs.dirs:
        best = min(best, smallest_bigger(dir, free_required))
    return best


with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()
    print(part_one(input_data))
    print(part_two(input_data))