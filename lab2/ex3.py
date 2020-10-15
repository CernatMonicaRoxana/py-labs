def operations_on_lists(a, b):
    intes = [val_a for val_a in a if val_a in b]
    reunion = a[:]
    for val in b:
        if val not in a:
            reunion.append(val)
    a_b = [val_a for val_a in a if val_a not in b]
    b_a = [val_b for val_b in b if val_b not in a]

    return intes, reunion, a_b, b_a


if __name__ == '__main__':
    a1 = [1, 2, 3, 4]
    b1 = [4, 5, 6, 7]
    print(operations_on_lists(a1, b1))
