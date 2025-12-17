#!/usr/bin/env python3

from multiprocessing import Pool

testcase = True
if testcase:
    file = "test2.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Device:
    def __init__(self,name,outputs):
        self.name = name
        self.outputs = outputs
        self.paths_fft = 0  # paths to the end that include 'fft' on the downstream side.
        self.paths_dac = 0
        self.paths_fftdac = 0
        self.complete = [False,False,False,False] # fftdac, fft, dac, neither
        self.inputs=[]
    def print(self):
        print(f"{self.name}: Inputs {self.inputs}  Outputs {self.outputs} Paths {self.paths_fft} {self.paths_dac} {self.paths_fftdac}")

def FindPaths(loc,devices,path):
    # there may be loops that never end up at 'out'
    total = 0
    for dev in devices[loc].outputs:
        if dev in path:
            print("Loop!")
            # could delete this path (after this loop is done)
            exit(1)

        if(dev == 'out'):
            total += 1
            # return this path
        else:
            # we don't really need to keep track of the whole path, except to stop loops?
            new_path = path.copy()
            new_path.append(dev)
            total += FindPaths(dev,devices,new_path)

    return total

def FindPaths2(loc,devices,path,depth):
    fork_at_depth = 3
    # there may be loops that never end up at 'out'
    total = 0
    for dev in devices[loc].outputs:
        if dev in path:
            print("Loop!")
            # could delete this path (after this loop is done)
            exit(1)

        if(dev == 'out'):
#            print("Found the end!  Do something.")
            if('dac' in path and 'fft' in path):
                print(path)
                total += 1
        else:
            # we don't really need to keep track of the whole path, except to stop loops?
            depth += 1
            new_path = path.copy()
            # only put the devices we care about in memory
#            if(dev == 'fft' or dev == 'dac'):
#                new_path.append(dev)
            new_path.append(dev)
            total += FindPaths2(dev,devices,new_path,depth)

    return total

## need to build a memory of an exit points and how many paths
# it takes to get to the end from there.
# ie, reverse this to Depth-First-Search

# Test case paths are:
# ['aaa', 'fft', 'ccc', 'eee', 'dac', 'fff', 'ggg']
# ['aaa', 'fft', 'ccc', 'eee', 'dac', 'fff', 'hhh']

## We need to keep track of paths 'below' that included fft or dac or both.
## and if the current path has the other missing components.

def FindPathswMemory(next,devices,path):
    tot_fft = 0
    tot_dac = 0
    tot_fftdac = 0
    status = False

    for dev in devices[next].outputs:

        if(dev == 'out'):
            return (True,path)

        # process from this new device

### TODO... hhmm..  do we need multiple 'complete' statuses?
## whether we got her with either, none, or both required devices?

        # MEMORY
        if(('fft' in path and 'dac' in path and devices[dev].complete[0] == True) or
          ('fft' in path and devices[dev].complete[1] == True) or
          ('dac' in path and devices[dev].complete[2] == True) or
          devices[dev].complete[3] == True):


#        if(devices[dev].complete == True):
        # TODO.. if dev already has paths_* completed we don't have to process it again.
        # we might need a 'proccessed' variable
        # if it's already processed we just check our path against devices[dev].paths*
        # and calculate the totals.

            if(devices[dev].paths_fftdac > 0):
                status = True
                tot_fftdac += devices[dev].paths_fftdac
            if(devices[dev].paths_fft > 0 and 'dac' in path):
                status = True
                tot_fft += devices[dev].paths_fft
            if(devices[dev].paths_dac > 0 and 'fft' in path):
                status = True
                tot_dac += devices[dev].paths_dac

        # also set status=True here if needed.

        else:
            # only store the two points we care about in memory
            new_path = path.copy()
            if(dev == 'fft' or dev == 'dac'):
                new_path.append(dev)

            # True/False for fft/dac?
            (ret_status, ret_path) = FindPathswMemory(dev,devices,new_path)

            # After return, we now keep keep track of which combinations of 
            # downstream paths had fft/dac... if our current path has the other(s)
            # and remove fft/dac from the current path before returning if that's
            # the current device

            # NOTE.. path also has to actually get to 'out' in order to count.

            # We're processing the 'next' device here.  Add up the path totals and add them to device[next]
            if(ret_status):
                if('fft' in ret_path and 'dac' in ret_path):
                    tot_fftdac += 1
                elif('fft' in ret_path):
                    tot_fft += 1
                elif('dac' in ret_path):
                    tot_dac += 1
                status = True  # any one of our downstreams will suffice.

        if('fft' in path and 'dac' in path):
            devices[dev].complete[0]=True
        elif('fft' in path):
            devices[dev].complete[1]=True
        elif('dac' in path):
            devices[dev].complete[2]=True
        else:
            devices[dev].complete[3]=True

    devices[next].paths_fftdac = tot_fftdac
    devices[next].paths_fft = tot_fft
    devices[next].paths_dac = tot_dac

    # remove fft/fac from path that is == the next value?
    if(next == 'fft'):
        del path[path.index('fft')]
    elif(next == 'dac'):
        del path[path.index('dac')]
    
    return (status,path)
    

def PopulateInputs(devices):
    # for each device tell the output device that this is a potential input
    for d in devices:
        for dev in devices[d].outputs:
            devices[dev].inputs.append(d)


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

    devices = {}
    for line in lines:
        (dev,paths) = line.split(':')
        paths = paths.split(' ')
        paths.pop(0)
        devices[dev] = Device(dev,paths)

    paths = []
#    total1 = FindPaths('you',devices,[])
#    temp = FindPaths2('svr',devices,[],0)
    devices['out'] = Device('out',[])
    PopulateInputs(devices)
    devices['out'].paths_to_end=len(devices['out'].inputs)

    (status,path) = FindPathswMemory('svr',devices,[])

    total2 = devices['svr'].paths_fftdac

    for d in devices:
        devices[d].print()

    return (total1,total2)



if(__name__ == '__main__'):    
    (total1,total2) = run_with_file(file)

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")







    



