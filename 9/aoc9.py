#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test6.txt"
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
    total1=0  # number of splits
    total2=0

    reds = []
    for line in lines:
        (a,b) = line.split(',')
        reds.append([int(a),int(b)])

    # Part 1
#    max_area = 0
#    for i in range(len(reds)):
#        for j in range(len(reds)):
#            if(i != j):
#                area = (abs(reds[j][0]-reds[i][0])+1) * (abs(reds[j][1]-reds[i][1])+1)
#                if(area > max_area):
#                    max_area = area
#                    max_pair = [i,j]
#    total1 = max_area

    # Part 2
    max_area = 0

    # build edges, keeping track of horizontal vs vertical
    horizontal = []
    vertical = []
    for i in range(len(reds)):
        if(i == len(reds)-1):
            j = 0
        else:
            j = i+1

        if(reds[i][0] == reds[j][0]):
            # add them all top to bottom
            if(reds[j][1] < reds[i][1]):
                vertical.append([reds[j][0],reds[j][1],reds[i][0],reds[i][1]])
            else:
                vertical.append([reds[i][0],reds[i][1],reds[j][0],reds[j][1]])
        elif(reds[i][1] == reds[j][1]):
            # add them left to right
            if(reds[i][0] < reds[j][0]):
                horizontal.append([reds[i][0],reds[i][1],reds[j][0],reds[j][1]])
            else:
                horizontal.append([reds[j][0],reds[j][1],reds[i][0],reds[i][1]])

#    print(horizontal)
#    print(vertical)

    for i in range(len(reds)):
        for j in range(len(reds)):
            if(i != j):
                area = (abs(reds[j][0]-reds[i][0])+1) * (abs(reds[j][1]-reds[i][1])+1)

                # if the area wouldn't be greater than the max good area, don't do the rest
                if(area < max_area):
                    continue

                # identify the opposite corners of the rectangle
                op1 = [ reds[j][0] , reds[i][1] ]
                op2 = [ reds[i][0] , reds[j][1] ]

                skip=True
                insides = [False,False]
                oi=0
                for op in [op1,op2]:
                    # for each opposite corner, determine if it's 'inside' the rectangle.
                    # first, is it on any of our edges, that would count as 'inside'
                    for [x1,y1,x2,y2] in horizontal:
                        if y1==op[1] and x1<=op[0] and op[0]<=x2:
                            insides[oi]=True

                    # It could also be on a vertical edge, but for vertical edges
                    # to the right of the point, we have to see what the Ray Casting value is
                    if(insides[oi]==False): 
                        intersections = 0      
                        for [x1,y1,x2,y2] in vertical:
                            if x1==op[0] and y1<=op[1] and op[1] <= y2:
                                insides[oi]=True

                            # We're casting a ray to the right
                            
                            if(insides[oi] == False) and (x2 > op[0]):
                                # For any vertical edge to the right, if y1 < op[1] < y2
                                # then we hit it?
                                if(y1 < op[1] and y2 > op[1]):
                                    intersections += 1
                        if(intersections % 2 == 1):  
                            # odd number, this is inside the polygon
                            insides[oi]=True
                    oi+=1

                if(insides == [True,True]):
                    skip=False
#                    print("valid")

                # finally, it's possible we have this situation:
                # #xxxxxxx#
                # x  #xx# x
                # x  x  x x
                # #xx#  #x#
                # So we need to know if any of this rectangle's edges would cross another edge.

#TODO  do we have this situation?
                # TODO but just going up and right back down would still be valid... 
                #  I really hope that's not an edge case in the data...

                # should probably build this into the vertical/horizontal loops above, but I'm too confused right now
                # bottom left corner is:
                if(skip == False):
                    # bottom edge
                    blx = min([op1[0],op2[0]])
                    bly = max([op1[1],op2[1]])
                    brx = max([op1[0],op2[0]])
                    bry = bly

                    # top edge
                    tlx = blx
                    tly = min([op1[1],op2[1]])
                    trx = brx
                    trry = tly  # can't use 'try'  (top right y)
                    
                    # check if the top/bottom edge cross any verticals
                    bottom_xs = []
                    top_xs = []
                    for [x1,y1,x2,y2] in vertical:
                        if blx < x1 and brx > x1:
                            if bly > y1 and bly <= y2:
                                bottom_xs.append(x1)

                        if tlx < x1 and trx > x1:
                            if tly >= y1 and tly < y2:
                                top_xs.append(x1)

                    if(len(bottom_xs) > 0):
                        for i in range(len(bottom_xs)-1):
                            if(bottom_xs[i] == bottom_xs[i+1]+1):
                                # side by side can be ignored
                                # but let's warn about it for now
                                print("side by side inlet from bottom")
                                exit()
                    if(len(top_xs) > 0):
                        for i in range(len(top_xs)-1):
                            if(top_xs[i] == top_xs[i+1]+1):
                                # side by side can be ignored
                                # but let's warn about it for now
                                print("side by side inlet from top")
                                exit()

                    if(len(bottom_xs)>0 or len(top_xs)>0):
                        skip = True
                        break 

                    if(skip == False):
                        left_ys = []
                        right_ys = []
                        # check if the left/right sides cross any horizontals
                        for [x1,y1,x2,y2] in horizontal:
                            if tly < y1 and bly > y1:
                                if tlx >= x1 and tlx < x2:
                                    left_ys.append(y1)
                            
                            if trry < y1 and bry > y1:
                                if trx < x1 and trx <= x2:
                                    right_ys.append(y1)
                                   
                        if(len(left_ys) > 0):
                            for i in range(len(left_ys)-1):
                                if(left_ys[i] == left_ys[i+1]+1):
                                    # side by side can be ignored
                                    # but let's warn about it for now
                                    print("side by side inlet from left")
                                    exit()
                        if(len(right_ys) > 0):
                            for i in range(len(right_ys)-1):
                                if(right_ys[i] == right_ys[i+1]+1):
                                    # side by side can be ignored
                                    # but let's warn about it for now
                                    print("side by side inlet from right")
                                    exit()
                        if(len(left_ys)>0 or len(right_ys)>0):
                            skip = True
                            break 


                if(skip==False):
                    if(area > max_area):
                        max_area = area

    total2 = max_area


    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print("Running w/ test2.txt")
    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



