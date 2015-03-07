#!/usr/bin/python
import sys
import re

line_no = 0
space_exists = False

for line in sys.stdin:
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
