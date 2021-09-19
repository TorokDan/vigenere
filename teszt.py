from getpass import getpass
import argparse

# for the arguments
def parsing():
    parser = argparse.ArgumentParser(description='just for fun... hehe')
    # parser.add_argument('-t', '--teszt', action='store_true')
    parser.add_argument('-a', '--tesztA', nargs='?')
    parser.add_argument('-b', '--tesztB', nargs='?')
    return parser.parse_args()


if '__main__' == __name__:
    args = parsing()
    # if args.tesztA == None and args.tesztB == None:
    #     print('Hahahahahahahah')
    # elif args.tesztA != None and args.tesztB == None:
    #     print(args.tesztA)
    # else:
    #     print(args.tesztB)
    print(args)