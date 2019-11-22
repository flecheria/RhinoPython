######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

#Some operator things

if __name__ == "__main__":
    a = 5 / 2
    print(a)
    b = 5 / 2.5
    print(b)
    c = 9 / 5
    print(c)
    d = 9 // 2
    print(d)
    e = 9 % 5
    print(e)
    f = divmod(9, 5)
    print(f) # this is intersting it produces a new kind of data
    
    #Precedence
    print(2 + 5 * 6)
    print((2 + 5) * 6)