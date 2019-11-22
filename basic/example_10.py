######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

from collections import namedtuple

#def return_two_values(value):
#    a = value + 5
#    b = value * 5
#    return (a, b)

def return_two_values(value):
    a = value + 5
    b = value * 5
    return a, b

if __name__ == "__main__":
    # TUPLE
    # tuple are immutable list, you can't change values sfter the assign
    a_tuple = ('ready', 'fire', 'aim')
    # this is correct
    print(a_tuple[0])
    # this gives you an error
    #a_tuple[0] = 'error'
    # useful to return multiple value from function
    print(return_two_values(9))
    first, second = return_two_values(9)
    
    empty_tuple = ()
    
    # Named tuples are not automatically supplied with Python, so you need to load a module
    # before using them. This is a convinient method to create simple object data
    Duck = namedtuple('Duck', 'bill tail')
    duck = Duck('wide orange', 'long')
    print("{} --- {}".format(duck.bill, duck.tail))
    # You can also make a named tuple from a dictionary:
    parts = {'bill': 'wide orange', 'tail': 'long'}
    duck2 = Duck(**parts)
    print(duck2)
    
    # SET
    # set of integers
    my_set = {1, 2, 3}
    print(my_set)
    # empty set
    my_set = set()
    
    # set of mixed datatypes
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)
    
    test_list = [1, 2, 3, 4, 3, 2]
    print(set(test_list))