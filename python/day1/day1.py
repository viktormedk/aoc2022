def part1(input):

    max_cal = 0

    curr_cal = 0

    for cal in input:
        if not cal.isspace():
            curr_cal += int(cal)
        else:
            curr_cal = 0

        max_cal = max(max_cal, curr_cal)

    print(max_cal)


def part2(input):

    curr_cal = 0

    cal_list = []

    for cal in input:
        if not cal.isspace():
            curr_cal += int(cal)
            if cal == input[-1]:
                cal_list.append(curr_cal)
        else:
            cal_list.append(curr_cal)
            curr_cal = 0

    print(sum(sorted(cal_list, reverse=True)[:3]))


def read_input(filename):
    input_data = open(filename, "r")

    return list(input_data)


if __name__ == "__main__":
    part1(read_input("input"))
    part2(read_input("input"))
