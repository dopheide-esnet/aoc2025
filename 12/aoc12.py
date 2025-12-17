#!/usr/bin/env python3

from multiprocessing import Pool

testcase = True
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


    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



