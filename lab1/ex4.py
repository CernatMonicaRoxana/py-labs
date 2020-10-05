def camel_case_to_snake(stri):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in stri]).lstrip('_')


if __name__ == '__main__':
    print(camel_case_to_snake("TurnThisIntoSnakeCase"))
