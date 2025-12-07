#!/usr/bin/env python3

import re

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"


def TestWorks():
    return True

def FindIndices(stuff,c):
    idx = []
    for s in range(len(stuff)):
        if(stuff[s] == c):
            idx.append(s)
    return idx

def run_with_file(input_file):
    try:
        stuff = open(input_file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()
    total1=0  # number of splits
    total2=0

    for i in range(len(lines)):
        lines[i] = list(lines[i])
    start = lines[0].index('S')

    beams={start: 1}  # list of active beam locations

    all_beams = [] # for Part2
    for i in range(1,len(lines)):
        splitters = FindIndices(lines[i],'^')
        for s in splitters:
            if s in beams:
                total1+=1
                if(s > 0):
                    beams[s-1] = 1
                if(s < len(lines[i])-1):
                    beams[s+1] = 1
                del beams[s]
        all_beams.append(beams.copy()) # add copy of beams

#    all_beams.append(beams.copy()) # the last row just continues

    i = len(lines)-4  # start three rows up from the bottom
    while(i > 0):
 #       print(all_beams[i])
 #       print(lines[i+2])
        for b in all_beams[i]:
#            print(b)
            if(lines[i+2][b] == '^'):
#                print("add up beam numbers")
                sub = all_beams[i+2][b-1] + all_beams[i+2][b+1]
 #               print("sub:",sub)                    
                all_beams[i][b] = sub
            else:
                all_beams[i][b]=all_beams[i+2][b]

        # Print the calculation row
#        for b in range(len(lines[i])):
#            if(b in all_beams[i]):
#                print(all_beams[i][b],end='')
#            else:
#                print(".",end='')
#        print()

        i -= 2 # skip up to rows

    for b in all_beams[2]:
        total2 += all_beams[2][b]
    #print(all_beams[2])

    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



