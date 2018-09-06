def get_initials(fullname):
    names = fullname.split()
    initials = ""
    for name in names:
        first_letter = name[0]
        first_capitalized = first_letter.upper()
        initials = initials + first_capitalized
    return initials

def main():
    fullname = input('Please enter your first and last name:')
    initials = get_initials(fullname)
    formatted_fullname = "'" + fullname + "'"
    print("The initials of",formatted_fullname,"are",initials)

if __name__=="__main__":
    main()

