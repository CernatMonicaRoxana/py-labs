def count_words(text:str) -> int:
    text = text.split(' ')
    return len(text)


if __name__ == '__main__':
    print(count_words("I have Python exam."))
