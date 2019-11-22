######################################################################
#
# Arc example from Rhinocommon
# 
# Copyright: MIT License
#
######################################################################

import rhinoscriptsyntax as rs

def range_float(start, stop, step):
    if(stop == None):
        stop = start + 0.0
    if(step == None):
        step = 1.0
    while start < stop:
        yield start
        start += step

def range_float_rec(start, stop, step):
    if(start < stop):
        return [start] + range_float_rec(start + step, stop, step)
    else:
        return [stop]

if __name__ == "__main__":
    
    a = range_float_rec(1.25, 3.5, 0.256)
    print(a)
    
    for i in range_float(1.25, 3.5, 0.256):
        print(i)

