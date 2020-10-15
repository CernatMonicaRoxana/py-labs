def items_x_times(x, *lines):
    ocurrences = {i: sum([line.count(i) for line in lines]) for line in lines for i in line}
    print([key for key, value in ocurrences.items() if value == x])


def items_x_times_2(x, *lines):
    concat_list = sum(lines, start=[])
    result = []
    for el in filter(lambda i: concat_list.count(i) == x, concat_list):
        if el not in result:
            result.append(el)
    print(result)


if __name__ == '__main__':
    items_x_times_2(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, 'test'])
