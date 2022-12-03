def part1(input):
    result = 0

    for rucksack in input:
        result_list = []
        middle = int(len(rucksack.rstrip()) / 2)
        end = int(len(rucksack.rstrip()))

        for item in rucksack[:middle]:
            if item in rucksack[middle:end]:
                if item.isupper():
                    const = 38
                else:
                    const = 96

                result_list.append((ord(item) - const))

        result += sum(set(result_list))

    print(result)


def part2(input):
    result = 0
    input = [item.rstrip() for item in input]
    triplets = []

    for item in range(0, len(input), 3):
        triplets.append(input[item : item + 3])

    for triple in triplets:
        done = False
        for rucksack in triple[0]:
            if done:
                continue
            for item in rucksack:
                if item in triple[0] and item in triple[1] and item in triple[2]:
                    done = True
                    if item.isupper():
                        const = 38
                    else:
                        const = 96
                    result += ord(item) - const
    print(result)


def read_input(filename):
    input_data = open(filename, "r")

    return list(input_data)


if __name__ == "__main__":
    part1(read_input("input"))
    part2(read_input("input"))
