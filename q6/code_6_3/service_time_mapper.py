#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove whitespace and split row into values
    line_split = line.strip().split("\t")
    # assign case, activity, timestamp
    case = line_split[1]
    service_time= line_split[19]
    # write the results to STDOUT;
    # key: case, value: (timestamp,activity)
    print('%s\t%s' % (case, service_time))


