def extract_digits(string):
    return ''.join([c for c in string if c.isdigit()])


if __name__ == '__main__':
    str = 'An apple is 123 USD'
    str1 = 'abc123abc'
    str2 = 'ab2abb4'

    print(extract_digits(str))
    print(extract_digits(str1))
    print(extract_digits(str2))
