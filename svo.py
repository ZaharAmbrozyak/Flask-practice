def search4letters(text, letters='aeiou') -> set:
    output = set()
    for i in text:
        if i in letters:
            output.add(i)
    return output
