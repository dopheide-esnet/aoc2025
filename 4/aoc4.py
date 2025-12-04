#!/usr/bin/env python3

import re

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

        
def TestWorks():
    return True

def PrintMap(map):
    for y in range(len(map)):
        print(''.join(map[y]))

def run_with_file(input_file):
    try:
        stuff = open(input_file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    map = []

    for line in lines:
        map.append(list(line))
#    print(map)

    bails = Part1(map)
    total1 = len(bails)
    total2 = 0
    

    while(len(bails) > 0):
        total2 += len(bails)
        # remove bails
        for (y,x) in bails:
            map[y][x] = 'x'
#        PrintMap(map)
#        print("")

        bails = Part1(map)

    return (total1,total2)

def Part1(map):
    total = 0
    subtotal = 0
    bails_to_remove = []
    for y in range(len(map)):
        for x in range(len(map[0])):

            subtotal = 0
            # check above
            if(map[y][x] == '@'):
                if(y>0):                  
                    if(x>0 and map[y-1][x-1] == '@'):
                        subtotal += 1
                    if(map[y-1][x] == '@'):
                        subtotal += 1
                    if(x<len(map[0])-1 and map[y-1][x+1] == '@'):
                        subtotal += 1

                # check this row
                if(x>0 and map[y][x-1] == '@'):
                    subtotal += 1
    # Don't count the bail itself
    #            if(map[y][x] == '@'):
    #                subtotal += 1
                if(x<len(map[0])-1 and map[y][x+1] == '@'):
                    subtotal += 1

                # check below
                if(y<len(map)-1):
                    if(x>0 and map[y+1][x-1] == '@'):
                        subtotal += 1
                    if(map[y+1][x] == '@'):
                        subtotal += 1
                    if(x<len(map[0])-1 and map[y+1][x+1] == '@'):
                        subtotal += 1

                if(subtotal < 4):
                    bails_to_remove.append((y,x))
                    total += 1
    return bails_to_remove

#def Part2(map):



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



