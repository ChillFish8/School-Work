__Morse_Code_Dict__ = { 'A': '.-', 'B': '-...',
                        'C': '-.-.', 'D': '-..', 'E': '.',
                        'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-',
                        'L': '.-..', 'M': '--', 'N': '-.',
                        'O': '---', 'P': '.--.', 'Q': '--.-',
                        'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--',
                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
                        '1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        '0': '-----', ', ': '--..--', '.': '.-.-.-',
                        '?': '..--..', '/': '-..-.', '-': '-....-',
                        '(': '-.--.', ')': '-.--.-'}


def encrypt():
    user_input_ = input("What would you like to encrypt?")
    Encryption = ""
    for letter in user_input_:
        code_ = f"{__Morse_Code_Dict__[letter.upper()]} "
        Encryption += code_
    print(f"Here is your encrypted message: {Encryption}")


def decrypt():
    user_input_ = input("What would you like to decrypt?")
    Decryption = ""
    Temp_Letter = ""
    i = 0
    for letter in user_input_:
        if letter != ' ':
            i = 0
            Temp_Letter += letter
        else:
            i += 1
            if i == 2:
                Decryption += ' '
            else:
                Decryption += list(__Morse_Code_Dict__.keys())[list(__Morse_Code_Dict__.values()).index(Temp_Letter)]
                Temp_Letter = ''
    print(f"Here is your decrypted message: {Decryption}")


encrypt()
decrypt()
