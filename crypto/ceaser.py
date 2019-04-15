
def rot13(mess, new_int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    signs = '!?,:'
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        elif char.isalpha() == False:
            encrypted = encrypted + char
        elif char == char.upper():
            char = char.lower()
            rotated_index = alphabet.index(char) + new_int
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index].upper()
            else:
                encrypted = encrypted + alphabet[rotated_index % 26].upper()    
        else:
            rotated_index = alphabet.index(char) + new_int
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted
def main():
    new_int = int(input("how much would you like it to rotate?"))
    print(rot13("Hello World!", new_int))
if __name__ == "__main__":
    main()
