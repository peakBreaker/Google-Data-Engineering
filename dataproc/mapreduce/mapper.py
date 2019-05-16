#!/usr/bin/env python
## Implementation in python 2.7 .. yeah
import sys

for line in sys.stdin:

    data = line.strip().split(' ')

    if len(data) == 5:

        time, store, item, price, payment = data

        print '{}\t{}'.format(item, price)
