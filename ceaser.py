LETTERS = 'abcdefghijklmnopqrstuvwxyz'
#add more or make a web app in js with multiple cyphers
def encrypt(message, key):
    encryptedResult = ""
    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            num += key
            if num > 26:
                num -= 26
            encryptedResult +=  LETTERS[num]
        else:
            encryptedResult += letter
    return encryptedResult

def decrypt(message, key):
    decryptedResult = ''
    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            num -= key
            if num > 26:
                num -= 26
            decryptedResult +=  LETTERS[num]
        else:
            decryptedResult += letter
    return decryptedResult

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')
    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))

main()
