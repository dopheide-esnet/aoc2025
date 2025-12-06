#!/usr/bin/env python3

def TestWorks():
    return True

def SortRangesByMin(r):
    (a,b) = r.split('-')
    return int(a)

def CombineRanges(ranges):
    '''
    Takes a list of integer ranges (ie, ['2-5', '11-15', '6-12', '17-19']) and outputs
    a list of non-overlapping ranges (ie ['2-15', '17-19'])
    '''
    new_ranges = []

    # Lets start by sorting by the ranges by minimum value
    ranges.sort(key=SortRangesByMin)

    i = 0
    while(i < len(ranges)-1):
        (a,b) = ranges[i].split('-')
        (c,d) = ranges[i+1].split('-')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

#        print(f"processing {a}-{b},{c}-{d}")

        if(c <= b + 1):
            # ranges overlap, minimum at a
            min = a
            if(b < d):
                max = d
            else:
                max = b
            # min-max range replaces a-b,c-d in ranges[]
            del ranges[i]
            ranges[i] = f"{min}-{max}"
        else:
            # no overlap, add (a,b) to new_ranges
            new_ranges.append(f"{a}-{b}")
            # delete a-b from ranges[]
            del ranges[i]

    # at the end we should have one range left
    new_ranges.extend(ranges)
    return new_ranges


if(__name__ == '__main__'):    

    ranges = ['2-5', '11-15', '6-12', '17-19']
    new_ranges = CombineRanges(ranges)
    print(new_ranges)
