from getpass import getpass
import argparse

# for the arguments
def parsing():
    parser = argparse.ArgumentParser(description='just for fun')
    parser.add_argument('-d', '--decode', action='store_true')
    parser.add_argument('-f', '--file', nargs=1)
    parser.add_argument('-p', '--password', nargs=1)
    parser.add_argument('-s', '--secret_file', nargs=1)
    parser.add_argument('-o', '--output', nargs=1)
    return parser.parse_args()

# ceasar sor létrehozása
def ceasar(letter, row):
    position = row.find(letter)
    return row[position:] + row[:position]

# ellenőrzi, hogy a jelszó csak az abc betűit használja-e
def checkKey(key):
    if not key.isalpha():
        print('A jelszó csak az abc betűit tartalmazhatja!')
        exit()
    return key.upper()

# A megadott jelszóból létrehoz egy ugyan olyan hosszúságú kulcsot, mint a megadott szöveg
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
    mainRow = 'AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐőPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz0123456789 .,!?#$@-\/\'[]*&<>%_§()|~\"'

    # jelszó bekérése, megadott argumentumok lekezelése
    if args.password == None and args.secret_file == None:
        key = getpass('Kérlek add meg a jelszót: ')
        key = checkKey(key)
    elif args.password != None and args.secret_file == None:
        key = args.password[0]
    elif args.password == None and args.secret_file != None:
        key = open(args.secret_file[0], 'r').read()
    elif args.password != None and args.secret_file != None:
        print("nem lehet egyszerre jelszót, és jelszó file-t használni!")
        exit()
    rows = []
    # decode
    if args.decode == True and args.file == None:
        fromCode = input('Kérlek add meg a mondatot, amit dekódolni szeretnél: ')

        key = newKey(key, fromCode)

        # létrehoz egy arrayt a ceasar soroknak
        for char in key:
            rows.append(ceasar(char, mainRow))

        print(eval(decode(fromCode, mainRow, rows, key)))
    # titkosítás fileból
    elif args.file != None and args.decode == False:
        file = args.file[0]
        fromCode = repr(open(file, 'r').read())

        key = newKey(key, fromCode)
        # létrehoz egy arrayt a ceasar soroknak
        for char in key:
            rows.append(ceasar(char, mainRow))
        if args.output == None:
            toCode = open(f'{file}.vig', 'w')
        if args.output != None:
            if args.output[0][-4:] == '.vig':
                toCode = open(args.output[0], 'w')
            if args.file[0][-4:] != '.vig':
                toCode = open(f'{args.output[0]}.vig', 'w')
        toCode.write(encode(fromCode, mainRow, rows))
        toCode.close()
    # dekódolás fileból
    elif args.file != None and args.decode == True:
        file = args.file[0]
        fromCode = open(file, 'r').read()
        key = newKey(key, fromCode)

        # létrehoz egy arrayt a ceasar soroknak
        for char in key:
            rows.append(ceasar(char, mainRow))
        if args.output == None:
            if args.file[0][-4:] == '.vig':
                toCode = open(file[:-4], 'w')
            if args.file[0][-4:] != '.vig':
                toCode = open(f'{args.file[0]}.org', 'w')
        if args.output != None:
            if args.output[0][-4:] == '.vig':
                toCode = open(args.output[0][:-4], 'w')
            if args.output[0][-4:] != '.vig':
                toCode = open(args.output[0], 'w')
        toCode.write(eval(decode(fromCode, mainRow, rows, key)))
        toCode.close()
    # encode
    else:
        toCode = repr(input('Kérlek add meg a mondatot, amit le szeretnél titkosítani: '))

        key = newKey(key, toCode)

        # létrehoz egy arrayt a ceasar soroknak
        for char in key:
            rows.append(ceasar(char, mainRow))
        
        # output
        print(encode(toCode, mainRow, rows))

if '__main__' == __name__:
    main()