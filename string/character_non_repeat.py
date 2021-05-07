def first_character_repeat(word):
    char_keys = {}
    for chr in word:
        if chr in char_keys:
            return chr
        else:
            char_keys[chr] = 1
    return None

print(first_character_repeat("vamosrafa"))