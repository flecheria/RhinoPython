######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

if __name__ == "__main__":
    #Strings
    # Change case
    # Strip space off the end of a string
    # Split a string
    test_string = '  this is a test   '
    print(test_string.upper())
    print(test_string.lower())
    print(test_string.strip(' '))
    print(test_string.translate(None, ' '))
    print(test_string.split(' '))
    #Integers and decimals
    # Add and subtract
    # Simple math
    
    #Lists
    # Add to or subtract from the list
    # Remove the last item of the list
    # Reorder the list
    # Sort the list
    dog_names = ['Joker', 'Simon', 'Ellie', 'Lishka', 'Turtle']
    dog_names.append('Walter')
    dog_names.remove('Simon')
    
    print(dog_names)
    
    print(dir(dog_names))
    for d in dir(dog_names):
        print(d)
    
    #Dictionaries
    # Add a key/value pair
    # Set a new value to the corresponding key
    # Look up a value by the key