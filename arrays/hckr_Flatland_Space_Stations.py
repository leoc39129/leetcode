#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # loop through stations, looking at adjacent stations
    # the max distance between two stations int div 2 is the max 
    # distance from a city to a station
    # while we loop through, update d_max (maximum distance at that
    # moment from a city to a station)
    
    # to begin, set d_max to first city -> first station
    # then loop through stations, updating d_max along the way
    c.sort()
    
    first = c[0]
    last = n-1 - c[-1]
    d_max = max(first, last)
    #print(d_max)
    
    for idx in range(len(c) - 1):
        d_max = max(d_max, (c[idx + 1] - c[idx]) // 2)
    # we still need to check last station to last city
    # let's fix that by appending n to c (n will be the # of last
    # city, that way we don't need to leave the loop)

    '''
    # Somehow this works:

    spot1 = c[idx]
        spot2 = c[idx + 1]
        cur_dist = (spot2 - spot1) // 2
        #print(cur_dist)
        if cur_dist > d_max:
            d_max = cur_dist

    # But this part didn't:
    
    c.append(n-1)
    c.sort()
    
    spot1 = 0
    spot2 = c[0]
    cur_dist = (spot2 - spot1) // 2
    d_max = cur_dist
    
    # (instead of initially setting d_max to max(0 -> first station, last station -> last city), append
    # last city to end of list, and set d_max to 0 -> first station)
    '''
    
    return d_max
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
