def extract_first_no(string):
    return ''.join([c for c in string if c.isdigit()])


if __name__ == '__main__':
    stri = 'An apple is 123 USD'
    str1 = 'abc123abc'
    str2 = 'ab2abb4'

    print(extract_first_no(stri))
    print(extract_first_no(str1))
    print(extract_first_no(str2))
