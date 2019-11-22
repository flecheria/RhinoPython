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

from es_3_add_method_to_a_class import *

# create a subclass:
# - superclasses are listed in parentheses inside the class header
# - classes inherit attributes form their superclasses
# - instances inherit attributes from all accessible classe
# - logic changes are made by subclassing, not changing superclasses

class Car(Vehicle):
    """
    The car class
    """
    
    def brake(self):
        """
        Override brake method
        """
        return "this is a different bracking system!"
    
    # a method unique for the car object
    def onboard_pc(self, _state):
        """
        presence of the personal control
        """
        if(_state):
            return "the control is present"
        else:
            return "the control is not present"
    
if __name__ == "__main__":
    
    # makes a new instance of the object car
    car = Car("yellow", 2, 4, "car")
    print( car.brake() )
    # use the car method
    print( car.onboard_pc(True) )
    print( car.onboard_pc(False) )