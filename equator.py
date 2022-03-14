import sys

with open(sys.argv[1], 'r') as fp:
    for jim in fp:
        print(jim.rstrip('\n\r'))