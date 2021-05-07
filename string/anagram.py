def is_anagram(check_token, anagram):
    if len(check_token) != len(anagram):
        return False

    anagram = anagram.lower()
    check_token = check_token.lower()

    for ch in check_token:
        pos = anagram.index(ch)        
        if pos != -1:
            anagram = anagram.replace(ch, '', 1)
        else:
            return False      

    if anagram == '':
        return True

print("Night","Thing")
print(is_anagram("Night","Thing"))