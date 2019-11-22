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

# the simplest class in python
class Rec(object): pass

if __name__ == "__main__":
    new_rec = Rec()
    print( dir(new_rec) )

    # ['__doc__', '__module__']

    # Methods named __something__ are special hooks in Python
    # Such methods are called automatically when instances appear in built-in operations
    # Classes may override most built-in type operations
    # There are no defaults for operator overloading methods, and none are required
    #
    # usually we mean to overrride the __init__ method...    