LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message, key):
    result = ""
    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            num += key
            encrypted +=  LETTERS[num]
        else:
            encrypted += symbol
    return encrypted

def decrypt(message, key):
    decrypted = ''
    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            num -= key
            decrypted +=  LETTERS[num]
        else:
            decrypted += symbol
    return decrypted

def bruteforce(message):
    for key in range(26):
        plaintext = ""
        for letter in message:
            if letter in LETTERS:
                num = LETTERS.find(letter)
                num += key
                plaintext +=  LETTERS[num]
        print(plaintext)

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26] or 0 for bruteforce: '))
    if(key == 0):
        print(bruteForce(message))
    else:
        choice = input('Encrypt or Decrypt? [E/D]: ')
        if choice.lower().startswith('e'):
            print(encrypt(message, key))
        else:
            print(decrypt(message, key))
