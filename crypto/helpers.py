def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.lower() not in alphabet:
        return char
    new_index = (alphabet_position(char) + rot) % len(alphabet)
    if char.isupper():
        return alphabet[new_index].upper()
    else:
        return alphabet[new_index]