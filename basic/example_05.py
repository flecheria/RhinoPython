######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

#List

if __name__ == "__main__":
    empty_list = []
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    big_birds = ['emu', 'ostrich', 'cassowary']
    first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
    
    a = [0, 1, 2, 3, 4, 5]
    b = [0, True, "test", 2.36]
    
    #You can also make an empty list with the list() function:
    another_empty_list = list()
    
    perfectly_fine = ['Graham', True, 10, 10.56]
    
    print( first_names[0] )
    print(first_names[-1])
    print(first_names[-2])
    print(first_names[:])
    print(first_names[2:])
    print(first_names[1:3])
    
    # more on list and its API
    # https://docs.python.org/2/tutorial/datastructures.html
    
    # a glimpse in for loop, the main way to iterate a list
    for i in range(10):
        print(i)
        
    # what produce range()
    print(type(range(10)))
    
    # so we can iterate
    for d in weekdays:
        print(d)
    
    for i in range(len(weekdays)):
        print(str(i) + " " + weekdays[i])
        #or better
        print("{0} {1}".format(i, weekdays[i]))
    
    for i, d in enumerate(weekdays):
        print("{0} {1}".format(i, d))