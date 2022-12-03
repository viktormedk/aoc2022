part1 = {
    "AX": 4,
    "BX": 1,
    "CX": 7,
    "AY": 8,
    "BY": 5,
    "CY": 2,
    "AZ": 3,
    "BZ": 9,
    "CZ": 6,
}

part2 = {
    "AX": 3,
    "BX": 1,
    "CX": 2,
    "AY": 4,
    "BY": 5,
    "CY": 6,
    "AZ": 8,
    "BZ": 9,
    "CZ": 7,
}


def day2(input, score):
    result = 0

    for line in input:
        result += score[f"{line[0]}" + f"{line[2]}"]

    print(result)


def read_input(filename):
    input_data = open(filename, "r")

    return list(input_data)


if __name__ == "__main__":
    day2(read_input("input"), part1)
    day2(read_input("input"), part2)
