from helpers import alphabet_position, rotate_character



def encrypt(text,rot):
    encrypted_list = ''
    for char in text:
        encrypted_list += rotate_character(char,rot)
    return encrypted_list



def main():
    input_text = input("Please enter a text: ")
    rot = int(input("How many rotations?"))
    print (encrypt(input_text,rot))


if __name__=='__main__':
    main()
    
