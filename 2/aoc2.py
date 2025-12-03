#!/usr/bin/env python3

# initial result
# $ time ./aoc2.py
# Dumb Total Part2: 24774350322
# Total: 12850231731
# real	0m12.598s


import re
import clean

testcase = True
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

invalid_ranges = dict()
invalids = dict()
        
def TestWorks():
    return True

def do_it_dumb(ranges):
    '''
    This is how I got the answer originally (assuming I have time to write a better version).
    While this is inefficient in a number of ways, the numbers we're dealing with aren't that large
    so sometimes it's better to just let the computer do the work.
    '''
    max = 0
    for r in ranges:
        (a,b) = r.split('-')
        if(int(b) > max):
            max = int(b)
    i = 1
    num = int(str(i)+str(i))
    repeat = len(str(max))+1
    while(num <= max):
        for j in range(2,repeat):
            check = int(str(i)*j)
            for r in ranges:
                (a,b) = r.split('-')
                if(check >= int(a) and check <= int(b)):
                    invalids[check] = 1

        i += 1
        num = int(str(i)+str(i))

    total = 0
    for n in invalids:
        total += n
    
    print(f"Dumb Total Part2: {total}")

def do_it_smarter(ranges):
    '''
    Using my new 'clean.py' module, I sort and combine the input ranges before processing.
    '''

    total = 0
    ranges = clean.CombineRanges(ranges)
    (a,b) = ranges[-1].split('-')

    for r in ranges:
        subtotal = 0
        (a,b) = r.split('-')
        # the first digit of 'a' is our starting point
        start = int(a[0])
#        print(a,b)
#        print("start",start)
        mn_repeat = max( [int(len(b)/2),2]  ) # ie, we don't need to check 333 if the minimum is 1234
        mx_repeat = len(b) # the max repeat length

        a = int(a)
        b = int(b)
        print("range",a,b)

### the next level of repeat needs to skip past the max value of the previous repeat
#  we don't want 2 2 2 2 2 2  and then 22 22 22
#  but that would potentially skip stuff in the middle? 


        for x in range(mn_repeat,mx_repeat+1):
            i = 1
            num = int(str(i)*x)
            while(num <= b):
#                    print("Try",num)
                if(num >= a and num <= b):
                    print("win",num)
                    subtotal += num
                i+=1
                num = int(str(i)*x)
            
        print("subtotal",subtotal)
        total += subtotal

    
    print(f"Part2: {total}")

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
    ranges = lines[0].split(',')
# How I got Part 2 originally
#    do_it_dumb(ranges)

    # Part 2
    do_it_smarter(ranges)

    # Part 1
    for r in ranges:
        (a,b) = r.split('-')
        total += do_range(int(a),int(b))

    return get_total()

def do_range(min,max):
    '''
    The subtotal we generate here is good for checking the range, but since ranges can overlap
    we have to make sure each invalid ID is unique.  That's why we use dict: invalid_ranges.
    '''

    subtotal = 0

    # find out the length of the minimum value divided by 2
    # we can't have an odd number of digits
    start_len = int(len(str(min)) / 2)

    # single digit minimum
    if(start_len == 0):
        a = 1
    else:
        a = int(str(min)[:start_len])
#    b = int(str(min)[start_len:])

    num = int(str(a)+str(a))

    # increase a until start >= min
    while(num < min):
        a += 1
        num = int(str(a)+str(a))

    start = num # just for tracking purposes
#    print(f"do range {min} {max} {a} {start}")
    
    while(num <= max):
#        print(f"  {num}")
        invalid_ranges[num] = 1  # part 1 only
        subtotal += num
        a += 1
        num = int(str(a)+str(a))

    return subtotal

def get_total():
    new_total = 0
    for n in invalid_ranges:
        new_total += n
    
    return new_total

if(__name__ == '__main__'):    
    total = run_with_file(file)

    print(f"Total: {total}")






    



