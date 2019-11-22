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

class With_Override(object):
    
    def __init__(self, _value):
        """
        Constructor
        """
        self.data = _value
    
    def __add__(self, _other):
        """
        it runs on a + expression
        """
        return With_Override(self + _other)
    
    def __str__(self):
        """
        Printing run this - mainly is ot use for user friendly displays
        """
        # return "{}, {}, {}".format(self.section_type, self.lenght,, self.width)
        return "print from __str__: {}".format(self.data)
        
    def __repr__(self):
        """
        Interactive console and REPL display this
        """
        return "print from __repr__"
        
if __name__ == "__main__":
    
    test_1 = With_Override("abc")
    print(test_1)
    
    str(test_1)
    print( repr(test_1) )
    