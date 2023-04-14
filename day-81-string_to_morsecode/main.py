from morse_dictionary import MORSE_CODE_DICT


print('Welcome to my morse code translator!')
print('At any time you can type "exit" to exit program. ENJOY!')
print('Type "info" for quick explanation and tutorial.')


def encrypt(msg):
    """function that handles encryption"""
    encrypted_msg = ''
    for i, char in enumerate(msg):
        encrypted_msg += MORSE_CODE_DICT[char]
        # enumerate because I wanted to add space only if its middle letter
        if i < len(msg) - 1:
            encrypted_msg += ' '
    return encrypted_msg


def decrypt(msg):
    """function that handles decryption"""
    decrypted_msg = ''

    def get_key(morse_frag):
        for letter, morse in MORSE_CODE_DICT.items():
            if morse_frag == morse:
                return letter
        return f"**{morse} doesn't exist**"

    for char in msg.split(' '):
        decrypted_msg += get_key(char)
    return decrypted_msg


def information():
    """basic info about how program works and functions to get better user experience"""
    print('''\nProgram is basic it operates in English mainly if you type character that is not in database you will get.
Space between letters is one space
Between words there is a "/"
You can choose between "encrypt" or "decrypt"
At any time you can type "exit" to quit program\n''')


while True:
    user_input = input('Choose mode, type: encrypt/decrypt: ').upper()
    if user_input == 'ENCRYPT':
        while True:
            try:
                message = input('Type your message or "back" to go back: ').upper()
                if message == 'BACK':
                    break
                print(f'Your word in morse code is: {encrypt(message)}')
                print('Feel free to copy and use it. :)', end='\n\n')
            except KeyError as error:
                print(f"I'm sorry you can't use character {error} it's currently not in database. :( Try again.")
    elif user_input == 'DECRYPT':
        print('Please provide your decrypted message in according to the format inside "info"')
        message = input('Type your message or "back" to go back: ').upper()
        print(f'Your decrypted message is: {decrypt(message)}')
    elif user_input == 'EXIT':
        print('Thanks for using the program. Bye!')
        exit()
    elif user_input == 'INFO':
        information()
    else:
        print('Invalid input try again')
