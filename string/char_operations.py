def give_number(chr):
    if chr:
        return ord(chr)

def give_char(num):
    if num:
        return chr(num)


print(give_number('a'))
print(give_number(' '))
print(give_number('A'))
print(give_number(''))

print(give_char(97))
print(give_char(65))
print(give_char(32))
print(give_char(81))