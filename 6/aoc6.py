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
    total1=0
    total2=0

    input = []

    for line in lines:
        input.append(line.split())

    # Part 1
    for j in range(len(input[0])):

        for i in reversed(range(len(input))):
            if i == len(input)-1:
                op = input[i].pop(0)
            elif i == len(input)-2:
                subtotal = int(input[i].pop(0))
            else:
                num = int(input[i].pop(0))
                if(op == '*'):
                    subtotal *= num
                elif(op == '+'):
                    subtotal += num
        total1 += subtotal

    # Part 2
    input = []
    for line in lines:
        input.append(list(line))

    # todo, loop for range(len(input[0]))
#    for j in range(len(input[0])):
    nums = []
    for j in range(len(input[0])):
        subtotal = 0
        num = ''
        for i in range(len(input)):

            if(i == len(input)-1) and len(input[i]) > 0:
                maybe = input[i].pop(0)
                if(maybe != ' '):
                    op = maybe
#                    print("op",op)

            else:
#                print("here",input[i])
                if(len(input[i])>0):
                    maybe = input[i].pop(0)
                    if(maybe != ' '):
                        num = num + maybe # append to string

        if(num == ''):
            #print("do math",op,nums)
            subtotal = int(nums[0])
            for n in range(1,len(nums)):
                if(op == '+'):
                    subtotal += int(nums[n])
                elif(op == '*'):
                    subtotal *= int(nums[n])
            total2 += subtotal
            nums = []
        else:
            nums.append(num)
#            print("do math",op,nums)

    # do math one last time.
    #print("do math",op,nums)
    subtotal = int(nums[0])
    for n in range(1,len(nums)):
        if(op == '+'):
            subtotal += int(nums[n])
        elif(op == '*'):
            subtotal *= int(nums[n])
    total2 += subtotal




    


    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



