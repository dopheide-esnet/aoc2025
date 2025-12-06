#!/usr/bin/env python3

import re
import clean

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

        
def TestWorks():
    return True

def run_with_file(input_file):
    try:
        stuff = open(input_file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    total1=0
    total2=0

    ranges = []
    items = []
    for line in lines:
        if '-' in line:
            ranges.append(line)
        elif line != '':
            items.append(int(line))

    ranges = clean.CombineRanges(ranges)
    items.sort()

#    print("Ranges:",ranges)
#    print("Items:",items)

    i = 0
    for r in ranges:
        (a,b) = r.split('-')
        a = int(a)
        b = int(b)
        total2 += b-a+1 # inclusive

        while(items[i] < a):
            i+=1
        
        # we're at an index that might be in this range.
        j = i
        while(j<len(items) and (items[j] <= b)):
            j+=1

        total1 += j-i
        # now we're outside the range.

    return (total1,total2)


if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



