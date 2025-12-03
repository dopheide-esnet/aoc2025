#!/usr/bin/env python3

import re

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

    total = 0
    total2 = 0

    for line in lines:
        newline = list(line)
        bank = list(map(int,newline))
#        print(bank)

        # Part1
        # find the largest integer that isn't in the last position
        first_max = max(bank[:-1])
        # where is the first one
        start = bank[:-1].index(first_max)
        # find the next max after that one.
        second_max = max(bank[start+1:])
        total += int(f"{first_max}{second_max}")

        # Part2
        # find the largest integer that would still leave 11 remaining digits
        rd = 11  # remaining digits we need
        max1 = max(bank[:-rd])
        numstr = str(max1)
        # ?  Do we need to try all possible starting positions of this max digit?
        #    I don't think so because we'd want to use that next high digit anyways
        index = bank[:-rd].index(max1)

        # We need to track the index relative to the full bank.
        # so it'll be -rd + current index
        while(rd > 0):
            index+=1 # next bank index will be at least one more

#            print(f"rd {rd}")


            rem_len = len(bank[index:])
            window = len(bank[index:])-rd+1

#            print(rem_len,"Window",window)
#            if(window == 0):
#            if(rd == index):  # TODO, this can't be right.
#                print("now just fill it out",index,rd)
#                strbank = list(map(str,bank[index:index+rd]))
#                numstr = numstr + ''.join(strbank)
#                rd = 0
#            else:
#                print("Look for new max in",bank[index:index+window])
            m = max(bank[index:index+window])
            i = bank[index:index+window].index(m)
            index = index + i  # the new overall index of the bank
#                print("new max",m,index)
            numstr = numstr+str(m)
            rd -= 1

#        print(f"subtotal {numstr}")
        total2 += int(numstr)

    return (total,total2)


if(__name__ == '__main__'):    
    (total,total2) = run_with_file(file)

    print(f"Total1: {total}")
    print(f"Total2: {total2}")



exit(1)





    



