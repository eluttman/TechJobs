from helpers import alphabet_position, rotate_character



def encrypt(text,key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    count = 0
    for char in text:
        if char.lower() in alphabet:
            letter_of_key= key[count % len(key)]
            num_to_rotate_by = alphabet_position(letter_of_key)
            encrypted_message += rotate_character(char,num_to_rotate_by)
            count += 1
        else:
            encrypted_message += char
    return encrypted_message

def main():
    text = input("Please enter your message:")
    key = input("Please enter your key word:")
    print (encrypt(text, key))

if __name__ == "__main__":
    main()