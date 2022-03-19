import sys

linenum = int(sys.argv[1]) - 1

with open(sys.argv[2], 'r') as file:
    for i, line in enumerate(file):
        if i == linenum:
            print(line.rstrip('\n\r'))
