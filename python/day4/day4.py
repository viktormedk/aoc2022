def part1(input):
    count = 0

    for sections in input:
        # clean data for easier comparison
        sec1, sec2 = sections.rstrip().split(",")
        sec1 = [int(x) for x in sec1.split("-")]
        sec2 = [int(x) for x in sec2.split("-")]

        # is first section in second
        if sec1[0] >= sec2[0]:
            if sec1[1] <= sec2[1]:
                count += 1
                continue

        # is second section in first
        if sec1[0] <= sec2[0]:
            if sec1[1] >= sec2[1]:
                count += 1
    print(count)


def part2(input):
    count = 0

    for sections in input:
        # clean data for easier comparison
        sec1, sec2 = sections.rstrip().split(",")
        sec1 = [int(x) for x in sec1.split("-")]
        sec2 = [int(x) for x in sec2.split("-")]

        # Do they intersect?
        if max(sec1[0], sec2[0]) <= min(sec1[1], sec2[1]):
            count += 1

    print(count)


def read_input(filename):
    input_data = open(filename, "r")

    return list(input_data)


if __name__ == "__main__":
    part1(read_input("input"))
    part2(read_input("input"))
