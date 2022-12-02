import sys


def is_win(opponent, player):
    if (opponent == 3 and player == 1):
        return True
    if (opponent == 1 and player == 2):
        return True
    if (opponent == 2 and player == 3):
        return True
    return False

def part_one(input_data):
    score = 0
    for line in input_data:
        separated = line.split()
        opponent = ord(separated[0]) - 64
        me = ord(separated[1]) - 87
        score += me
        if me == opponent:
            score += 3
        if is_win(opponent, me):
            score += 6
    return score

def part_two(input_data):
    score = 0
    for line in input_data:
        separated = line.split()
        opponent = ord(separated[0]) - 65
        me = ord(separated[1]) - 89
        score += (me + 1) * 3
        score += ((me + opponent) % 3) + 1
    return score

with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()
    print(part_one(input_data))
    print(part_two(input_data))