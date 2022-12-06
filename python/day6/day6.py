def part1(input):
    for row in input:
        for i in range(len(row)):
            if len(set(row[i : i + 4])) == 4:
                print(i + 4)
                break


def part2(input):
    for row in input:
        for i in range(len(row)):
            if len(set(row[i : i + 14])) == 14:
                print(i + 14)
                break


def read_input(filename):
    input_data = open(filename, "r")

    return list(input_data)


if __name__ == "__main__":
    part1(read_input("input"))
    part2(read_input("input"))
