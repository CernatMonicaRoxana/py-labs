def most_common_char(sentence):
    sentence = ''.join(sentence.split(' '))
    dup_letter = []
    dup_encountered = []

    for c in sentence.lower():
        if c not in dup_letter and sentence.lower().count(c) > 1:
            dup_letter.append(c)
            dup_encountered.append(sentence.lower().count(c))

    max_dup = max(dup_encountered)
    index_of_max = dup_encountered.index(max_dup)
    return "The letter ** {} ** appears {} times".format(dup_letter[index_of_max], dup_encountered[index_of_max])


if __name__ == '__main__':
    string = 'an apple is not a tomato'
    print(most_common_char(string))


