def decrypt(text, key1, key2):
    # Reverse second transposition
    n = len(text)
    rows = (n + key2 - 1) // key2
    remainder = n % key2

    columns = []
    start = 0

    for i in range(key2):
        size = rows if remainder == 0 or i < remainder else rows - 1
        columns.append(text[start:start + size])
        start += size

    first = ''
    for r in range(rows):
        for c in range(key2):
            if r < len(columns[c]):
                first += columns[c][r]

    # Reverse first transposition
    n = len(first)
    rows = (n + key1 - 1) // key1
    remainder = n % key1

    columns = []
    start = 0

    for i in range(key1):
        size = rows if remainder == 0 or i < remainder else rows - 1
        columns.append(first[start:start + size])
        start += size

    original = ''
    for r in range(rows):
        for c in range(key1):
            if r < len(columns[c]):
                original += columns[c][r]

    return original