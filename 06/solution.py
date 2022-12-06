import sys

def find_unique_n_sequence(data, n):
    start = 0
    while(len(set(data[start:start+n])) != n):
        start += 1
    return start + n

with open(sys.argv[1]) as input_file:
    input_data = input_file.readline()
    print(find_unique_n_sequence(input_data, 4))
    print(find_unique_n_sequence(input_data, 14))