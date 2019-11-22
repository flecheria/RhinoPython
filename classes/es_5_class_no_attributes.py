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

class Strange_Test:
    """
    A class without attributes and a very strange methods
    """
    
    def set_data(self, _value):
        """
        Set the value of data attribute
        """
        self.data = _value
    
    def display_data(self):
        """
        Display the data attribute
        """
        print(self.data)
    
    def strange_method(self):
        """
        a method that use a value that doesn.t exist inside the class
        """
        return self.value * 2
        
if __name__ == "__main__":
     x = Strange_Test()
     y = Strange_Test()
     
     # print(x.data)
     # x.data = "string 2"
     
     x.set_data("String")
     x.display_data()
     
     y.set_data(3.1425)
     y.display_data()
     
     # now we set a new attribute...
     x.value = 7
     # and we use it
     print( x.strange_method() )
     y.value = 8.5
     print( y.strange_method() )
     
     # all attributes are public
     # it's possible change a value without using any method
     x.data = 9
     x.display_data()