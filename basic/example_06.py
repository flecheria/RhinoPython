######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

#Strings

if __name__ == "__main__":
    
    palindrome = 'A man,\nA plan,\nA canal:\n\t\tPanama.'
    print(palindrome)
    
#    Combine with +
    print('Release the kraken! ' + 'At once!')
    a = 'Release the kraken! ' + 'At once!'
    print(a)
    
    #Duplicate with *
    print("ciao " * 6)
    
    #Exatract with []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print(letters[0])
    print(letters[1])
    print(letters[-1])
    print(letters[-2])
    print(letters[25])
    print(letters[5])
    
    #you can't access what doesn't exist
    #print(letters[100})

    #String are immutable
    #https://stackoverflow.com/questions/9097994/arent-python-strings-immutable-then-why-does-a-b-work
    # http://net-informations.com/python/iq/immutable.htm
    name = 'Henny'
    # name[0] = 'P'
    name.replace('H', 'P')
    print(name)
    print('P' + name[1:])
    
    g = list('cat')
    print(g)
    
    # more on string and formatting
    # https://docs.python.org/2/library/string.html
    # https://pyformat.info/