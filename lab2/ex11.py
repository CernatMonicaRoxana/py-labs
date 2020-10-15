def special_sort(list_of_tuples):
    list_of_tuples.sort(key=lambda tuples: tuples[1][2])
    print(list_of_tuples)


if __name__ == '__main__':
    lists = [('abc', 'bcd'), ('abc', 'zza')]
    special_sort(lists)
