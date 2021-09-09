#!venv/bin/python3
from getpass import getpass
from typing import final


# create a ceasar row
def ceasar(letter, row):
    endRow = ''
    finalRow = ''
    number = 0
    for char in row:
        if char == letter:
            number = 1
        if number == 1:
            finalRow += char
        if number == 0:
            endRow += char
    return f'{finalRow}{endRow}'
    print(letter)


# check if the key is only contains alphabetical characters
def checkKey(key):
    if not key.isalpha():
        print('The password can only contains alphabetical characters')
        exit()
    return key.upper()

# Create the long key string, which is as long as the sentence
def newKey(key, toCode):
    newKeyString = ''
    
    for x in range((int(len(toCode)//int(len(key))))):
        newKeyString += key
    if len(toCode) % len(key) != 0:
        for y in  range(len(toCode)%len(key)):
            newKeyString += key[y]
    return newKeyString

def main():
    mainRow = 'AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ'
    key = getpass('Please give me the password for the encode: ')
    key = checkKey(key)
    toCode = input('Please give me the sentence, you want to encode: ')

    key = newKey(key, toCode)

    # array for the ceasar rows
    rows = []
    for char in key:
        rows.append(ceasar(char, mainRow))
    
    # here will come the encode 
    for charNum in range(len(toCode)):
        print(f'the character: {toCode[charNum]}\nThe encoded character: {rows[charNum]}')


if '__main__' == __name__:
    main()