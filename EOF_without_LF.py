#!/usr/bin/python
import sys

file_str = sys.stdin.read()

if file_str[-2:] == '\n\n':
    print >> sys.stderr, 'End with a line feed codes'
    print 'NG'
    sys.exit(1)

print 'OK'
