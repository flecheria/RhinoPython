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

#Assign variable
#In Python, everything booleans, integers, floats, strings,
#even large data structures, functions, and programs 
#is implemented as an object.

#This is the global scope, the space outside function and main module definition
#and this is a variable...
b = 5

def my_addition(a, b):
    return a + b

def Test(value):
    c = b * value
    global a
    a = 560
    global b
    print("--- I'm printing from the function ", b)
    b = 20
    return c

#This the entry point of your module, the main module.
#Pratically this the main program.
#Every python file (.py) is a module and could have or have not the main module
#But consider always to implement the main module.
#More information on:
#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    
    a = 5
    b = 12
    print(a)
    print(b) #which b is printing?
    
    result = Test(a)
    print(result)
    print(a)
    print(b)
    
#    is the way of doing secure?

#from https://www.geeksforgeeks.org/global-local-variables-python/
#Global and Local Variables in Python
#Global variables are the one that are defined and declared 
#outside a function and we need to use them inside a function.
#
# when you read something like this, forget it!!!