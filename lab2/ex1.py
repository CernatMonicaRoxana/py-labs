def fibonacci(n):
    fibonacci_list = [0, 1]
    if n < 1 :
        return []
    elif n == 1:
        return [0]
    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return list(map(str, fibonacci_list))


if __name__ == '__main__':
    print(fibonacci(10))
s
