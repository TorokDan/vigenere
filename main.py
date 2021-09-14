#!venv/bin/python3
from getpass import getpass
from typing import final
import argparse

# for the arguments
def parsing():
    parser = argparse.ArgumentParser(description='just for fun... hehe')
    parser.add_argument('-d', '--decode', action='store_true')
    return parser.parse_args()

# generate a ceasar row
def ceasar(letter, row):
    position = row.find(letter)
    return row[position:] + row[:position]


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

def encode(code, mainRow, rows):
    output = ''
    for charNumTo in range(len(code)):
        for numMain in range(len(mainRow)):
            if mainRow[numMain] == code[charNumTo]:
                output += rows[charNumTo][numMain]
    return output

def decode(code, mainRow, rows, key):
    output = ''
    for numKey in range(len(key)):
        for charNumRow in range(len(rows[numKey])):
            if rows[numKey][charNumRow] == code[numKey]:
                output += mainRow[charNumRow]
    return output

def main():
    args = parsing()
    mainRow = 'AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐőPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz .!?'

    # get the 'password'
    key = getpass('Please give me the password for the encode: ')
    key = checkKey(key)
    rows = []

    # encode
    if args.decode == False:
        toCode = input('Please give me the sentence, you want to encode: ')

        key = newKey(key, toCode)

        # array for the ceasar rows
        for char in key:
            rows.append(ceasar(char, mainRow))
        
        # output
        print(encode(toCode, mainRow, rows))
    if args.decode == True:
        fromCode = input('Please give me the sentence, you want to decode: ')

        key = newKey(key, fromCode)

        # array for the ceasar rows
        for char in key:
            rows.append(ceasar(char, mainRow))

        print(decode(fromCode, mainRow, rows, key))

        


if '__main__' == __name__:
    main()