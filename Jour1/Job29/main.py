def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        elif note >= 40 and note % 5 >= 3:
            arrondies.append(note + (5 - note % 5))
        else:
            arrondies.append(note)
    return arrondies

print(arrondir_notes([73, 67, 38, 33, 83, 82, 68, 54]))