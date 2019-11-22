######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

#Lambda and anonimous functions are complex and profound topic
#more examples here, for our scope now it doesn't matter
#but keep in mind
#https://www.w3schools.com/python/python_lambda.asp

def myfunc(n):
    return lambda a : a * n 

if __name__ == "__main__":
    x = lambda a, b, c : a + b + c
    print(x(5, 6, 2)) 
    
    y = lambda a, b : a * b
    print(y(5, 6))
    
    # do you see anything to do with variable assignment here?
    mydoubler = myfunc(2)
    print(mydoubler(11))