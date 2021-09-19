from getpass import getpass
import argparse

# for the arguments
def parsing():
    parser = argparse.ArgumentParser(description='just for fun... hehe')
    # parser.add_argument('-t', '--teszt', action='store_true')
    parser.add_argument('-t', '--teszt', nargs='?')
    return parser.parse_args()


if '__main__' == __name__:
    args = parsing()
    if args.teszt == None:
        print('Hahahahahahahah')
    else:
        print(args.teszt)