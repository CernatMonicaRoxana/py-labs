def vowel_counter(sentence):
    vowels = 'aeiou'
    count = 0
    for c in sentence:
        if c.lower() in vowels:
            count += 1

    return count


if __name__ == '__main__':
    print(vowel_counter('Ana are mere'))
