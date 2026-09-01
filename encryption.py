def encrypt(text, key1, key2):
    # First transposition
    rows = [text[i:i + key1] for i in range(0, len(text), key1)]
    first = ''.join(''.join(row[i] for row in rows if i < len(row))
                    for i in range(key1))

    # Second transposition
    rows = [first[i:i + key2] for i in range(0, len(first), key2)]
    second = ''.join(''.join(row[i] for row in rows if i < len(row))
                     for i in range(key2))

    return second