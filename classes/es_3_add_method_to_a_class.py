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

# Python 2.x syntax
class Vehicle(object):
    """
    The Vehicle class
    """
    
    def __init__(self, _colors, _doors, _tires, _type):
        """Constructor"""
        self.colors = _colors   # these are attributes
        self.doors = _doors
        self.tires = _tires
        self.type = _type
    
    def brake(self):
        """
        Stop the car
        """
        # return "Bracking"
        return "{}'s bracking".format(self.type)
        
    def drive(self):
        """
        Drive the car
        """
        # return "I'm driving"
        return "I'm driving a {} with {} doors".format(self.type, self.doors)
        
if __name__ == "__main__":
    
    # makes a first instance of the object vehicle
    car = Vehicle("blue", 5, 4, "car")
    print( car.brake() )
    print( car.drive() )
    
    # makes a second instance of the object vehicle
    truck = Vehicle("red", 3, 6, "truck")
    print( truck.brake() )
    print( truck.drive() )
    