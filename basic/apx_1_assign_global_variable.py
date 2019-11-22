######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

def GlobalValue():
    return 7.34

if __name__ == "__main__":
    a = 5 + GlobalValue()
    print(a)
    
#    or as function in place (know as lambda)
    l = lambda : 7.34
    a = 5 + l()
    print(a)