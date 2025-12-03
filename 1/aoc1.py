#!/usr/bin/env python3

import re

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

class Lock:
    def __init__(self,loc):
        self.loc = loc
        self.digits = 100
    def Move(self,move,num):
        orig_loc = self.loc
        if(move == "R"):
            self.loc += num
        else:
            self.loc -= num
    
        self.loc = self.loc % self.digits

        if(move =="R"):
            passed = int ((orig_loc+num) / self.digits)
        else:
            # moving left
            temp = int(num / self.digits)
            rem = num % self.digits
            if(rem<100):
                if(self.loc < orig_loc):
                    if(self.loc == 0):
                        passed = 1
                    else:
                        passed = 0
                else:
                    if(orig_loc == 0):
                        passed = 0
                    else:
                        passed = 1
            passed += temp

#        print(f"\n{orig_loc} {move}{num} {self.loc} passed {passed}")

        return passed
    
        
def TestWorks():
    return True

def run_with_file(input_file,start):
    try:
        stuff = open(input_file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    lock = Lock(start)
    total = 0
    total2 = 0
    for line in lines:
        m = re.search(r'([LR])(\d+)',line)
        if(m):
            move = m.group(1)
            num = int(m.group(2))
            passed = lock.Move(move,num)
            total2 += passed
            print(f"Move {move}{num} passed {passed} loc {lock.loc} ")
            if lock.loc == 0:
                total += 1
    
    return (total, total2)

if(__name__ == '__main__'):    
    (total,total2) = run_with_file(file,50)

    print(f"Total 1: {total}\nTotal 2: {total2}")



    



