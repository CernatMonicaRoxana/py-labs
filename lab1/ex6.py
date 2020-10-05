def palindrome(a):
    return a == a[::-1]


if __name__ == '__main__':
    print(palindrome('malam'))
    print(palindrome('baba'))
    print(palindrome('ana'))
