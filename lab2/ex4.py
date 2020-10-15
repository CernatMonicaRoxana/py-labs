def compose(notes, moves, start):
    num_notes = len(notes)
    position = start
    song = [notes[position]]

    for move in moves:
        position = (position + move) % num_notes
        song.append(notes[position])

    return song


if __name__ == '__main__':
    print(compose(['do', 're', 'mi', 'fa', 'sol'], [1, -3, 4, 2], 2))
