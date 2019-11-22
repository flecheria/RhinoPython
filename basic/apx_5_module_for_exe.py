import rhinoscriptsyntax as rs
from random import random

from apx_6_module_for_testing import test

def test_single():
    return str(random() * 50)

if __name__ == "__main__":
    
    com = '_Line 0,0,0 '
    
    for i in range(4):
        # new_com = com + test_single() + ',' + test_single() + ',' + test_single()
        new_com = com + test(50) + ',' + test(20) + ',' + test(19.26)
        rs.Command(new_com)
    
    
    rs.Command('_Circle 25,50,90 80')
