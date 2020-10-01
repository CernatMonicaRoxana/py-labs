from string import ascii_uppercase


def convert(string):
    for c in ascii_uppercase:
        string = string.replace(c, "_"+c.lower())
        string = string.lstrip("_")
    return string


if __name__ == '__main__':
    print(convert("AnaAreMere"))