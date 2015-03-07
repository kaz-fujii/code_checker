#!/usr/bin/python
import argparse
import sys

parser = argparse.ArgumentParser(
            description='Check a file doesn\'t end with a line feed.')
parser.add_argument('filename',  type=argparse.FileType('r'),
                    help='a file to be checked')
f = parser.parse_args().filename
file_str = f.read()

if file_str[-2:] == '\n\n':
    print >> sys.stderr, 'End with a line feed code.'
    print 'NG'
    sys.exit(1)

print 'OK'
