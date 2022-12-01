import sys

with open(sys.argv[1]) as input_file:
    input_data = input_file.readlines()


elves = [0]
index = 0

for line in input_data:
    if (line == "\n"):
        index += 1
        elves.append(0)
        continue
    elves[index] += int(line)

elves.sort()

print(elves[-1])
print(sum(elves[-3:]))
