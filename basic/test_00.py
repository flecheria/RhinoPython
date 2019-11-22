######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

def DummyFunction(value):
    c = 3.512 * value
    return c
    
def my_addiction(a, b):
    return a + b

if __name__ == "__main__":
    a = 10
    b = 23.56
    c = True
    d = "string"
    d1 = 'string'
    
    result = a + b
    
    print(a)
    print(b)
    print(c)
    print(d)
    print(d1)
    print(result)
    
    print( type(a) )
    print( type(b) )
    print( type(c) )
    print( type(d) )
    print( type(d1) )
    print( type(result) )
    
    # print( my_addiction(a, d) )