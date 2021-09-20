from getpass import getpass
import argparse

# for the arguments
def parsing():
    parser = argparse.ArgumentParser(description='just for fun... hehe')
    parser.add_argument('-d', '--decode', action='store_true')
    parser.add_argument('-f', '--file', nargs=1)
    parser.add_argument('-p', '--password', nargs=1)
    parser.add_argument('-s', '--secret_file', nargs=1)
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
    print(args)
    mainRow = 'AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐőPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz0123456789 .,!?#$@-'

    # get the 'password'
    if args.password == None and args.secret_file == None:
        key = getpass('Please give me the password: ')
        key = checkKey(key)
    elif args.password != None and args.secret_file == None:
        key = args.password[0]
    elif args.password == None and args.secret_file != None:
        key = open(args.secret_file[0], 'r').read()
    rows = []
    # decode
    if args.decode == True and args.file == None:
        fromCode = input('Please give me the sentence, you want to decode: ')

        key = newKey(key, fromCode)

        # array for the ceasar rows
        for char in key:
            rows.append(ceasar(char, mainRow))

        print(decode(fromCode, mainRow, rows, key))
    # encode from file
    elif args.file != None and args.decode == False:
        file = args.file[0]
        fromCode = open(file, 'r').read()
        key = newKey(key, fromCode)

        # array for the ceasar rows
        for char in key:
            rows.append(ceasar(char, mainRow))
        
        toCode = open(f'{file}.vig', 'w')
        toCode.write(encode(fromCode, mainRow, rows))
        toCode.close()
    # decode from file
    elif args.file != None and args.decode == True:
        file = args.file[0]
        if file.endswith('.vig') == False:
            print('This is not a vig file. Give a file, with a .vig ending.')
        else:
            fromCode = open(file, 'r').read()
            key = newKey(key, fromCode)

            # array for the ceasar rows
            for char in key:
                rows.append(ceasar(char, mainRow))
            
            toCode = open(f'{file[:-4]}', 'w')
            toCode.write(decode(fromCode, mainRow, rows, key))
            toCode.close()
    # encode
    else:
        toCode = input('Please give me the sentence, you want to encode: ')

        key = newKey(key, toCode)

        # array for the ceasar rows
        for char in key:
            rows.append(ceasar(char, mainRow))
        
        # output
        print(encode(toCode, mainRow, rows))

if '__main__' == __name__:
    main()