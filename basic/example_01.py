######################################################################
#
# DO NOT CANCEL THIS PART
# Author: Paolo Cappelletto
# e-mail: info@flecheria.it
# skype: flecheria
# Date: 191014
# Version: 1.0
# 
# Copyright: MIT License
#
######################################################################

b = 10

def Test2():
    b = 50
    return b

def Test(value):
    c = b * value
    global b
    b = 20
    return c

def Test3():
    return None

if __name__ == "__main__":
    a = 5
    print(Test2())
    
    result = Test(a)
    print(result)
    print(b)
    
#    another test
    null = 86
    print(null)
    
#    and the last one
    print(Test3())
    
#Variable names can only contain these characters:
#  Lowercase letters (a through z)
#  Uppercase letters (A through Z)
#  Digits (0 through 9)
#  Underscore (_)
#Names cannot begin with a digit. Also, Python treats names that begin with an underscore
#in special ways (which you can read about in Chapter 4). These are valid names:
#  a
#  a1
#  a_b_c___95
#  _abc
#  _1a
#These names, however, are not valid:
#  1
#  1a
#  1_