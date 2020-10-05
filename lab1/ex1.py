def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    numbers = input()
    numbers = [int(no) for no in numbers]
    print(numbers)

    a = numbers[0]
    b = numbers[1]

    gcd_a_b = gcd(a, b)

    for i in range(2, len(numbers)):
        gcd_a_b = gcd(gcd_a_b, numbers[i])

    print(gcd_a_b)
