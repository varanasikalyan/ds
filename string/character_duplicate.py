def duplicate_characters(token):
    result = {}
    for character in token:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1

    return result

print(duplicate_characters("Programming"))