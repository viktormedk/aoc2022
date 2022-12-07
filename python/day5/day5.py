def part1(input):
    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    offset = 1
    for n_stacks in range(1, 10):
        for i in range(8):
            box = input[i][offset].strip()
            if box.isalpha():
                stacks[n_stacks].append(box)
        offset += 4

    for row in input[10:]:
        conf = [int(d) for d in row.split() if d.isdigit()]
        for times in range(int(conf[0])):
            stacks[int(conf[2])].insert(0, stacks[int(conf[1])].pop(0))

    for n in range(1, 10):
        print(stacks[n][0])


def part2(input):
    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    offset = 1
    for n_stacks in range(1, 10):
        for i in range(8):
            box = input[i][offset].strip()
            if box.isalpha():
                stacks[n_stacks].append(box)
        offset += 4

    for row in input[10:]:
        conf = [int(d) for d in row.split() if d.isdigit()]
        retain = int(conf[0])
        for times in range(int(conf[0])):
            if retain > 1:
                stacks[int(conf[2])].insert(times, stacks[int(conf[1])].pop(0))
            else:
                stacks[int(conf[2])].insert(0, stacks[int(conf[1])].pop(0))

    for n in range(1, 10):
        print(stacks[n][0])


def read_input(filename):
    input_data = open(filename, "r")

    return list(input_data)


if __name__ == "__main__":
    part1(read_input("input"))
    part2(read_input("input"))
