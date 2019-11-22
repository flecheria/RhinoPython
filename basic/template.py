######################################################################
#
# Template for rhinopython script
# 
# Copyright: MIT License
#
######################################################################

import rhinoscriptsyntax as rs

def dummy_function(value):
    return value * 2.53

if __name__ == "__main__":
    p = rs.AddPoint([0, 0, 0])
    a = dummy_function(2)
    print(a)