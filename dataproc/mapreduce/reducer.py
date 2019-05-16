#!/usr/bin/env python

import sys

total_price = 0.0
old_key = None

for line in sys.stdin:

    data = line.strip().split('\t')

    if len(data) == 2:

        this_key, this_price = data

        if old_key and old_key != this_key:

            print old_key, '\t', total_price

            total_price = 0.0

        old_key = this_key

        if float(this_price) > total_price:
            
            total_price = float(this_price)

if old_key != None:

    print old_key, '\t', total_price
