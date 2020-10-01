def spiral(matrix):
    size = len(matrix)
    res = ''.join(matrix[0])
    res += ''.join([matrix[i][size-1] for i in range(1, size)])
    res += ''.join(matrix[size-1][-2::-1])
    res += ''.join([matrix[i][0] for i in range(size-2, 0, -1)])
    res += ''.join(matrix[1])
    return res


if __name__ == '__main__':
    matrix1 = [
        ["a", "b", "c", "d"],
        ["l", "m", "n", "e"],
        ["k", "p", "o", "f"],
        ["j", "i", "h", "g"]
    ]

    matrix2 = [
        ['1', '2', '3', '4', '5'],
        ['g', 'h', 'i', 'j', '6'],
        ['f', 'o', 'p   ', 'k', '7'],
        ['e', 'n', 'm', 'l', '8'],
        ['d', 'c', 'b', 'a', '9']
    ]
    print(spiral(matrix1))