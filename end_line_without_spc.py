#!/usr/bin/python
import argparse
import re
import sys

parser = argparse.ArgumentParser(
            description='Check lines do not end with a white space.')
parser.add_argument('filename',  type=argparse.FileType('r'),
                    help='a file to be checked')
f = parser.parse_args().filename

line_no = 0
space_exists = False

for line in f:
    line_no += 1
    pattern = r' +$'
    if re.search(pattern, line):
        space_exists = True
        print >> sys.stderr, (
            'A white space exists at the end of line ' + str(line_no))

if space_exists:
    print 'NG'
    sys.exit(1)
else:
    print 'OK'
    sys.exit(0)
