######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

def multiply(value):
    return value * 5

if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5]
    new_empty_list = []
    
    print(a)
    
    for item in a:
        b = multiply(item)
        new_empty_list.append(b)
        print(b)
    
    print(new_empty_list)