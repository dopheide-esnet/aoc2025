#!/usr/bin/env python3

testcase = True
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

def Toggle(lights,x):
    if(lights[x] == '.'):
        lights[x] = '#'
    else:
        lights[x] = '.'

def DoButtons(presses,i,buttons,correct,lights):

    total = -1

    # Don't press this button
    if(i < len(buttons)-1):
        (good,p) = DoButtons(presses,i+1,buttons,correct,lights.copy())
        if(good):
            if total == -1 or p < total:
                total = p

    # Press this button
    presses += 1
    for x in buttons[i]:
        Toggle(lights,x)
    
    if(lights == correct):
#        print("holy shit", presses, lights)
        return (True,presses)
    elif(i < len(buttons)-1):
        (good,p) = DoButtons(presses,i+1,buttons,correct,lights.copy())
        if(good):
            if(total == -1 or p < total):
                total = p

    # Press it again!
    presses += 1
    for x in buttons[i]:
        Toggle(lights,x)
    
    if(lights == correct):
#        print("holy shit", presses, lights)
        return (True,presses)
    elif(i < len(buttons)-1):
        (good,p) = DoButtons(presses,i+1,buttons,correct,lights.copy())
        if(good):
            if(total == -1 or p < total):
                total = p

    if(total != -1):
        return (True,total)

    return (False,total)

def GeneratePresses(wgp,how_many):
    presses = []
    for hm in range(how_many):
        if(len(presses) == 0):
            for b in wgp:            
                presses.append([b])
            print(presses)
        else:
            new_presses = []
            for b in wgp:
                for p in range(len(presses)):
                    pl = presses[p].copy()
                    pl.append(b)
                    new_presses.append(pl)
            presses = new_presses
            
    # order doesn't matter so let's sort and uniq them.
    for p in presses:
        p.sort()
    
    # normal list(set()) doesn't work on a list of lists.
    # Thank you, Google.  But now we have tuples... 
    presses = list(dict.fromkeys(tuple(sublist) for sublist in presses))
    presses = list(list(sublist) for sublist in presses)
    return presses


def DoButtons2(presses,buttons,correct,j,jolts):
    total = -1

    # Currently try to fulfill the obligations of correct[j], given our current jolts status.

    were_gonna_press = []
    for i in range(len(buttons)):
        if(j in buttons[i]):
            were_gonna_press.append(i)
    
    print("pressing",were_gonna_press)
    how_many = correct[j] - jolts[j]
    print("how many", how_many)

    # These are all the new things we're going to try and add to various
    # copies of jolts
    presses = GeneratePresses(were_gonna_press,how_many)
    for p in presses:
        new_jolts = jolts.copy()
        for j in p:
            print("press",j)
            
            # add to new_jolts

        # compare if any column is too big to be correct

    return (False,total)


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

    # There is no point in pressing a button more than twice, right?

    for line in lines:
        stuff = line.split()
#        print(stuff)
        correct = list(stuff[0])[1:-1]
#        print(correct)
        buttons = []
        for b in stuff[1:-1]:
            b=b.lstrip('(')
            b=b.rstrip(')')
            buttons.append(b.split(','))
        for b in buttons:
            for i in range(len(b)):
                b[i] = int(b[i])
#        print(buttons)
        j = stuff[-1].lstrip('{')
        j = j.rstrip('}')
        jolts = j.split(',')
        for j in range(len(jolts)):
            jolts[j] = int(jolts[j])

        # Attempt to brute force Part 1
#        lights = ['.'] * len(correct)
#        (good,res) = DoButtons(0,0,buttons,correct,lights.copy())
#        total1 += res

        our_jolts = [0] * len(jolts)
        (good,res) = DoButtons2(0,buttons,jolts.copy(),0,our_jolts)

        exit()
        print("only doing one so far")

    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



