#!/usr/bin/env python3

import time

# try and figure out how multi processing works with python

from multiprocessing import Pool

def f(x):
    time.sleep(5*x)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

