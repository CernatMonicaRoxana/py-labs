def count_bits(no):
    no = bin(no).lstrip('0b')
    return no.count('1')


if __name__ == '__main__':
    print(count_bits(24))
