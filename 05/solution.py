import sys


def parse_matrix(data):
    line_no = 0
    while(data[line_no].split()[0] != "1"):
        line_no += 1
    
    stacks = len(data[line_no].split())
    matrix =  [[] for _ in range(stacks)]

    for i in range(line_no):
        for s in range(stacks):
            item = data[line_no-i - 1][(s * 4) + 1]
            if (item == " "): continue
            matrix[s].append(item)
    return matrix, line_no

def command_split(command):
    split = command.split()
    amount = int(split[1])
    origin = int(split[3]) - 1
    target = int(split[5]) - 1
    return amount, origin, target

def get_top_crates(matrix):
    result = ''
    for stack in matrix:
        result += stack[-1]
    return result

def part_one(data):
    matrix, line_no = parse_matrix(data)
    start_line = line_no + 2

    for command in data[start_line:]:
        split = command.split()
        amount, origin, target = command_split(command)
        for _ in range(amount):
            matrix[target].append(matrix[origin].pop())

    return get_top_crates(matrix)


def part_two(data):
    matrix, line_no = parse_matrix(data)
    start_line = line_no + 2

    for command in data[start_line:]:
        split = command.split()
        amount, origin, target = command_split(command)
        lifted = matrix[origin][-amount:]
        matrix[origin] = matrix[origin][:-amount]
        matrix[target].extend(lifted)

    return get_top_crates(matrix)


with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()
    print(part_one(input_data))
    print(part_two(input_data))