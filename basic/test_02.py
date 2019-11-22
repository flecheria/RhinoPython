######################################################################
#
# Arc example from Rhinocommon
# 
# Copyright: MIT License
#
######################################################################

import rhinoscriptsyntax as rs
from random import random

def GetValue(value):
    return random() * value

if __name__ == "__main__":
    
    for item in range(10000):
        rs.AddPoint([GetValue(80), GetValue(200), GetValue(50)])
        
        https://tinyurl.com/ydt5qd5q