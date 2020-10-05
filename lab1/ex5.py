def spiral(matrix):
    size = len(matrix)
    # first row
    r = ''.join(matrix[0])
    # last column without first element
    r += ''.join([matrix[i][size-1] for i in range(1, size)])
    # last row
    r += ''.join(matrix[size-1][-2::-1])
    # first column
    r += ''.join([matrix[i][0] for i in range(size - 2, 0, -1)])
    # inner matrix
    if size > 2:
        r += spiral([matrix[i][1:size-1] for i in range(1, size - 1)])

    return r


if __name__ == '__main__':
    matrix1 = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p'],
    ]

    print(spiral(matrix1))
