######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

if __name__ == "__main__":
    # sets are unordered
    animal_names = {
        'cats': ['Walter', 'Ra'],
        'dogs': ['Joker', 'Simon', 'Ellie', 'Lishka', 'Fido'],
        'horses': ['Mr. Ed']
        }
    
    print(animal_names)
    print(animal_names['cats'])
    
    animal_names['mouse'] = ['computer mouse', 'mickey mouse', 'dead mouse']
    print(animal_names)
    
    for n in animal_names:
        print(n)
        print(animal_names[n])
    # more on dictionary
    # https://docs.python.org/2/tutorial/datastructures.html#dictionaries
    # https://realpython.com/python-dicts/
    
    drinks = {
        'martini': {'vodka', 'vermouth'}, 
        'black russian': {'vodka', 'kahlua'}, 
        'white russian': {'cream', 'kahlua', 'vodka'}, 
        'manhattan': {'rye', 'vermouth', 'bitters'}, 
        'screwdriver': {'orange juice', 'vodka'}
        }
    print(drinks)
    
    # iterate trough dictionary
    for name, contents in drinks.items():
        if 'vodka' in contents:
            print(name)
    
    # Combinations and operation
    for name, contents in drinks.items():
        if contents & {'vermouth', 'orange juice'}:
            print(name)