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

#Conversion
if __name__ == "__main__":
    print(5)
    print( float(5) )
    print( str(5) )
    print( int(True) )
    
    print( float(True) )
    print( int(False) )
    
    print("paolo")
    
    print(type(5))
    print(type("ciao"))
    print(type(True))
    print(type(3.890))
    
#    and some confusing things
    print(True + 2)
    print(True + 2.567)
    print(True + True)
#    finally we get an error
#    print(True + " Ciao")

#    but there's always a wasy
#    print("{} Ciao".format(True))