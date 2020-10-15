def fibonacci(n):
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def first_n_fib(n):
    fib = []
    for i in range(1, n+1):
        fib.append(fibonacci(i))
    return fib


if __name__ == '__main__':
    print(first_n_fib(10))
