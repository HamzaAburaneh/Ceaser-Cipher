LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message, key):
    encryptedResult = ""
    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            num += key
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
            decryptedResult +=  LETTERS[num]
        else:
            decryptedResult += letter
    return decryptedResult

def bruteforce(message):
    for key in range(26):
        plaintext = ""
        for letter in message:
            if letter in LETTERS:
                num = LETTERS.find(letter)
                num += key
                plaintext += LETTERS[num]
            else:
                plaintext += letter
        print(plaintext)

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26] or 0 for bruteforce: '))
    if key == 0:
        print(bruteforce(message))
        return
    choice = input('Encrypt or Decrypt? [E/D]: ')
    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))

main()
