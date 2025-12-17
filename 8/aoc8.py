#!/usr/bin/env python3

import math

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class JunctionBox:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.connected = False
        self.circuit_id = None
        self.neighbor = None  # closest neighbor
        self.neighbor_dist = None
        self.id = -1
    def print(self):
        print(f"{self.id} {self.x},{self.y},{self.z}  {self.connected}  {self.circuit_id}  {self.neighbor}  {self.neighbor_dist}")

#class Circuit:
#    def __init__(self,box1,box2):
#        boxes = [box1,box2]

def Dist(box1,box2):
    return math.sqrt((box2.x - box1.x)**2 + (box2.y - box1.y)**2 + (box2.z - box1.z)**2)

def SortByMinDist(box):
    return box.neighbor_dist

def SortByCircuitLen(c):
    return len(c)

def FindUnconnectedMinimums(boxes):
    min_dist = -1
    min_pair = []
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if i!=j:
                if(boxes[i].connected == True and boxes[j].connected == True and
                   boxes[i].circuit_id == boxes[j].circuit_id):

# I think I'm misintepreting:
# The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes
# were already in the same circuit, nothing happens!

# I think that still counts as a connection being added

                    continue
                else:
                    dist = Dist(boxes[i],boxes[j])
                    if(min_dist == -1 or dist < min_dist):
                        min_dist = dist
                        min_pair = [i,j]
    return min_pair

def FindAllMinimums(boxes):
    max_len = 10000 # for part2 (can be set to 1000 for part1)
    minimums = []
    minimums_dict = {}  
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if i!=j:
                dist = Dist(boxes[i],boxes[j])
                if(dist not in minimums):
                    if(len(minimums) < max_len):
                        if(dist in minimums):
                            if(minimums_dict[dist] == (j,i)):
                                continue
                            else:
                                print("oh come on! (1)")
                                # it's possible separate boxes have the exact same distance...
                                exit()
                        minimums.append(dist)
                        minimums_dict[dist] = (i,j) # maps to which boxes they are
                        minimums.sort()
                    elif dist < minimums[-1]:
                        if(dist in minimums):
                            if(minimums_dict[dist] == (j,i)):
                                continue
                            else:
                                print("oh come on! (2)")
                                # it's possible separate boxes have the exact same distance...
                                exit()
                        del minimums_dict[minimums[-1]]
                        del minimums[-1]
                        minimums_dict[dist] = (i,j)
                        minimums.append(dist)
                        minimums.sort()
    return (minimums,minimums_dict)

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

    boxes = []
    for line in lines:
        (x,y,z) = line.split(',')
        boxes.append(JunctionBox(int(x),int(y),int(z)))

    circuits = {}
    next_circuit_id = 1
    count = 0

    (m,md) = FindAllMinimums(boxes)

    while(count < 10000):

#        print("Num Circuits",len(circuits))
        # this is going to be really inefficient
#        pair = FindUnconnectedMinimums(boxes)
#        b1 = pair[0]
#        b2 = pair[1]

        if(len(m) == 0):
            print("we ran out of known minimums")
            exit()

        minimum = m.pop(0)
        (b1,b2) = md[minimum]

#        print("Minimum Pair",b1,b2)

        if(boxes[b1].connected==True and boxes[b2].connected==True):

            if(boxes[b1].circuit_id == boxes[b2].circuit_id):
#                print("oh shit")
                count+=1
                continue
            to_be_deleted = boxes[b2].circuit_id
            for b in circuits[boxes[b2].circuit_id]:
                boxes[b].circuit_id = boxes[b1].circuit_id
            circuits[boxes[b1].circuit_id].extend(circuits[to_be_deleted])
            del circuits[to_be_deleted]

            count+=1
        elif(boxes[b1].connected==False and boxes[b2].connected==False):
            circuits[next_circuit_id] = [b1,b2]
            boxes[b1].circuit_id = next_circuit_id
            boxes[b2].circuit_id = next_circuit_id
            boxes[b1].connected = True
            boxes[b2].connected = True
            next_circuit_id += 1
            count+=1
        elif(boxes[b1].connected==True and boxes[b2].connected==False):
            boxes[b2].circuit_id = boxes[b1].circuit_id
            boxes[b2].connected = True
            circuits[boxes[b1].circuit_id].append(b2)
            count+=1
        elif(boxes[b1].connected==False and boxes[b2].connected==True):
            boxes[b1].circuit_id = boxes[b2].circuit_id
            boxes[b1].connected = True
            circuits[boxes[b2].circuit_id].append(b1)
            count+=1 
        else:
            print("no")
            exit()


        # TODO, for my input, I need to keep finding minimum distances.
        # the 1000 I started with won't be enough.


        # Part 2, comment out and set while loop parameters for Part1
#        print("Num Circuits",len(circuits))
        if(count > 10 and len(circuits) == 1):
            for c in circuits:
                cir_size = len(circuits[c])
            if(cir_size == len(boxes)):
#                print(boxes[b1].print())
#                print(boxes[b2].print())
                total2 = boxes[b1].x * boxes[b2].x

#                for c in circuits:
#                    circuits[c].sort()
#                    print(circuits[c])

                break

#        for box in boxes:
#            box.print()

#    for c in circuits:
#        circuits[c].sort()
#        print(circuits[c])

# Part 1:  Uncomment this
#    keys_sorted = sorted(circuits.items(), key=lambda item: len(item[1]), reverse=True)
#    total1 = 1
#    for i in range(3):
#        (x,b) = keys_sorted[i]
#        total1 *= len(b)

    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}  (need to change code to work again)")
    print(f"Total2: {total2}")







    



